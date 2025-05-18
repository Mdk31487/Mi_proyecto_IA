using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class MainMenu : MonoBehaviour
{
    [Header("Menu Buttons")]
    public Button startButton;
    public Button optionsButton;
    public Button creditsButton;
    public Button quitButton;

    [Header("Menu Panels")]
    public GameObject mainPanel;
    public GameObject optionsPanel;
    public GameObject creditsPanel;

    private UIManager uiManager;
    private AudioManager audioManager;
    private SceneLoader sceneLoader;

    private void Start()
    {
        uiManager = GetComponent<UIManager>();
        audioManager = GetComponent<AudioManager>();
        sceneLoader = GetComponent<SceneLoader>();

        SetupButtons();
        ShowMainPanel();
    }

    private void SetupButtons()
    {
        if (startButton != null)
        {
            startButton.onClick.AddListener(OnStartClicked);
        }

        if (optionsButton != null)
        {
            optionsButton.onClick.AddListener(OnOptionsClicked);
        }

        if (creditsButton != null)
        {
            creditsButton.onClick.AddListener(OnCreditsClicked);
        }

        if (quitButton != null)
        {
            quitButton.onClick.AddListener(OnQuitClicked);
        }
    }

    private void OnStartClicked()
    {
        if (audioManager != null)
        {
            audioManager.PlaySFX("ButtonClick");
        }

        if (sceneLoader != null)
        {
            sceneLoader.LoadSceneAsync("Modulo2");
        }
    }

    private void OnOptionsClicked()
    {
        if (audioManager != null)
        {
            audioManager.PlaySFX("ButtonClick");
        }

        ShowOptionsPanel();
    }

    private void OnCreditsClicked()
    {
        if (audioManager != null)
        {
            audioManager.PlaySFX("ButtonClick");
        }

        ShowCreditsPanel();
    }

    private void OnQuitClicked()
    {
        if (audioManager != null)
        {
            audioManager.PlaySFX("ButtonClick");
        }

        #if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
        #else
        Application.Quit();
        #endif
    }

    private void ShowMainPanel()
    {
        if (mainPanel != null) mainPanel.SetActive(true);
        if (optionsPanel != null) optionsPanel.SetActive(false);
        if (creditsPanel != null) creditsPanel.SetActive(false);
    }

    private void ShowOptionsPanel()
    {
        if (mainPanel != null) mainPanel.SetActive(false);
        if (optionsPanel != null) optionsPanel.SetActive(true);
        if (creditsPanel != null) creditsPanel.SetActive(false);
    }

    private void ShowCreditsPanel()
    {
        if (mainPanel != null) mainPanel.SetActive(false);
        if (optionsPanel != null) optionsPanel.SetActive(false);
        if (creditsPanel != null) creditsPanel.SetActive(true);
    }

    public void OnBackClicked()
    {
        if (audioManager != null)
        {
            audioManager.PlaySFX("ButtonClick");
        }

        ShowMainPanel();
    }
} 