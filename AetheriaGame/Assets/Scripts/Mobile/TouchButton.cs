using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;
using System;

public class TouchButton : MonoBehaviour, IPointerDownHandler, IPointerUpHandler, IPointerEnterHandler, IPointerExitHandler
{
    [Header("Button Settings")]
    public bool isToggle = false;
    public float holdTime = 0.5f;
    public float repeatRate = 0.1f;

    [Header("Visual Settings")]
    public Color normalColor = new Color(1f, 1f, 1f, 0.7f);
    public Color pressedColor = new Color(1f, 1f, 1f, 1f);
    public Color disabledColor = new Color(0.5f, 0.5f, 0.5f, 0.5f);

    [Header("Events")]
    public event Action OnButtonDown;
    public event Action OnButtonUp;
    public event Action OnButtonHold;
    public event Action OnButtonRepeat;

    private bool isPressed;
    private bool isHolding;
    private float holdTimer;
    private float repeatTimer;
    private Image buttonImage;
    private bool isEnabled = true;

    private void Awake()
    {
        buttonImage = GetComponent<Image>();
        if (buttonImage == null)
        {
            buttonImage = gameObject.AddComponent<Image>();
        }
        SetNormalState();
    }

    private void Update()
    {
        if (isPressed && isEnabled)
        {
            holdTimer += Time.deltaTime;
            
            if (holdTimer >= holdTime && !isHolding)
            {
                isHolding = true;
                OnButtonHold?.Invoke();
            }

            if (isHolding)
            {
                repeatTimer += Time.deltaTime;
                if (repeatTimer >= repeatRate)
                {
                    repeatTimer = 0f;
                    OnButtonRepeat?.Invoke();
                }
            }
        }
    }

    public void OnPointerDown(PointerEventData eventData)
    {
        if (!isEnabled) return;

        isPressed = true;
        holdTimer = 0f;
        repeatTimer = 0f;
        isHolding = false;
        
        if (!isToggle)
        {
            SetPressedState();
        }
        
        OnButtonDown?.Invoke();
    }

    public void OnPointerUp(PointerEventData eventData)
    {
        if (!isEnabled) return;

        if (isToggle)
        {
            isPressed = !isPressed;
            if (isPressed)
            {
                SetPressedState();
            }
            else
            {
                SetNormalState();
            }
        }
        else
        {
            isPressed = false;
            SetNormalState();
        }

        isHolding = false;
        OnButtonUp?.Invoke();
    }

    public void OnPointerEnter(PointerEventData eventData)
    {
        if (!isEnabled) return;
        
        if (!isPressed && !isToggle)
        {
            SetHoverState();
        }
    }

    public void OnPointerExit(PointerEventData eventData)
    {
        if (!isEnabled) return;
        
        if (!isPressed && !isToggle)
        {
            SetNormalState();
        }
    }

    private void SetNormalState()
    {
        if (buttonImage != null)
        {
            buttonImage.color = normalColor;
        }
    }

    private void SetPressedState()
    {
        if (buttonImage != null)
        {
            buttonImage.color = pressedColor;
        }
    }

    private void SetHoverState()
    {
        if (buttonImage != null)
        {
            Color hoverColor = normalColor;
            hoverColor.a += 0.1f;
            buttonImage.color = hoverColor;
        }
    }

    private void SetDisabledState()
    {
        if (buttonImage != null)
        {
            buttonImage.color = disabledColor;
        }
    }

    public void SetEnabled(bool enabled)
    {
        isEnabled = enabled;
        if (enabled)
        {
            SetNormalState();
        }
        else
        {
            SetDisabledState();
        }
    }

    public void SetOpacity(float opacity)
    {
        Color color = buttonImage.color;
        color.a = opacity;
        buttonImage.color = color;
    }

    public void SetSize(float size)
    {
        RectTransform rectTransform = GetComponent<RectTransform>();
        if (rectTransform != null)
        {
            rectTransform.sizeDelta = new Vector2(size, size);
        }
    }

    public bool IsPressed()
    {
        return isPressed;
    }

    public bool IsHolding()
    {
        return isHolding;
    }
} 