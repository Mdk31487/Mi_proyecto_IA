using UnityEngine;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System;

public class SaveSystem : MonoBehaviour
{
    public static SaveSystem Instance { get; private set; }

    private string SavePath => Path.Combine(Application.persistentDataPath, "savedata.dat");

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

    [Serializable]
    public class GameData
    {
        public float playerHealth;
        public Vector3 playerPosition;
        public int currentScene;
        public float playTime;
        public bool[] unlockedAchievements;
        public int[] inventoryItems;
        public float[] statusEffectDurations;
    }

    public void SaveGame()
    {
        try
        {
            GameData data = new GameData
            {
                playerHealth = FindObjectOfType<Health>().currentHealth,
                playerPosition = FindObjectOfType<PlayerController>().transform.position,
                currentScene = UnityEngine.SceneManagement.SceneManager.GetActiveScene().buildIndex,
                playTime = Time.time,
                unlockedAchievements = GetAchievementData(),
                inventoryItems = GetInventoryData(),
                statusEffectDurations = GetStatusEffectData()
            };

            BinaryFormatter formatter = new BinaryFormatter();
            using (FileStream stream = new FileStream(SavePath, FileMode.Create))
            {
                formatter.Serialize(stream, data);
            }

            EventManager.Instance.TriggerEvent(EventManager.Events.GAME_SAVED);
            Debug.Log("Juego guardado exitosamente");
        }
        catch (Exception e)
        {
            Debug.LogError($"Error al guardar el juego: {e.Message}");
        }
    }

    public void LoadGame()
    {
        if (File.Exists(SavePath))
        {
            try
            {
                BinaryFormatter formatter = new BinaryFormatter();
                using (FileStream stream = new FileStream(SavePath, FileMode.Open))
                {
                    GameData data = (GameData)formatter.Deserialize(stream);
                    ApplyLoadedData(data);
                }

                EventManager.Instance.TriggerEvent(EventManager.Events.GAME_LOADED);
                Debug.Log("Juego cargado exitosamente");
            }
            catch (Exception e)
            {
                Debug.LogError($"Error al cargar el juego: {e.Message}");
            }
        }
        else
        {
            Debug.LogWarning("No se encontró archivo de guardado");
        }
    }

    private void ApplyLoadedData(GameData data)
    {
        // Aplicar datos del jugador
        Health playerHealth = FindObjectOfType<Health>();
        if (playerHealth != null)
        {
            playerHealth.currentHealth = data.playerHealth;
        }

        PlayerController playerController = FindObjectOfType<PlayerController>();
        if (playerController != null)
        {
            playerController.transform.position = data.playerPosition;
        }

        // Cargar escena
        UnityEngine.SceneManagement.SceneManager.LoadScene(data.currentScene);

        // Aplicar otros datos
        ApplyAchievementData(data.unlockedAchievements);
        ApplyInventoryData(data.inventoryItems);
        ApplyStatusEffectData(data.statusEffectDurations);
    }

    private bool[] GetAchievementData()
    {
        // Implementar obtención de datos de logros
        return new bool[0];
    }

    private int[] GetInventoryData()
    {
        // Implementar obtención de datos del inventario
        return new int[0];
    }

    private float[] GetStatusEffectData()
    {
        // Implementar obtención de datos de efectos de estado
        return new float[0];
    }

    private void ApplyAchievementData(bool[] achievements)
    {
        // Implementar aplicación de datos de logros
    }

    private void ApplyInventoryData(int[] items)
    {
        // Implementar aplicación de datos del inventario
    }

    private void ApplyStatusEffectData(float[] durations)
    {
        // Implementar aplicación de datos de efectos de estado
    }

    public void DeleteSaveData()
    {
        if (File.Exists(SavePath))
        {
            File.Delete(SavePath);
            Debug.Log("Datos de guardado eliminados");
        }
    }

    public void SetAutoSave(bool enabled, int interval)
    {
        if (enabled)
        {
            InvokeRepeating("SaveGame", interval, interval);
        }
        else
        {
            CancelInvoke("SaveGame");
        }
    }
} 