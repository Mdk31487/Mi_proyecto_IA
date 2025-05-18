using UnityEngine;
using System;

public abstract class StatusEffect : MonoBehaviour
{
    public string effectName;
    public float duration;
    public float tickRate;
    public Sprite icon;
    public string description;

    protected float remainingDuration;
    protected float nextTickTime;
    protected bool isActive;

    public event Action<StatusEffect> OnEffectRemoved;

    protected virtual void Start()
    {
        remainingDuration = duration;
        nextTickTime = Time.time + tickRate;
        isActive = true;
    }

    protected virtual void Update()
    {
        if (!isActive) return;

        remainingDuration -= Time.deltaTime;

        if (Time.time >= nextTickTime)
        {
            ApplyEffect();
            nextTickTime = Time.time + tickRate;
        }

        if (remainingDuration <= 0)
        {
            RemoveEffect();
        }
    }

    protected abstract void ApplyEffect();

    public virtual void RemoveEffect()
    {
        isActive = false;
        OnEffectRemoved?.Invoke(this);
        Destroy(this);
    }

    public void RefreshDuration()
    {
        remainingDuration = duration;
    }
} 