using UnityEngine;

public class UIManager : MonoBehaviour
{
    public static UIManager Instance { get; private set; }

    [Header("UI Panels")]
    [SerializeField] private StatusEffectPanel statusEffectPanel;
    [SerializeField] private GameObject pauseMenu;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }
        else
        {
            Destroy(gameObject);
        }
    }

    public void AddStatusEffect(string effectId, Sprite icon, string effectName, float duration)
    {
        if (statusEffectPanel != null)
        {
            statusEffectPanel.AddEffect(effectId, icon, effectName, duration);
        }
        else
        {
            Debug.LogWarning("Status Effect Panel not assigned to UIManager!");
        }
    }

    public void RemoveStatusEffect(string effectId)
    {
        if (statusEffectPanel != null)
        {
            statusEffectPanel.RemoveEffect(effectId);
        }
    }

    public void ShowPauseMenu()
    {
        if (pauseMenu != null)
        {
            pauseMenu.SetActive(true);
        }
    }

    public void HidePauseMenu()
    {
        if (pauseMenu != null)
        {
            pauseMenu.SetActive(false);
        }
    }
} 