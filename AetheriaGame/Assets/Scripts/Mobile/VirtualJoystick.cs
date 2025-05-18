using UnityEngine;
using UnityEngine.EventSystems;
using UnityEngine.UI;

public class VirtualJoystick : MonoBehaviour, IPointerDownHandler, IPointerUpHandler, IDragHandler
{
    [Header("Joystick Settings")]
    public RectTransform background;
    public RectTransform handle;
    public float deadzone = 0.1f;
    public float maxDistance = 100f;

    [Header("Visual Settings")]
    public Color normalColor = new Color(1f, 1f, 1f, 0.5f);
    public Color activeColor = new Color(1f, 1f, 1f, 0.8f);

    private Vector2 joystickCenter;
    private Vector2 joystickPosition;
    private bool isDragging;
    private Image backgroundImage;
    private Image handleImage;

    private void Awake()
    {
        backgroundImage = background.GetComponent<Image>();
        handleImage = handle.GetComponent<Image>();
        ResetJoystick();
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        isDragging = true;
        joystickCenter = eventData.position;
        background.position = joystickCenter;
        handle.position = joystickCenter;
        backgroundImage.color = activeColor;
        handleImage.color = activeColor;
    }

    public void OnPointerUp(PointerEventData eventData)
    {
        isDragging = false;
        ResetJoystick();
    }

    public void OnDrag(PointerEventData eventData)
    {
        if (!isDragging) return;

        Vector2 direction = eventData.position - joystickCenter;
        float distance = direction.magnitude;

        if (distance > deadzone)
        {
            if (distance > maxDistance)
            {
                direction = direction.normalized * maxDistance;
            }
            handle.position = joystickCenter + direction;
        }
        else
        {
            handle.position = joystickCenter;
        }
    }

    private void ResetJoystick()
    {
        joystickPosition = Vector2.zero;
        backgroundImage.color = normalColor;
        handleImage.color = normalColor;
        handle.position = background.position;
    }

    public Vector2 GetDirection()
    {
        if (!isDragging) return Vector2.zero;

        Vector2 direction = handle.position - background.position;
        float distance = direction.magnitude;

        if (distance > deadzone)
        {
            return direction.normalized * (distance / maxDistance);
        }

        return Vector2.zero;
    }

    public bool IsActive()
    {
        return isDragging;
    }

    public void SetOpacity(float opacity)
    {
        Color bgColor = backgroundImage.color;
        Color hColor = handleImage.color;
        
        bgColor.a = opacity;
        hColor.a = opacity;
        
        backgroundImage.color = bgColor;
        handleImage.color = hColor;
    }

    public void SetSize(float size)
    {
        background.sizeDelta = new Vector2(size, size);
        handle.sizeDelta = new Vector2(size * 0.5f, size * 0.5f);
        maxDistance = size * 0.4f;
    }
} 