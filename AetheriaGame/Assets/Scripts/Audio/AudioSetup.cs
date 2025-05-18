using UnityEngine;
using UnityEngine.Audio;
using System.IO;

public class AudioSetup : MonoBehaviour
{
    [Header("Audio Mixer")]
    public AudioMixer audioMixer;

    [Header("Audio Groups")]
    public AudioMixerGroup musicGroup;
    public AudioMixerGroup sfxGroup;
    public AudioMixerGroup voiceGroup;

    [Header("Audio Clips")]
    public AudioClip[] musicTracks;
    public AudioClip[] sfxClips;
    public AudioClip[] voiceClips;

    private void Awake()
    {
        CreateAudioMixer();
        CreateAudioGroups();
        LoadAudioClips();
    }

    private void CreateAudioMixer()
    {
        if (audioMixer == null)
        {
            // Crear el AudioMixer
            audioMixer = new AudioMixer();
            audioMixer.name = "GameAudioMixer";

            // Crear los grupos de mezcla
            musicGroup = audioMixer.FindMatchingGroups("Music")[0];
            sfxGroup = audioMixer.FindMatchingGroups("SFX")[0];
            voiceGroup = audioMixer.FindMatchingGroups("Voice")[0];

            // Configurar los parámetros de volumen
            audioMixer.SetFloat("MusicVolume", 0f);
            audioMixer.SetFloat("SFXVolume", 0f);
            audioMixer.SetFloat("VoiceVolume", 0f);
        }
    }

    private void CreateAudioGroups()
    {
        if (musicGroup == null)
        {
            musicGroup = audioMixer.FindMatchingGroups("Music")[0];
        }

        if (sfxGroup == null)
        {
            sfxGroup = audioMixer.FindMatchingGroups("SFX")[0];
        }

        if (voiceGroup == null)
        {
            voiceGroup = audioMixer.FindMatchingGroups("Voice")[0];
        }
    }

    private void LoadAudioClips()
    {
        // Cargar música
        string musicPath = "Assets/Audio/Music";
        if (Directory.Exists(musicPath))
        {
            musicTracks = Resources.LoadAll<AudioClip>("Audio/Music");
        }

        // Cargar efectos de sonido
        string sfxPath = "Assets/Audio/SFX";
        if (Directory.Exists(sfxPath))
        {
            sfxClips = Resources.LoadAll<AudioClip>("Audio/SFX");
        }

        // Cargar voces
        string voicePath = "Assets/Audio/Voice";
        if (Directory.Exists(voicePath))
        {
            voiceClips = Resources.LoadAll<AudioClip>("Audio/Voice");
        }
    }

    public void SaveAudioMixer()
    {
        if (audioMixer != null)
        {
            // Guardar el AudioMixer como un asset
            #if UNITY_EDITOR
            string path = "Assets/Audio/GameAudioMixer.mixer";
            UnityEditor.AssetDatabase.CreateAsset(audioMixer, path);
            UnityEditor.AssetDatabase.SaveAssets();
            #endif
        }
    }
} 