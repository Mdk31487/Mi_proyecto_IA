using UnityEngine;
using System.Collections.Generic;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    // Estado del juego
    public enum GameState
    {
        MainMenu,
        Playing,
        Paused,
        Training,
        Dialogue,
        Loading
    }

    public GameState CurrentState { get; private set; }

    // Datos del jugador
    [System.Serializable]
    public class PlayerData
    {
        public string playerName;
        public int currentZone;
        public float experience;
        public Dictionary<string, float> skills;
        public List<string> completedMissions;
    }

    public PlayerData playerData;

    // Eventos
    public delegate void GameStateChangeHandler(GameState newState);
    public event GameStateChangeHandler OnGameStateChanged;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            InitializeGame();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void InitializeGame()
    {
        playerData = new PlayerData
        {
            playerName = "Player",
            currentZone = 0,
            experience = 0f,
            skills = new Dictionary<string, float>(),
            completedMissions = new List<string>()
        };

        CurrentState = GameState.MainMenu;
    }

    public void ChangeGameState(GameState newState)
    {
        CurrentState = newState;
        OnGameStateChanged?.Invoke(newState);

        switch (newState)
        {
            case GameState.Paused:
                Time.timeScale = 0f;
                break;
            case GameState.Playing:
                Time.timeScale = 1f;
                break;
            case GameState.Training:
                Time.timeScale = 0.5f;
                break;
        }
    }

    public void SaveGame()
    {
        string json = JsonUtility.ToJson(playerData);
        PlayerPrefs.SetString("PlayerData", json);
        PlayerPrefs.Save();
    }

    public void LoadGame()
    {
        if (PlayerPrefs.HasKey("PlayerData"))
        {
            string json = PlayerPrefs.GetString("PlayerData");
            playerData = JsonUtility.FromJson<PlayerData>(json);
        }
    }

    public void UpdatePlayerSkill(string skillName, float value)
    {
        if (playerData.skills.ContainsKey(skillName))
        {
            playerData.skills[skillName] = value;
        }
        else
        {
            playerData.skills.Add(skillName, value);
        }
    }

    public void AddCompletedMission(string missionId)
    {
        if (!playerData.completedMissions.Contains(missionId))
        {
            playerData.completedMissions.Add(missionId);
            SaveGame();
        }
    }
} 