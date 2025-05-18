using UnityEngine;

public class BurningEffect : StatusEffect
{
    public float damagePerTick = 5f;

    public BurningEffect()
    {
        id = "burning";
        effectName = "Burning";
        duration = 5f;
        isPermanent = false;
        isStackable = true;
        maxStacks = 3;
    }

    public override void OnApply(GameObject target)
    {
        // Add visual effects
        Debug.Log($"{target.name} is now burning!");
    }

    public override void OnRemove(GameObject target)
    {
        // Remove visual effects
        Debug.Log($"{target.name} is no longer burning!");
    }

    public override void OnTick(GameObject target)
    {
        // Apply damage
        if (target.TryGetComponent<Health>(out Health health))
        {
            float totalDamage = damagePerTick * currentStacks;
            health.TakeDamage(totalDamage);
            Debug.Log($"{target.name} took {totalDamage} burning damage!");
        }
    }

    public override void OnStack(GameObject target)
    {
        Debug.Log($"{target.name}'s burning effect increased to {currentStacks} stacks!");
    }
} 