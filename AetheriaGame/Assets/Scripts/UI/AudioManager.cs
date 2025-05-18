using UnityEngine;
using System.Collections.Generic;

public class AudioManager : MonoBehaviour
{
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

    [Header("Audio Sources")]
    public AudioSource musicSource;
    public AudioSource sfxSource;
    public AudioSource voiceSource;

    [Header("Sound Effects")]
    public Sound[] soundEffects;

    [Header("Music")]
    public Sound[] musicTracks;

    [Header("Voice")]
    public Sound[] voiceLines;

    private Dictionary<string, Sound> soundDictionary = new Dictionary<string, Sound>();
    private float musicVolume = 0.8f;
    private float sfxVolume = 1f;
    private float voiceVolume = 1f;

    private void Awake()
    {
        InitializeAudioSources();
        InitializeSoundDictionary();
        LoadVolumeSettings();
    }

    private void InitializeAudioSources()
    {
        if (musicSource == null)
        {
            musicSource = gameObject.AddComponent<AudioSource>();
            musicSource.playOnAwake = false;
            musicSource.loop = true;
        }

        if (sfxSource == null)
        {
            sfxSource = gameObject.AddComponent<AudioSource>();
            sfxSource.playOnAwake = false;
        }

        if (voiceSource == null)
        {
            voiceSource = gameObject.AddComponent<AudioSource>();
            voiceSource.playOnAwake = false;
        }
    }

    private void InitializeSoundDictionary()
    {
        foreach (Sound s in soundEffects)
        {
            s.source = sfxSource;
            soundDictionary[s.name] = s;
        }

        foreach (Sound s in musicTracks)
        {
            s.source = musicSource;
            soundDictionary[s.name] = s;
        }

        foreach (Sound s in voiceLines)
        {
            s.source = voiceSource;
            soundDictionary[s.name] = s;
        }
    }

    private void LoadVolumeSettings()
    {
        musicVolume = PlayerPrefs.GetFloat("MusicVolume", 0.8f);
        sfxVolume = PlayerPrefs.GetFloat("SFXVolume", 1f);
        voiceVolume = PlayerPrefs.GetFloat("VoiceVolume", 1f);

        musicSource.volume = musicVolume;
        sfxSource.volume = sfxVolume;
        voiceSource.volume = voiceVolume;
    }

    public void PlayMusic(string name)
    {
        if (soundDictionary.TryGetValue(name, out Sound sound))
        {
            musicSource.clip = sound.clip;
            musicSource.volume = sound.volume * musicVolume;
            musicSource.pitch = sound.pitch;
            musicSource.loop = sound.loop;
            musicSource.Play();
        }
    }

    public void PlaySFX(string name)
    {
        if (soundDictionary.TryGetValue(name, out Sound sound))
        {
            sfxSource.PlayOneShot(sound.clip, sound.volume * sfxVolume);
        }
    }

    public void PlayVoice(string name)
    {
        if (soundDictionary.TryGetValue(name, out Sound sound))
        {
            voiceSource.clip = sound.clip;
            voiceSource.volume = sound.volume * voiceVolume;
            voiceSource.pitch = sound.pitch;
            voiceSource.loop = sound.loop;
            voiceSource.Play();
        }
    }

    public void StopMusic()
    {
        musicSource.Stop();
    }

    public void StopVoice()
    {
        voiceSource.Stop();
    }

    public void SetMusicVolume(float volume)
    {
        musicVolume = volume;
        musicSource.volume = volume;
        PlayerPrefs.SetFloat("MusicVolume", volume);
    }

    public void SetSFXVolume(float volume)
    {
        sfxVolume = volume;
        sfxSource.volume = volume;
        PlayerPrefs.SetFloat("SFXVolume", volume);
    }

    public void SetVoiceVolume(float volume)
    {
        voiceVolume = volume;
        voiceSource.volume = volume;
        PlayerPrefs.SetFloat("VoiceVolume", volume);
    }

    public void PlaySFX(AudioClip clip)
    {
        if (clip != null)
        {
            sfxSource.PlayOneShot(clip, sfxVolume);
        }
    }
} 