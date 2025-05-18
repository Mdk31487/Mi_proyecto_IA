using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;

public class StatusEffectPanel : MonoBehaviour
{
    public GameObject statusEffectIconPrefab;
    public Transform iconContainer;
    public float iconSpacing = 10f;

    private Dictionary<StatusEffect, GameObject> activeEffects = new Dictionary<StatusEffect, GameObject>();

    public void AddStatusEffect(StatusEffect effect)
    {
        if (activeEffects.ContainsKey(effect)) return;

        GameObject iconObj = Instantiate(statusEffectIconPrefab, iconContainer);
        Image iconImage = iconObj.GetComponent<Image>();
        iconImage.sprite = effect.icon;

        // Add tooltip
        TooltipTrigger tooltip = iconObj.GetComponent<TooltipTrigger>();
        if (tooltip != null)
        {
            tooltip.header = effect.effectName;
            tooltip.content = effect.description;
        }

        activeEffects.Add(effect, iconObj);
        effect.OnEffectRemoved += RemoveStatusEffect;
        UpdateIconPositions();
    }

    public void RemoveStatusEffect(StatusEffect effect)
    {
        if (activeEffects.TryGetValue(effect, out GameObject iconObj))
        {
            Destroy(iconObj);
            activeEffects.Remove(effect);
            UpdateIconPositions();
        }
    }

    private void UpdateIconPositions()
    {
        float currentX = 0;
        foreach (var iconObj in activeEffects.Values)
        {
            RectTransform rectTransform = iconObj.GetComponent<RectTransform>();
            rectTransform.anchoredPosition = new Vector2(currentX, 0);
            currentX += rectTransform.rect.width + iconSpacing;
        }
    }
} 