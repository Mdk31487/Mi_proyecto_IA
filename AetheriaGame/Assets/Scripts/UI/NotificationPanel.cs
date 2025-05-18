using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.Collections;

public class NotificationPanel : MonoBehaviour
{
    [Header("UI Elements")]
    public TextMeshProUGUI notificationText;
    public Image background;
    public CanvasGroup canvasGroup;

    [Header("Animation Settings")]
    public float fadeInDuration = 0.3f;
    public float fadeOutDuration = 0.3f;
    public float displayDuration = 2f;
    public AnimationCurve fadeCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);

    private Coroutine currentCoroutine;

    private void Awake()
    {
        if (canvasGroup == null)
        {
            canvasGroup = GetComponent<CanvasGroup>();
            if (canvasGroup == null)
            {
                canvasGroup = gameObject.AddComponent<CanvasGroup>();
            }
        }
    }

    public void ShowNotification(string message, float duration = -1)
    {
        if (duration < 0)
        {
            duration = displayDuration;
        }

        if (currentCoroutine != null)
        {
            StopCoroutine(currentCoroutine);
        }

        currentCoroutine = StartCoroutine(ShowNotificationCoroutine(message, duration));
    }

    private IEnumerator ShowNotificationCoroutine(string message, float duration)
    {
        // Configurar el mensaje
        if (notificationText != null)
        {
            notificationText.text = message;
        }

        // Fade in
        yield return StartCoroutine(FadeCoroutine(0f, 1f, fadeInDuration));

        // Esperar la duración
        yield return new WaitForSeconds(duration);

        // Fade out
        yield return StartCoroutine(FadeCoroutine(1f, 0f, fadeOutDuration));
    }

    private IEnumerator FadeCoroutine(float startAlpha, float targetAlpha, float duration)
    {
        float currentTime = 0f;
        canvasGroup.alpha = startAlpha;

        while (currentTime < duration)
        {
            currentTime += Time.deltaTime;
            float normalizedTime = currentTime / duration;
            float curveValue = fadeCurve.Evaluate(normalizedTime);
            canvasGroup.alpha = Mathf.Lerp(startAlpha, targetAlpha, curveValue);
            yield return null;
        }

        canvasGroup.alpha = targetAlpha;
    }

    public void SetNotificationType(NotificationType type)
    {
        if (background != null)
        {
            switch (type)
            {
                case NotificationType.Info:
                    background.color = new Color(0.2f, 0.6f, 1f, 0.9f);
                    break;
                case NotificationType.Success:
                    background.color = new Color(0.2f, 0.8f, 0.2f, 0.9f);
                    break;
                case NotificationType.Warning:
                    background.color = new Color(1f, 0.8f, 0.2f, 0.9f);
                    break;
                case NotificationType.Error:
                    background.color = new Color(0.8f, 0.2f, 0.2f, 0.9f);
                    break;
            }
        }
    }
}

public enum NotificationType
{
    Info,
    Success,
    Warning,
    Error
} 