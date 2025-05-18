using UnityEngine;
using UnityEngine.UI;

public class MobileControlsUI : MonoBehaviour
{
    [Header("Joystick")]
    public RectTransform joystickBackground;
    public RectTransform joystickHandle;
    public Joystick joystick;

    [Header("Action Buttons")]
    public RectTransform jumpButton;
    public RectTransform interactButton;
    public RectTransform attackButton;
    public RectTransform inventoryButton;

    [Header("Settings")]
    public float minButtonSize = 50f;
    public float maxButtonSize = 200f;
    public float defaultButtonSize = 100f;
    public float defaultJoystickSize = 150f;

    private void Start()
    {
        if (ConfigManager.Instance != null)
        {
            // Aplicar configuración guardada
            ApplySavedSettings();
        }
    }

    private void ApplySavedSettings()
    {
        // Ajustar tamaño del joystick
        float joystickSize = ConfigManager.Instance.CurrentConfig.joystickSize * defaultJoystickSize;
        joystickBackground.sizeDelta = new Vector2(joystickSize, joystickSize);
        joystickHandle.sizeDelta = new Vector2(joystickSize * 0.5f, joystickSize * 0.5f);

        // Ajustar tamaño de botones
        float buttonSize = ConfigManager.Instance.CurrentConfig.buttonSize * defaultButtonSize;
        buttonSize = Mathf.Clamp(buttonSize, minButtonSize, maxButtonSize);

        if (jumpButton != null) jumpButton.sizeDelta = new Vector2(buttonSize, buttonSize);
        if (interactButton != null) interactButton.sizeDelta = new Vector2(buttonSize, buttonSize);
        if (attackButton != null) attackButton.sizeDelta = new Vector2(buttonSize, buttonSize);
        if (inventoryButton != null) inventoryButton.sizeDelta = new Vector2(buttonSize, buttonSize);

        // Ajustar opacidad
        float opacity = ConfigManager.Instance.CurrentConfig.buttonOpacity;
        SetButtonsOpacity(opacity);
    }

    private void SetButtonsOpacity(float opacity)
    {
        Image[] buttonImages = GetComponentsInChildren<Image>();
        foreach (Image image in buttonImages)
        {
            Color color = image.color;
            color.a = opacity;
            image.color = color;
        }
    }

    public void UpdateButtonSizes(float size)
    {
        size = Mathf.Clamp(size, minButtonSize, maxButtonSize);
        
        if (jumpButton != null) jumpButton.sizeDelta = new Vector2(size, size);
        if (interactButton != null) interactButton.sizeDelta = new Vector2(size, size);
        if (attackButton != null) attackButton.sizeDelta = new Vector2(size, size);
        if (inventoryButton != null) inventoryButton.sizeDelta = new Vector2(size, size);
    }

    public void UpdateJoystickSize(float size)
    {
        float joystickSize = size * defaultJoystickSize;
        joystickBackground.sizeDelta = new Vector2(joystickSize, joystickSize);
        joystickHandle.sizeDelta = new Vector2(joystickSize * 0.5f, joystickSize * 0.5f);
    }

    public void UpdateOpacity(float opacity)
    {
        SetButtonsOpacity(opacity);
    }
} 