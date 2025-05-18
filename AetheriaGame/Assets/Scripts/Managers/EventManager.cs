using UnityEngine;
using System;
using System.Collections.Generic;

public class EventManager : MonoBehaviour
{
    public static EventManager Instance { get; private set; }

    private Dictionary<string, List<Action<object>>> eventDictionary;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            eventDictionary = new Dictionary<string, List<Action<object>>>();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    public void StartListening(string eventName, Action<object> listener)
    {
        if (!eventDictionary.ContainsKey(eventName))
        {
            eventDictionary[eventName] = new List<Action<object>>();
        }

        if (!eventDictionary[eventName].Contains(listener))
        {
            eventDictionary[eventName].Add(listener);
        }
    }

    public void StopListening(string eventName, Action<object> listener)
    {
        if (eventDictionary.ContainsKey(eventName))
        {
            eventDictionary[eventName].Remove(listener);
        }
    }

    public void TriggerEvent(string eventName, object data = null)
    {
        if (eventDictionary.ContainsKey(eventName))
        {
            foreach (Action<object> listener in eventDictionary[eventName])
            {
                try
                {
                    listener.Invoke(data);
                }
                catch (Exception e)
                {
                    Debug.LogError($"Error al ejecutar evento {eventName}: {e.Message}");
                }
            }
        }
    }

    // Eventos predefinidos
    public static class Events
    {
        // Eventos del jugador
        public const string PLAYER_DAMAGED = "PLAYER_DAMAGED";
        public const string PLAYER_HEALED = "PLAYER_HEALED";
        public const string PLAYER_DIED = "PLAYER_DIED";
        public const string PLAYER_LEVEL_UP = "PLAYER_LEVEL_UP";

        // Eventos de efectos de estado
        public const string STATUS_EFFECT_APPLIED = "STATUS_EFFECT_APPLIED";
        public const string STATUS_EFFECT_REMOVED = "STATUS_EFFECT_REMOVED";
        public const string STATUS_EFFECT_TICK = "STATUS_EFFECT_TICK";

        // Eventos de UI
        public const string UI_DIALOGUE_STARTED = "UI_DIALOGUE_STARTED";
        public const string UI_DIALOGUE_ENDED = "UI_DIALOGUE_ENDED";
        public const string UI_NOTIFICATION_SHOWN = "UI_NOTIFICATION_SHOWN";

        // Eventos de escena
        public const string SCENE_LOADING = "SCENE_LOADING";
        public const string SCENE_LOADED = "SCENE_LOADED";

        // Eventos de guardado
        public const string GAME_SAVED = "GAME_SAVED";
        public const string GAME_LOADED = "GAME_LOADED";

        // Eventos de combate
        public const string COMBAT_STARTED = "COMBAT_STARTED";
        public const string COMBAT_ENDED = "COMBAT_ENDED";
        public const string ENEMY_DEFEATED = "ENEMY_DEFEATED";
    }

    // Ejemplo de uso:
    /*
    void Start()
    {
        EventManager.Instance.StartListening(EventManager.Events.PLAYER_DAMAGED, OnPlayerDamaged);
    }

    void OnDestroy()
    {
        EventManager.Instance.StopListening(EventManager.Events.PLAYER_DAMAGED, OnPlayerDamaged);
    }

    void OnPlayerDamaged(object data)
    {
        float damage = (float)data;
        // Manejar el daño
    }
    */
} 