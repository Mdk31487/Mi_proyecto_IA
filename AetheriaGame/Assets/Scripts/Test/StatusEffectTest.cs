using UnityEngine;
using UnityEngine.UI;

public class StatusEffectTest : MonoBehaviour
{
    [Header("Test Settings")]
    [SerializeField] private StatusEffectPanel statusEffectPanel;
    [SerializeField] private Sprite[] testIcons;
    [SerializeField] private string[] testEffectNames;
    [SerializeField] private float[] testDurations;
    [SerializeField] private float testInterval = 2f;

    private float timer;
    private int currentIndex;

    private void Update()
    {
        timer += Time.deltaTime;
        if (timer >= testInterval)
        {
            timer = 0f;
            AddTestEffect();
        }
    }

    private void AddTestEffect()
    {
        if (testIcons == null || testIcons.Length == 0 ||
            testEffectNames == null || testEffectNames.Length == 0 ||
            testDurations == null || testDurations.Length == 0)
        {
            Debug.LogError("Test arrays not properly configured!");
            return;
        }

        int iconIndex = currentIndex % testIcons.Length;
        int nameIndex = currentIndex % testEffectNames.Length;
        int durationIndex = currentIndex % testDurations.Length;

        string effectId = $"test_effect_{currentIndex}";
        statusEffectPanel.AddEffect(
            effectId,
            testIcons[iconIndex],
            testEffectNames[nameIndex],
            testDurations[durationIndex]
        );

        currentIndex++;
    }
} 