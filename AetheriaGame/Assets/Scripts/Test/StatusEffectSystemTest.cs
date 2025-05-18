using UnityEngine;
using UnityEngine.UI;

public class StatusEffectSystemTest : MonoBehaviour
{
    public Button testBurnButton;
    public Button testStunButton;
    public StatusEffectPanel statusEffectPanel;
    public GameObject player;

    private void Start()
    {
        testBurnButton.onClick.AddListener(TestBurnEffect);
        testStunButton.onClick.AddListener(TestStunEffect);
    }

    private void TestBurnEffect()
    {
        BurnEffect burnEffect = player.AddComponent<BurnEffect>();
        burnEffect.effectName = "Quemadura";
        burnEffect.description = "Inflige daño por tiempo";
        burnEffect.duration = 5f;
        burnEffect.tickRate = 1f;
        burnEffect.damagePerTick = 5f;
        statusEffectPanel.AddStatusEffect(burnEffect);
    }

    private void TestStunEffect()
    {
        StunEffect stunEffect = player.AddComponent<StunEffect>();
        stunEffect.effectName = "Aturdimiento";
        stunEffect.description = "No puedes moverte";
        stunEffect.duration = 3f;
        stunEffect.tickRate = 1f;
        statusEffectPanel.AddStatusEffect(stunEffect);
    }
} 