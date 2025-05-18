using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.Collections;
using DG.Tweening;

public class StatusEffectPrefab : MonoBehaviour
{
    [Header("UI References")]
    [SerializeField] private Image effectIcon;
    [SerializeField] private TextMeshProUGUI effectNameText;
    [SerializeField] private Image durationBar;
    [SerializeField] private TextMeshProUGUI durationText;
    [SerializeField] private Image background;

    [Header("Animation Settings")]
    [SerializeField] private float fadeInDuration = 0.3f;
    [SerializeField] private float fadeOutDuration = 0.3f;
    [SerializeField] private AnimationCurve fadeCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);

    private CanvasGroup canvasGroup;
    private float currentDuration;
    private float maxDuration;
    private bool isActive;

    private void Awake()
    {
        canvasGroup = GetComponent<CanvasGroup>();
        if (canvasGroup == null)
        {
            canvasGroup = gameObject.AddComponent<CanvasGroup>();
        }
    }

    public void Initialize(Sprite icon, string effectName, float duration)
    {
        effectIcon.sprite = icon;
        effectNameText.text = effectName;
        maxDuration = duration;
        currentDuration = duration;
        isActive = true;

        UpdateDurationUI();
        StartCoroutine(DurationCoroutine());
        FadeIn();
    }

    private void UpdateDurationUI()
    {
        float fillAmount = currentDuration / maxDuration;
        durationBar.fillAmount = fillAmount;
        durationText.text = $"{Mathf.CeilToInt(currentDuration)}s";
    }

    private IEnumerator DurationCoroutine()
    {
        while (currentDuration > 0 && isActive)
        {
            currentDuration -= Time.deltaTime;
            UpdateDurationUI();
            yield return null;
        }

        if (isActive)
        {
            FadeOut();
        }
    }

    private void FadeIn()
    {
        canvasGroup.alpha = 0;
        canvasGroup.DOFade(1, fadeInDuration)
            .SetEase(fadeCurve);
    }

    private void FadeOut()
    {
        isActive = false;
        canvasGroup.DOFade(0, fadeOutDuration)
            .SetEase(fadeCurve)
            .OnComplete(() => Destroy(gameObject));
    }

    public void Remove()
    {
        if (isActive)
        {
            FadeOut();
        }
    }

    public void SetHighlighted(bool highlighted)
    {
        if (background != null)
        {
            background.color = highlighted ? Color.yellow : Color.white;
        }
    }
} 
} 