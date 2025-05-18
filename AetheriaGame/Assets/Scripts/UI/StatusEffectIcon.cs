using UnityEngine;
using UnityEngine.UI;

public class StatusEffectIcon : MonoBehaviour
{
    public Image iconImage;
    public TooltipTrigger tooltipTrigger;
    public StatusEffect effect;

    public void Initialize(StatusEffect statusEffect)
    {
        effect = statusEffect;
        iconImage.sprite = statusEffect.icon;
        tooltipTrigger.header = statusEffect.effectName;
        tooltipTrigger.content = statusEffect.description;
    }
} 