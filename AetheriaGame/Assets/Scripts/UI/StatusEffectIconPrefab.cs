using UnityEngine;
using UnityEngine.UI;

[RequireComponent(typeof(Image))]
[RequireComponent(typeof(TooltipTrigger))]
public class StatusEffectIconPrefab : MonoBehaviour
{
    private Image iconImage;
    private TooltipTrigger tooltipTrigger;
    private StatusEffectIcon statusEffectIcon;

    private void Awake()
    {
        // Obtener componentes
        iconImage = GetComponent<Image>();
        tooltipTrigger = GetComponent<TooltipTrigger>();
        statusEffectIcon = GetComponent<StatusEffectIcon>();

        // Configurar el RectTransform
        RectTransform rectTransform = GetComponent<RectTransform>();
        rectTransform.sizeDelta = new Vector2(40, 40);

        // Configurar el Image
        iconImage.raycastTarget = true;
        iconImage.preserveAspect = true;

        // Configurar el StatusEffectIcon
        if (statusEffectIcon != null)
        {
            statusEffectIcon.iconImage = iconImage;
            statusEffectIcon.tooltipTrigger = tooltipTrigger;
        }
    }

    public void Setup(StatusEffect effect)
    {
        if (statusEffectIcon != null)
        {
            statusEffectIcon.Initialize(effect);
        }
    }
} 