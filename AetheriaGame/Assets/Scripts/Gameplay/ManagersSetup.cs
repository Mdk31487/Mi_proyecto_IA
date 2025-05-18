using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class ManagersSetup : MonoBehaviour
{
    [Header("UI Configuration")]
    public GameObject mainMenuPanel;
    public GameObject pauseMenuPanel;
    public GameObject dialoguePanel;
    public GameObject hudPanel;
    public GameObject loadingPanel;

    [Header("Audio Configuration")]
    public AudioClip[] musicTracks;
    public AudioClip[] sfxClips;
    public AudioClip[] voiceClips;

    [Header("Fade Configuration")]
    public float sceneFadeDuration = 1f;
    public float uiFadeDuration = 0.3f;

    private void Awake()
    {
        SetupGameManager();
        SetupUIManager();
        SetupAudioManager();
        SetupSceneLoader();
    }

    private void SetupGameManager()
    {
        GameManager gameManager = gameObject.AddComponent<GameManager>();
        // El GameManager se configura automáticamente en su Awake
    }

    private void SetupUIManager()
    {
        UIManager uiManager = gameObject.AddComponent<UIManager>();
        uiManager.fadeDuration = uiFadeDuration;

        // Configurar paneles UI
        uiManager.panels = new System.Collections.Generic.List<UIManager.UIPanel>
        {
            CreateUIPanel("MainMenu", mainMenuPanel, true),
            CreateUIPanel("PauseMenu", pauseMenuPanel, false),
            CreateUIPanel("HUD", hudPanel, false),
            CreateUIPanel("Loading", loadingPanel, false)
        };

        // Configurar sistema de diálogo
        uiManager.dialogueUI = new UIManager.DialogueUI
        {
            dialoguePanel = dialoguePanel,
            speakerNameText = dialoguePanel.transform.Find("SpeakerName")?.GetComponent<TextMeshProUGUI>(),
            dialogueText = dialoguePanel.transform.Find("DialogueText")?.GetComponent<TextMeshProUGUI>(),
            speakerPortrait = dialoguePanel.transform.Find("SpeakerPortrait")?.GetComponent<Image>(),
            choiceContainer = dialoguePanel.transform.Find("ChoicesContainer")?.gameObject,
            choiceButtonPrefab = Resources.Load<GameObject>("UI/ChoiceButton")
        };
    }

    private void SetupAudioManager()
    {
        AudioManager audioManager = gameObject.AddComponent<AudioManager>();

        // Configurar grupos de audio
        audioManager.mixerGroups = new System.Collections.Generic.List<AudioManager.AudioMixerGroup>
        {
            CreateAudioGroup("Music", musicTracks, 0.8f),
            CreateAudioGroup("SFX", sfxClips, 1f),
            CreateAudioGroup("Voice", voiceClips, 1f)
        };
    }

    private void SetupSceneLoader()
    {
        SceneLoader sceneLoader = gameObject.AddComponent<SceneLoader>();
        sceneLoader.fadeDuration = sceneFadeDuration;

        // Crear canvas de fade
        GameObject fadeCanvas = new GameObject("FadeCanvas");
        Canvas canvas = fadeCanvas.AddComponent<Canvas>();
        canvas.renderMode = RenderMode.ScreenSpaceOverlay;
        canvas.sortingOrder = 999;

        CanvasScaler scaler = fadeCanvas.AddComponent<CanvasScaler>();
        scaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
        scaler.referenceResolution = new Vector2(1920, 1080);

        fadeCanvas.AddComponent<GraphicRaycaster>();

        // Crear imagen de fade
        GameObject fadeImage = new GameObject("FadeImage");
        fadeImage.transform.SetParent(fadeCanvas.transform, false);
        Image image = fadeImage.AddComponent<Image>();
        image.color = Color.black;

        RectTransform rectTransform = fadeImage.GetComponent<RectTransform>();
        rectTransform.anchorMin = Vector2.zero;
        rectTransform.anchorMax = Vector2.one;
        rectTransform.sizeDelta = Vector2.zero;

        // Configurar SceneLoader
        sceneLoader.fadeCanvasGroup = fadeCanvas.AddComponent<CanvasGroup>();
        sceneLoader.fadeImage = image;
    }

    private UIManager.UIPanel CreateUIPanel(string name, GameObject panelObject, bool startVisible)
    {
        if (panelObject == null)
        {
            Debug.LogWarning($"Panel {name} no encontrado!");
            return null;
        }

        CanvasGroup canvasGroup = panelObject.GetComponent<CanvasGroup>();
        if (canvasGroup == null)
        {
            canvasGroup = panelObject.AddComponent<CanvasGroup>();
        }

        return new UIManager.UIPanel
        {
            panelName = name,
            panelObject = panelObject,
            canvasGroup = canvasGroup,
            startVisible = startVisible
        };
    }

    private AudioManager.AudioMixerGroup CreateAudioGroup(string name, AudioClip[] clips, float volume)
    {
        var group = new AudioManager.AudioMixerGroup
        {
            name = name,
            volume = volume,
            sounds = new System.Collections.Generic.List<AudioManager.Sound>()
        };

        foreach (var clip in clips)
        {
            if (clip != null)
            {
                group.sounds.Add(new AudioManager.Sound
                {
                    name = clip.name,
                    clip = clip,
                    volume = 1f,
                    pitch = 1f,
                    loop = name == "Music"
                });
            }
        }

        return group;
    }
} 