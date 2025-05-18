using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class UISetup : MonoBehaviour
{
    [Header("Panel References")]
    public GameObject mainMenuPanel;
    public GameObject pauseMenuPanel;
    public GameObject dialoguePanel;
    public GameObject hudPanel;
    public GameObject loadingPanel;

    [Header("Dialogue Panel References")]
    public TextMeshProUGUI speakerNameText;
    public TextMeshProUGUI dialogueText;
    public Image speakerPortrait;
    public GameObject choicesContainer;

    [Header("References")]
    public Canvas mainCanvas;
    public StatusEffectPanel statusEffectPanel;
    public TooltipSystem tooltipSystem;
    public Button testBurnButton;
    public Button testStunButton;

    [Header("Prefabs")]
    public GameObject statusEffectIconPrefab;

    [Header("Sprites")]
    public Sprite burnIcon;
    public Sprite stunIcon;

    private void Awake()
    {
        SetupPanels();
        SetupDialoguePanel();
    }

    private void Start()
    {
        SetupCanvas();
        SetupStatusEffectPanel();
        SetupTooltipSystem();
        SetupTestButtons();
    }

    private void SetupPanels()
    {
        // Configurar MainMenuPanel
        if (mainMenuPanel != null)
        {
            SetupPanel(mainMenuPanel, "MainMenu", true);
        }

        // Configurar PauseMenuPanel
        if (pauseMenuPanel != null)
        {
            SetupPanel(pauseMenuPanel, "PauseMenu", false);
        }

        // Configurar DialoguePanel
        if (dialoguePanel != null)
        {
            SetupPanel(dialoguePanel, "Dialogue", false);
        }

        // Configurar HUDPanel
        if (hudPanel != null)
        {
            SetupPanel(hudPanel, "HUD", false);
        }

        // Configurar LoadingPanel
        if (loadingPanel != null)
        {
            SetupPanel(loadingPanel, "Loading", false);
        }
    }

    private void SetupPanel(GameObject panel, string name, bool startVisible)
    {
        // Añadir CanvasGroup si no existe
        CanvasGroup canvasGroup = panel.GetComponent<CanvasGroup>();
        if (canvasGroup == null)
        {
            canvasGroup = panel.AddComponent<CanvasGroup>();
        }

        // Configurar RectTransform
        RectTransform rectTransform = panel.GetComponent<RectTransform>();
        if (rectTransform != null)
        {
            rectTransform.anchorMin = Vector2.zero;
            rectTransform.anchorMax = Vector2.one;
            rectTransform.sizeDelta = Vector2.zero;
            rectTransform.anchoredPosition = Vector2.zero;
        }

        // Configurar visibilidad inicial
        panel.SetActive(startVisible);
        canvasGroup.alpha = startVisible ? 1f : 0f;
        canvasGroup.interactable = startVisible;
        canvasGroup.blocksRaycasts = startVisible;
    }

    private void SetupDialoguePanel()
    {
        if (dialoguePanel == null) return;

        // Crear SpeakerName si no existe
        if (speakerNameText == null)
        {
            GameObject speakerNameObj = new GameObject("SpeakerName");
            speakerNameObj.transform.SetParent(dialoguePanel.transform, false);
            speakerNameText = speakerNameObj.AddComponent<TextMeshProUGUI>();
            RectTransform speakerNameRect = speakerNameText.GetComponent<RectTransform>();
            speakerNameRect.anchorMin = new Vector2(0, 1);
            speakerNameRect.anchorMax = new Vector2(0.3f, 1);
            speakerNameRect.pivot = new Vector2(0, 1);
            speakerNameRect.anchoredPosition = new Vector2(20, -20);
            speakerNameRect.sizeDelta = new Vector2(200, 40);
        }

        // Crear DialogueText si no existe
        if (dialogueText == null)
        {
            GameObject dialogueTextObj = new GameObject("DialogueText");
            dialogueTextObj.transform.SetParent(dialoguePanel.transform, false);
            dialogueText = dialogueTextObj.AddComponent<TextMeshProUGUI>();
            RectTransform dialogueTextRect = dialogueText.GetComponent<RectTransform>();
            dialogueTextRect.anchorMin = new Vector2(0, 0);
            dialogueTextRect.anchorMax = new Vector2(1, 0.3f);
            dialogueTextRect.pivot = new Vector2(0.5f, 0);
            dialogueTextRect.anchoredPosition = new Vector2(0, 20);
            dialogueTextRect.sizeDelta = new Vector2(-40, -40);
        }

        // Crear SpeakerPortrait si no existe
        if (speakerPortrait == null)
        {
            GameObject portraitObj = new GameObject("SpeakerPortrait");
            portraitObj.transform.SetParent(dialoguePanel.transform, false);
            speakerPortrait = portraitObj.AddComponent<Image>();
            RectTransform portraitRect = speakerPortrait.GetComponent<RectTransform>();
            portraitRect.anchorMin = new Vector2(0, 0);
            portraitRect.anchorMax = new Vector2(0.2f, 0.4f);
            portraitRect.pivot = new Vector2(0, 0);
            portraitRect.anchoredPosition = new Vector2(20, 20);
            portraitRect.sizeDelta = new Vector2(0, 0);
        }

        // Crear ChoicesContainer si no existe
        if (choicesContainer == null)
        {
            GameObject choicesObj = new GameObject("ChoicesContainer");
            choicesObj.transform.SetParent(dialoguePanel.transform, false);
            choicesContainer = choicesObj;
            RectTransform choicesRect = choicesContainer.GetComponent<RectTransform>();
            choicesRect.anchorMin = new Vector2(0.5f, 0);
            choicesRect.anchorMax = new Vector2(0.5f, 0.4f);
            choicesRect.pivot = new Vector2(0.5f, 0);
            choicesRect.anchoredPosition = new Vector2(0, 20);
            choicesRect.sizeDelta = new Vector2(400, 200);

            // Añadir VerticalLayoutGroup
            VerticalLayoutGroup layout = choicesContainer.AddComponent<VerticalLayoutGroup>();
            layout.spacing = 10;
            layout.padding = new RectOffset(10, 10, 10, 10);
            layout.childAlignment = TextAnchor.MiddleCenter;
            layout.childForceExpandWidth = true;
            layout.childForceExpandHeight = false;
            layout.childControlWidth = true;
            layout.childControlHeight = true;
        }
    }

    private void SetupCanvas()
    {
        if (mainCanvas == null)
        {
            mainCanvas = GetComponent<Canvas>();
        }

        CanvasScaler scaler = mainCanvas.GetComponent<CanvasScaler>();
        if (scaler != null)
        {
            scaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
            scaler.referenceResolution = new Vector2(1920, 1080);
            scaler.screenMatchMode = CanvasScaler.ScreenMatchMode.MatchWidthOrHeight;
            scaler.matchWidthOrHeight = 0.5f;
        }
    }

    private void SetupStatusEffectPanel()
    {
        if (statusEffectPanel != null)
        {
            statusEffectPanel.statusEffectIconPrefab = statusEffectIconPrefab;
        }
    }

    private void SetupTooltipSystem()
    {
        if (tooltipSystem != null)
        {
            tooltipSystem.tooltip.gameObject.SetActive(false);
        }
    }

    private void SetupTestButtons()
    {
        if (testBurnButton != null)
        {
            testBurnButton.onClick.AddListener(() => {
                StatusEffectSystemTest test = FindObjectOfType<StatusEffectSystemTest>();
                if (test != null)
                {
                    test.TestBurnEffect();
                }
            });
        }

        if (testStunButton != null)
        {
            testStunButton.onClick.AddListener(() => {
                StatusEffectSystemTest test = FindObjectOfType<StatusEffectSystemTest>();
                if (test != null)
                {
                    test.TestStunEffect();
                }
            });
        }
    }
} 