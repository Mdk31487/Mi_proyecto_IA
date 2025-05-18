using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.Collections;

public class StatusEffectUI : MonoBehaviour
{
    [Header("UI Elements")]
    public Image effectIcon;
    public TextMeshProUGUI effectNameText;
    public Image durationBar;
    public TextMeshProUGUI durationText;

    private float duration;
    private float remainingDuration;
    private Coroutine durationCoroutine;

    public void Initialize(string effectName, Sprite icon, float effectDuration)
    {
        if (effectNameText != null)
        {
            effectNameText.text = effectName;
        }

        if (effectIcon != null && icon != null)
        {
            effectIcon.sprite = icon;
        }

        duration = effectDuration;
        remainingDuration = effectDuration;

        if (durationBar != null)
        {
            durationBar.fillAmount = 1f;
        }

        if (durationText != null)
        {
            durationText.text = $"{Mathf.Ceil(remainingDuration)}s";
        }

        if (durationCoroutine != null)
        {
            StopCoroutine(durationCoroutine);
        }
        durationCoroutine = StartCoroutine(UpdateDuration());
    }

    private IEnumerator UpdateDuration()
    {
        while (remainingDuration > 0)
        {
            remainingDuration -= Time.deltaTime;

            if (durationBar != null)
            {
                durationBar.fillAmount = remainingDuration / duration;
            }

            if (durationText != null)
            {
                durationText.text = $"{Mathf.Ceil(remainingDuration)}s";
            }

            yield return null;
        }

        Destroy(gameObject);
    }

    public void RefreshDuration(float newDuration)
    {
        duration = newDuration;
        remainingDuration = newDuration;

        if (durationBar != null)
        {
            durationBar.fillAmount = 1f;
        }

        if (durationText != null)
        {
            durationText.text = $"{Mathf.Ceil(remainingDuration)}s";
        }
    }

    private void OnDestroy()
    {
        if (durationCoroutine != null)
        {
            StopCoroutine(durationCoroutine);
        }
    }
} 