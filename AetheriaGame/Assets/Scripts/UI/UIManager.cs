using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;
using TMPro;
using System;
using System.Collections;

public class UIManager : MonoBehaviour
{
    public static UIManager Instance { get; private set; }

    [System.Serializable]
    public class UIPanel
    {
        public string panelName;
        public GameObject panelObject;
        public CanvasGroup canvasGroup;
        public bool startVisible;
    }

    [System.Serializable]
    public class DialogueUI
    {
        public GameObject dialoguePanel;
        public TextMeshProUGUI speakerNameText;
        public TextMeshProUGUI dialogueText;
        public Image speakerPortrait;
        public GameObject choiceContainer;
        public GameObject choiceButtonPrefab;
    }

    public List<UIPanel> panels = new List<UIPanel>();
    public DialogueUI dialogueUI;
    public float fadeDuration = 0.3f;

    [Header("UI Panels")]
    public GameObject mainMenuPanel;
    public GameObject pauseMenuPanel;
    public GameObject dialoguePanel;
    public GameObject hudPanel;
    public GameObject loadingPanel;

    [Header("Notification")]
    public GameObject notificationPanel;
    public TextMeshProUGUI notificationText;
    public float defaultNotificationDuration = 2f;

    [Header("Panels")]
    public GameObject statusEffectPanel;
    public GameObject tooltipPanel;

    [Header("Status Effect Panel")]
    public Transform iconContainer;
    public GameObject statusEffectIconPrefab;

    [Header("Tooltip Panel")]
    public TextMeshProUGUI tooltipHeader;
    public TextMeshProUGUI tooltipContent;
    public RectTransform tooltipRect;

    private Dictionary<string, UIPanel> panelDictionary = new Dictionary<string, UIPanel>();
    private UIPanel currentPanel;
    private AudioManager audioManager;
    private SceneLoader sceneLoader;
    private Coroutine notificationCoroutine;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            InitializeUI();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void Start()
    {
        audioManager = GetComponent<AudioManager>();
        sceneLoader = GetComponent<SceneLoader>();

        // Ocultar todos los paneles al inicio
        if (mainMenuPanel != null) mainMenuPanel.SetActive(false);
        if (pauseMenuPanel != null) pauseMenuPanel.SetActive(false);
        if (dialoguePanel != null) dialoguePanel.SetActive(false);
        if (hudPanel != null) hudPanel.SetActive(false);
        if (loadingPanel != null) loadingPanel.SetActive(false);
        if (notificationPanel != null) notificationPanel.SetActive(false);

        SetupPanels();
        SetupTooltips();
    }

    private void InitializeUI()
    {
        foreach (var panel in panels)
        {
            panelDictionary[panel.panelName] = panel;
            if (panel.canvasGroup == null)
            {
                panel.canvasGroup = panel.panelObject.GetComponent<CanvasGroup>();
                if (panel.canvasGroup == null)
                {
                    panel.canvasGroup = panel.panelObject.AddComponent<CanvasGroup>();
                }
            }

            panel.panelObject.SetActive(panel.startVisible);
            if (!panel.startVisible)
            {
                panel.canvasGroup.alpha = 0f;
                panel.canvasGroup.interactable = false;
                panel.canvasGroup.blocksRaycasts = false;
            }
        }
    }

    private void SetupPanels()
    {
        // Configurar StatusEffectPanel
        if (statusEffectPanel != null)
        {
            RectTransform panelRect = statusEffectPanel.GetComponent<RectTransform>();
            panelRect.anchorMin = new Vector2(1, 1);
            panelRect.anchorMax = new Vector2(1, 1);
            panelRect.pivot = new Vector2(1, 1);
            panelRect.anchoredPosition = new Vector2(-20, -20);
            panelRect.sizeDelta = new Vector2(200, 100);

            // Configurar IconContainer
            if (iconContainer != null)
            {
                HorizontalLayoutGroup layout = iconContainer.GetComponent<HorizontalLayoutGroup>();
                if (layout != null)
                {
                    layout.spacing = 10;
                    layout.padding = new RectOffset(10, 10, 10, 10);
                    layout.childAlignment = TextAnchor.MiddleCenter;
                    layout.childForceExpandWidth = false;
                    layout.childForceExpandHeight = false;
                    layout.childControlWidth = true;
                    layout.childControlHeight = true;
                }
            }
        }

        // Configurar TooltipPanel
        if (tooltipPanel != null)
        {
            tooltipPanel.SetActive(false);
            RectTransform tooltipRect = tooltipPanel.GetComponent<RectTransform>();
            tooltipRect.sizeDelta = new Vector2(200, 100);
        }
    }

    private void SetupTooltips()
    {
        if (tooltipPanel != null)
        {
            // Configurar TooltipHeader
            if (tooltipHeader != null)
            {
                tooltipHeader.fontSize = 16;
                tooltipHeader.fontStyle = FontStyles.Bold;
                tooltipHeader.alignment = TextAlignmentOptions.Center;
            }

            // Configurar TooltipContent
            if (tooltipContent != null)
            {
                tooltipContent.fontSize = 14;
                tooltipContent.alignment = TextAlignmentOptions.Center;
            }
        }
    }

    public void ShowPanel(string panelName, bool fade = true)
    {
        if (panelDictionary.TryGetValue(panelName, out UIPanel panel))
        {
            if (currentPanel != null)
            {
                HidePanel(currentPanel.panelName, fade);
            }

            currentPanel = panel;
            panel.panelObject.SetActive(true);

            if (fade)
            {
                StartCoroutine(FadePanel(panel, 0f, 1f));
            }
            else
            {
                panel.canvasGroup.alpha = 1f;
                panel.canvasGroup.interactable = true;
                panel.canvasGroup.blocksRaycasts = true;
            }
        }
    }

