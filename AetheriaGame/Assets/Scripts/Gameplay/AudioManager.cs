using UnityEngine;
using System.Collections.Generic;
using System;

public class AudioManager : MonoBehaviour
{
    public static AudioManager Instance { get; private set; }

    [System.Serializable]
    public class Sound
    {
        public string name;
        public AudioClip clip;
        [Range(0f, 1f)]
        public float volume = 1f;
        [Range(0.1f, 3f)]
        public float pitch = 1f;
        public bool loop = false;
        [HideInInspector]
        public AudioSource source;
    }

    [System.Serializable]
    public class AudioMixerGroup
    {
        public string name;
        [Range(0f, 1f)]
        public float volume = 1f;
        public List<Sound> sounds = new List<Sound>();
    }

    public List<AudioMixerGroup> mixerGroups = new List<AudioMixerGroup>();
    public float masterVolume = 1f;
    public bool isMuted = false;

    private Dictionary<string, AudioSource> activeSources = new Dictionary<string, AudioSource>();

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            InitializeAudio();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void InitializeAudio()
    {
        foreach (var group in mixerGroups)
        {
            foreach (var sound in group.sounds)
            {
                sound.source = gameObject.AddComponent<AudioSource>();
                sound.source.clip = sound.clip;
                sound.source.volume = sound.volume * group.volume * masterVolume;
                sound.source.pitch = sound.pitch;
                sound.source.loop = sound.loop;
                sound.source.playOnAwake = false;
            }
        }
    }

    public void PlaySound(string soundName, string groupName = "Default")
    {
        if (isMuted) return;

        var group = mixerGroups.Find(g => g.name == groupName);
        if (group == null) return;

        var sound = group.sounds.Find(s => s.name == soundName);
        if (sound == null) return;

        sound.source.Play();
        activeSources[soundName] = sound.source;
    }

    public void StopSound(string soundName)
    {
        if (activeSources.ContainsKey(soundName))
        {
            activeSources[soundName].Stop();
            activeSources.Remove(soundName);
        }
    }

    public void StopAllSounds()
    {
        foreach (var source in activeSources.Values)
        {
            source.Stop();
        }
        activeSources.Clear();
    }

    public void SetGroupVolume(string groupName, float volume)
    {
        var group = mixerGroups.Find(g => g.name == groupName);
        if (group != null)
        {
            group.volume = Mathf.Clamp01(volume);
            foreach (var sound in group.sounds)
            {
                if (sound.source != null)
                {
                    sound.source.volume = sound.volume * group.volume * masterVolume;
                }
            }
        }
    }

    public void SetMasterVolume(float volume)
    {
        masterVolume = Mathf.Clamp01(volume);
        foreach (var group in mixerGroups)
        {
            foreach (var sound in group.sounds)
            {
                if (sound.source != null)
                {
                    sound.source.volume = sound.volume * group.volume * masterVolume;
                }
            }
        }
    }

    public void ToggleMute()
    {
        isMuted = !isMuted;
        AudioListener.volume = isMuted ? 0f : 1f;
    }

    public void FadeIn(string soundName, float duration, string groupName = "Default")
    {
        StartCoroutine(FadeSound(soundName, 0f, 1f, duration, groupName));
    }

    public void FadeOut(string soundName, float duration)
    {
        StartCoroutine(FadeSound(soundName, 1f, 0f, duration));
    }

    private System.Collections.IEnumerator FadeSound(string soundName, float startVolume, float targetVolume, float duration, string groupName = "Default")
    {
        var group = mixerGroups.Find(g => g.name == groupName);
        if (group == null) yield break;

        var sound = group.sounds.Find(s => s.name == soundName);
        if (sound == null) yield break;

        float currentTime = 0f;
        float start = startVolume * sound.volume * group.volume * masterVolume;
        float target = targetVolume * sound.volume * group.volume * masterVolume;

        while (currentTime < duration)
        {
            currentTime += Time.deltaTime;
            sound.source.volume = Mathf.Lerp(start, target, currentTime / duration);
            yield return null;
        }

        sound.source.volume = target;
    }
} 