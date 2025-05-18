using UnityEngine;

public class StunEffect : StatusEffect
{
    private PlayerController playerController;

    protected override void Start()
    {
        base.Start();
        playerController = GetComponent<PlayerController>();
        if (playerController != null)
        {
            playerController.SetStunned(true);
        }
    }

    protected override void ApplyEffect()
    {
        // Stun effect doesn't need to do anything on tick
    }

    public override void RemoveEffect()
    {
        if (playerController != null)
        {
            playerController.SetStunned(false);
        }
        base.RemoveEffect();
    }
} 