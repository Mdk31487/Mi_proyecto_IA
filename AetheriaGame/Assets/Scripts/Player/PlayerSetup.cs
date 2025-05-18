using UnityEngine;

public class PlayerSetup : MonoBehaviour
{
    [Header("References")]
    public PlayerController playerController;
    public Health health;
    public Transform groundCheck;

    [Header("Settings")]
    public LayerMask groundMask;

    private void Start()
    {
        SetupPlayerController();
        SetupHealth();
    }

    private void SetupPlayerController()
    {
        if (playerController != null)
        {
            playerController.groundCheck = groundCheck;
            playerController.groundMask = groundMask;
        }
    }

    private void SetupHealth()
    {
        if (health != null)
        {
            health.maxHealth = 100f;
            health.currentHealth = health.maxHealth;
        }
    }
} 