using UnityEngine;

public class BurnEffect : StatusEffect
{
    public float damagePerTick = 5f;

    protected override void ApplyEffect()
    {
        Health health = GetComponent<Health>();
        if (health != null)
        {
            health.TakeDamage(damagePerTick);
        }
    }
} 