    public void HidePanel(string panelName, bool fade = true)
    {
        if (panelDictionary.TryGetValue(panelName, out UIPanel panel))
        {
            if (fade)
            {
                StartCoroutine(FadePanel(panel, 1f, 0f, () => panel.panelObject.SetActive(false)));
            }
            else
            {
                panel.canvasGroup.alpha = 0f;
                panel.canvasGroup.interactable = false;
                panel.canvasGroup.blocksRaycasts = false;
                panel.panelObject.SetActive(false);
            }
        }
    }

    private System.Collections.IEnumerator FadePanel(UIPanel panel, float startAlpha, float targetAlpha, Action onComplete = null)
    {
        float currentTime = 0f;
        panel.canvasGroup.alpha = startAlpha;

        while (currentTime < fadeDuration)
        {
            currentTime += Time.deltaTime;
            panel.canvasGroup.alpha = Mathf.Lerp(startAlpha, targetAlpha, currentTime / fadeDuration);
            yield return null;
        }

        panel.canvasGroup.alpha = targetAlpha;
        panel.canvasGroup.interactable = targetAlpha > 0f;
        panel.canvasGroup.blocksRaycasts = targetAlpha > 0f;
        onComplete?.Invoke();
    }

    public void ShowDialogue(string speakerName, string dialogueText, Sprite speakerPortrait = null)
    {
        dialogueUI.dialoguePanel.SetActive(true);
        dialogueUI.speakerNameText.text = speakerName;
        dialogueUI.dialogueText.text = dialogueText;
        
        if (speakerPortrait != null)
        {
            dialogueUI.speakerPortrait.sprite = speakerPortrait;
            dialogueUI.speakerPortrait.gameObject.SetActive(true);
        }
        else
        {
            dialogueUI.speakerPortrait.gameObject.SetActive(false);
        }
    }

    public void HideDialogue()
    {
        dialogueUI.dialoguePanel.SetActive(false);
    }

    public void ShowChoices(List<string> choices, Action<int> onChoiceSelected)
    {
        dialogueUI.choiceContainer.SetActive(true);
        
        // Limpiar opciones anteriores
        foreach (Transform child in dialogueUI.choiceContainer.transform)
        {
            Destroy(child.gameObject);
        }

        // Crear nuevas opciones
        for (int i = 0; i < choices.Count; i++)
        {
            int choiceIndex = i; // Capturar el índice para el lambda
            GameObject choiceButton = Instantiate(dialogueUI.choiceButtonPrefab, dialogueUI.choiceContainer.transform);
            choiceButton.GetComponentInChildren<TextMeshProUGUI>().text = choices[i];
            choiceButton.GetComponent<Button>().onClick.AddListener(() => {
                onChoiceSelected?.Invoke(choiceIndex);
                dialogueUI.choiceContainer.SetActive(false);
            });
        }
    }

    public void UpdateHealthBar(float currentHealth, float maxHealth)
    {
        // Implementar actualización de barra de vida
    }

    public void UpdateExperienceBar(float currentExp, float maxExp)
    {
        // Implementar actualización de barra de experiencia
    }

    public void ShowNotification(string message, float duration = -1)
    {
        if (duration < 0)
        {
            duration = defaultNotificationDuration;
        }

        if (notificationPanel != null && notificationText != null)
        {
            if (notificationCoroutine != null)
            {
                StopCoroutine(notificationCoroutine);
            }
            notificationCoroutine = StartCoroutine(ShowNotificationCoroutine(message, duration));
        }
    }

    private IEnumerator ShowNotificationCoroutine(string message, float duration)
    {
        notificationPanel.SetActive(true);
        notificationText.text = message;

        yield return new WaitForSeconds(duration);

        notificationPanel.SetActive(false);
    }

    public void ShowMainMenu()
    {
        if (mainMenuPanel != null)
        {
            mainMenuPanel.SetActive(true);
        }
    }

    public void ShowPauseMenu()
    {
        if (pauseMenuPanel != null)
        {
            pauseMenuPanel.SetActive(true);
        }
    }

    public void ShowHUD()
    {
        if (hudPanel != null)
        {
            hudPanel.SetActive(true);
        }
    }

    public void ShowLoading()
    {
        if (loadingPanel != null)
        {
            loadingPanel.SetActive(true);
        }
    }

    public void HideMainMenu()
    {
        if (mainMenuPanel != null)
        {
            mainMenuPanel.SetActive(false);
        }
    }

    public void HidePauseMenu()
    {
        if (pauseMenuPanel != null)
        {
            pauseMenuPanel.SetActive(false);
        }
    }

    public void HideHUD()
    {
        if (hudPanel != null)
        {
            hudPanel.SetActive(false);
        }
    }

    public void HideLoading()
    {
        if (loadingPanel != null)
        {
            loadingPanel.SetActive(false);
        }
    }

    public void ShowTooltip(string header, string content, Vector2 position)
    {
        if (tooltipPanel != null)
        {
            tooltipPanel.SetActive(true);
            if (tooltipHeader != null) tooltipHeader.text = header;
            if (tooltipContent != null) tooltipContent.text = content;
            if (tooltipRect != null) tooltipRect.position = position;
        }
    }

    public void HideTooltip()
    {
        if (tooltipPanel != null)
        {
            tooltipPanel.SetActive(false);
        }
    }
} 