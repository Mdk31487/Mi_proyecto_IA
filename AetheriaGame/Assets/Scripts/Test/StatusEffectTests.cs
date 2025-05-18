using UnityEngine;
using UnityEngine.TestTools;
using NUnit.Framework;
using System.Collections;

public class StatusEffectTests
{
    private GameObject testObject;
    private StatusEffectSystem statusEffectSystem;
    private Health health;

    [SetUp]
    public void Setup()
    {
        testObject = new GameObject("TestObject");
        statusEffectSystem = testObject.AddComponent<StatusEffectSystem>();
        health = testObject.AddComponent<Health>();
        health.maxHealth = 100f;
        health.currentHealth = health.maxHealth;
    }

    [TearDown]
    public void TearDown()
    {
        Object.Destroy(testObject);
    }

    [Test]
    public void BurnEffect_AppliesDamageOverTime()
    {
        // Arrange
        float initialHealth = health.currentHealth;
        BurnEffect burnEffect = new BurnEffect
        {
            damagePerTick = 5f,
            tickRate = 1f,
            duration = 3f
        };

        // Act
        statusEffectSystem.ApplyEffect(burnEffect);
        float timePassed = 0f;
        while (timePassed < 3f)
        {
            timePassed += Time.deltaTime;
            statusEffectSystem.Update();
        }

        // Assert
        Assert.Less(health.currentHealth, initialHealth);
    }

    [Test]
    public void StunEffect_PreventsMovement()
    {
        // Arrange
        PlayerController playerController = testObject.AddComponent<PlayerController>();
        StunEffect stunEffect = new StunEffect
        {
            duration = 2f
        };

        // Act
        statusEffectSystem.ApplyEffect(stunEffect);
        Vector3 initialPosition = testObject.transform.position;
        playerController.Move(Vector3.right);

        // Assert
        Assert.AreEqual(initialPosition, testObject.transform.position);
    }

    [Test]
    public void MultipleEffects_StackCorrectly()
    {
        // Arrange
        BurnEffect burnEffect1 = new BurnEffect { duration = 2f };
        BurnEffect burnEffect2 = new BurnEffect { duration = 2f };

        // Act
        statusEffectSystem.ApplyEffect(burnEffect1);
        statusEffectSystem.ApplyEffect(burnEffect2);

        // Assert
        Assert.AreEqual(2, statusEffectSystem.ActiveEffects.Count);
    }

    [Test]
    public void EffectRemoval_WorksCorrectly()
    {
        // Arrange
        BurnEffect burnEffect = new BurnEffect { duration = 1f };

        // Act
        statusEffectSystem.ApplyEffect(burnEffect);
        float timePassed = 0f;
        while (timePassed < 1.1f)
        {
            timePassed += Time.deltaTime;
            statusEffectSystem.Update();
        }

        // Assert
        Assert.AreEqual(0, statusEffectSystem.ActiveEffects.Count);
    }
} 