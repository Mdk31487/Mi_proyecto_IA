using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class PauseMenu : MonoBehaviour
{
    [Header("Menu Buttons")]
    public Button resumeButton;
    public Button optionsButton;
    public Button quitButton;

    [Header("Menu Panels")]
    public GameObject pausePanel;
    public GameObject optionsPanel;

    [Header("Audio Settings")]
    public Slider musicVolumeSlider;
    public Slider sfxVolumeSlider;
    public Slider voiceVolumeSlider;

    private UIManager uiManager;
    private AudioManager audioManager;
    private SceneLoader sceneLoader;
    private bool isPaused;

    private void Start()
    {
        uiManager = GetComponent<UIManager>();
        audioManager = GetComponent<AudioManager>();
        sceneLoader = GetComponent<SceneLoader>();

        SetupButtons();
        SetupVolumeSliders();
        HidePauseMenu();
    }

    private void Update()
    {
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            TogglePause();
        }
    }

    private void SetupButtons()
    {
        if (resumeButton != null)
        {
            resumeButton.onClick.AddListener(OnResumeClicked);
        }

        if (optionsButton != null)
        {
            optionsButton.onClick.AddListener(OnOptionsClicked);
        }

        if (quitButton != null)
        {
            quitButton.onClick.AddListener(OnQuitClicked);
        }
    }

    private void SetupVolumeSliders()
    {
        if (musicVolumeSlider != null)
        {
            musicVolumeSlider.value = PlayerPrefs.GetFloat("MusicVolume", 0.8f);
            musicVolumeSlider.onValueChanged.AddListener(OnMusicVolumeChanged);
        }

        if (sfxVolumeSlider != null)
        {
            sfxVolumeSlider.value = PlayerPrefs.GetFloat("SFXVolume", 1f);
            sfxVolumeSlider.onValueChanged.AddListener(OnSFXVolumeChanged);
        }

        if (voiceVolumeSlider != null)
        {
            voiceVolumeSlider.value = PlayerPrefs.GetFloat("VoiceVolume", 1f);
            voiceVolumeSlider.onValueChanged.AddListener(OnVoiceVolumeChanged);
        }
    }

    private void TogglePause()
    {
        isPaused = !isPaused;
        if (isPaused)
        {
            ShowPauseMenu();
        }
        else
        {
            HidePauseMenu();
        }
    }

    private void ShowPauseMenu()
    {
        Time.timeScale = 0f;
        if (pausePanel != null) pausePanel.SetActive(true);
        if (optionsPanel != null) optionsPanel.SetActive(false);
        if (audioManager != null)
        {
            audioManager.PlaySFX("Pause");
        }
    }

    private void HidePauseMenu()
    {
        Time.timeScale = 1f;
        if (pausePanel != null) pausePanel.SetActive(false);
        if (optionsPanel != null) optionsPanel.SetActive(false);
        if (audioManager != null)
        {
            audioManager.PlaySFX("Unpause");
        }
    }

    private void OnResumeClicked()
    {
        if (audioManager != null)
        {
            audioManager.PlaySFX("ButtonClick");
        }
        HidePauseMenu();
    }

    private void OnOptionsClicked()
    {
        if (audioManager != null)
        {
            audioManager.PlaySFX("ButtonClick");
        }
        if (pausePanel != null) pausePanel.SetActive(false);
        if (optionsPanel != null) optionsPanel.SetActive(true);
    }

    private void OnQuitClicked()
    {
        if (audioManager != null)
        {
            audioManager.PlaySFX("ButtonClick");
        }
        if (sceneLoader != null)
        {
            sceneLoader.LoadSceneAsync("MainMenu");
        }
    }

    private void OnMusicVolumeChanged(float volume)
    {
        if (audioManager != null)
        {
            audioManager.SetMusicVolume(volume);
        }
        PlayerPrefs.SetFloat("MusicVolume", volume);
    }

    private void OnSFXVolumeChanged(float volume)
    {
        if (audioManager != null)
        {
            audioManager.SetSFXVolume(volume);
        }
        PlayerPrefs.SetFloat("SFXVolume", volume);
    }

    private void OnVoiceVolumeChanged(float volume)
    {
        if (audioManager != null)
        {
            audioManager.SetVoiceVolume(volume);
        }
        PlayerPrefs.SetFloat("VoiceVolume", volume);
    }

    public void OnBackClicked()
    {
        if (audioManager != null)
        {
            audioManager.PlaySFX("ButtonClick");
        }
        if (pausePanel != null) pausePanel.SetActive(true);
        if (optionsPanel != null) optionsPanel.SetActive(false);
    }
} 