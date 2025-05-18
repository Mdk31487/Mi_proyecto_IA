using UnityEngine;

public class StunnedEffect : StatusEffect
{
    public StunnedEffect()
    {
        id = "stunned";
        effectName = "Stunned";
        duration = 2f;
        isPermanent = false;
        isStackable = false;
    }

    public override void OnApply(GameObject target)
    {
        // Disable movement and actions
        if (target.TryGetComponent<PlayerController>(out PlayerController controller))
        {
            controller.SetStunned(true);
        }
        Debug.Log($"{target.name} is now stunned!");
    }

    public override void OnRemove(GameObject target)
    {
        // Re-enable movement and actions
        if (target.TryGetComponent<PlayerController>(out PlayerController controller))
        {
            controller.SetStunned(false);
        }
        Debug.Log($"{target.name} is no longer stunned!");
    }

    public override void OnTick(GameObject target)
    {
        // Stun doesn't need tick behavior
    }
} 