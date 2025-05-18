using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class HUD : MonoBehaviour
{
    [Header("Health Bar")]
    public Slider healthBar;
    public TextMeshProUGUI healthText;
    public Image healthBarFill;

    [Header("Experience Bar")]
    public Slider experienceBar;
    public TextMeshProUGUI levelText;
    public TextMeshProUGUI experienceText;

    [Header("Minimap")]
    public RawImage minimapImage;
    public Camera minimapCamera;
    public float minimapZoom = 20f;

    [Header("Status Effects")]
    public Transform statusEffectsContainer;
    public GameObject statusEffectPrefab;

    private UIManager uiManager;
    private AudioManager audioManager;
    private float currentHealth;
    private float maxHealth;
    private float currentExperience;
    private float maxExperience;
    private int currentLevel;

    private void Start()
    {
        uiManager = GetComponent<UIManager>();
        audioManager = GetComponent<AudioManager>();

        SetupHealthBar();
        SetupExperienceBar();
        SetupMinimap();
    }

    private void SetupHealthBar()
    {
        if (healthBar != null)
        {
            healthBar.minValue = 0f;
            healthBar.maxValue = 100f;
            healthBar.value = 100f;
            currentHealth = 100f;
            maxHealth = 100f;
            UpdateHealthText();
        }
    }

    private void SetupExperienceBar()
    {
        if (experienceBar != null)
        {
            experienceBar.minValue = 0f;
            experienceBar.maxValue = 100f;
            experienceBar.value = 0f;
            currentExperience = 0f;
            maxExperience = 100f;
            currentLevel = 1;
            UpdateExperienceText();
        }
    }

    private void SetupMinimap()
    {
        if (minimapCamera != null)
        {
            minimapCamera.orthographicSize = minimapZoom;
        }
    }

    public void UpdateHealth(float current, float max)
    {
        currentHealth = current;
        maxHealth = max;

        if (healthBar != null)
        {
            healthBar.maxValue = max;
            healthBar.value = current;
            UpdateHealthText();
        }

        // Cambiar color de la barra según la salud
        if (healthBarFill != null)
        {
            float healthPercentage = current / max;
            if (healthPercentage > 0.6f)
            {
                healthBarFill.color = Color.green;
            }
            else if (healthPercentage > 0.3f)
            {
                healthBarFill.color = Color.yellow;
            }
            else
            {
                healthBarFill.color = Color.red;
            }
        }
    }

    public void UpdateExperience(float current, float max, int level)
    {
        currentExperience = current;
        maxExperience = max;
        currentLevel = level;

        if (experienceBar != null)
        {
            experienceBar.maxValue = max;
            experienceBar.value = current;
            UpdateExperienceText();
        }
    }

    private void UpdateHealthText()
    {
        if (healthText != null)
        {
            healthText.text = $"{Mathf.Ceil(currentHealth)}/{maxHealth}";
        }
    }

    private void UpdateExperienceText()
    {
        if (experienceText != null)
        {
            experienceText.text = $"{Mathf.Ceil(currentExperience)}/{maxExperience}";
        }

        if (levelText != null)
        {
            levelText.text = $"Nivel {currentLevel}";
        }
    }

    public void AddStatusEffect(string effectName, Sprite effectIcon, float duration)
    {
        if (statusEffectsContainer != null && statusEffectPrefab != null)
        {
            GameObject statusEffect = Instantiate(statusEffectPrefab, statusEffectsContainer);
            StatusEffectUI effectUI = statusEffect.GetComponent<StatusEffectUI>();
            if (effectUI != null)
            {
                effectUI.Initialize(effectName, effectIcon, duration);
            }
        }
    }

    public void UpdateMinimapZoom(float zoom)
    {
        minimapZoom = zoom;
        if (minimapCamera != null)
        {
            minimapCamera.orthographicSize = zoom;
        }
    }

    public void ShowNotification(string message, float duration = 2f)
    {
        if (uiManager != null)
        {
            uiManager.ShowNotification(message, duration);
        }
    }
} 