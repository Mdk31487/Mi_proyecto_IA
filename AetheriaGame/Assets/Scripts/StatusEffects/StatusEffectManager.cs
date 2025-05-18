using UnityEngine;
using System.Collections.Generic;
using System.Linq;

public class StatusEffectManager : MonoBehaviour
{
    private Dictionary<string, StatusEffect> activeEffects = new Dictionary<string, StatusEffect>();
    private float tickInterval = 1f;
    private float tickTimer;

    private void Update()
    {
        tickTimer += Time.deltaTime;
        if (tickTimer >= tickInterval)
        {
            tickTimer = 0f;
            TickEffects();
        }
    }

    public void ApplyEffect(StatusEffect effect, GameObject target)
    {
        if (activeEffects.ContainsKey(effect.id))
        {
            StatusEffect existingEffect = activeEffects[effect.id];
            if (existingEffect.CanStack())
            {
                existingEffect.AddStack();
                existingEffect.OnStack(target);
                UIManager.Instance.AddStatusEffect(effect.id, effect.icon, effect.effectName, effect.duration);
            }
        }
        else
        {
            effect.OnApply(target);
            activeEffects.Add(effect.id, effect);
            UIManager.Instance.AddStatusEffect(effect.id, effect.icon, effect.effectName, effect.duration);
        }
    }

    public void RemoveEffect(string effectId, GameObject target)
    {
        if (activeEffects.TryGetValue(effectId, out StatusEffect effect))
        {
            effect.OnRemove(target);
            activeEffects.Remove(effectId);
            UIManager.Instance.RemoveStatusEffect(effectId);
        }
    }

    private void TickEffects()
    {
        List<string> effectsToRemove = new List<string>();

        foreach (var kvp in activeEffects)
        {
            StatusEffect effect = kvp.Value;
            if (!effect.isPermanent)
            {
                effect.duration -= tickInterval;
                if (effect.duration <= 0)
                {
                    effectsToRemove.Add(kvp.Key);
                }
            }
            effect.OnTick(gameObject);
        }

        foreach (string effectId in effectsToRemove)
        {
            RemoveEffect(effectId, gameObject);
        }
    }

    public bool HasEffect(string effectId)
    {
        return activeEffects.ContainsKey(effectId);
    }

    public StatusEffect GetEffect(string effectId)
    {
        return activeEffects.TryGetValue(effectId, out StatusEffect effect) ? effect : null;
    }

    public List<StatusEffect> GetAllEffects()
    {
        return activeEffects.Values.ToList();
    }
} 