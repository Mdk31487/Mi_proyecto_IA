using UnityEngine;

public class StatusEffectSetup : MonoBehaviour
{
    [Header("Sprites")]
    public Sprite burnIcon;
    public Sprite stunIcon;

    [Header("Settings")]
    public float burnDamagePerTick = 5f;
    public float burnDuration = 5f;
    public float stunDuration = 3f;

    public void SetupBurnEffect(BurnEffect effect)
    {
        if (effect != null)
        {
            effect.effectName = "Quemadura";
            effect.description = "Inflige daño por tiempo";
            effect.duration = burnDuration;
            effect.tickRate = 1f;
            effect.damagePerTick = burnDamagePerTick;
            effect.icon = burnIcon;
        }
    }

    public void SetupStunEffect(StunEffect effect)
    {
        if (effect != null)
        {
            effect.effectName = "Aturdimiento";
            effect.description = "No puedes moverte";
            effect.duration = stunDuration;
            effect.tickRate = 1f;
            effect.icon = stunIcon;
        }
    }
} 