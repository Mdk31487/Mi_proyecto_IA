using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections.Generic;

public class SceneSetup : MonoBehaviour
{
    [System.Serializable]
    public class SceneInfo
    {
        public string sceneName;
        public string scenePath;
        public bool isLoaded;
    }

    [Header("Scene Configuration")]
    public List<SceneInfo> scenes = new List<SceneInfo>();

    [Header("References")]
    public Canvas mainCanvas;
    public GameObject player;
    public GameObject ground;
    public UISetup uiSetup;
    public PlayerSetup playerSetup;
    public StatusEffectSetup statusEffectSetup;

    [Header("Layer Settings")]
    public string groundLayerName = "Ground";

    private void Awake()
    {
        SetupScenes();
        SetupLayers();
        SetupReferences();
    }

    private void SetupScenes()
    {
        // Añadir escenas en orden
        scenes.Clear();
        scenes.Add(new SceneInfo { sceneName = "MainMenu", scenePath = "Assets/Scenes/MainMenu.unity" });
        scenes.Add(new SceneInfo { sceneName = "Modulo2", scenePath = "Assets/Scenes/MundoTierra/Modulo2.unity" });
        scenes.Add(new SceneInfo { sceneName = "Modulo3", scenePath = "Assets/Scenes/MundoTierra/Modulo3.unity" });
        scenes.Add(new SceneInfo { sceneName = "Modulo4", scenePath = "Assets/Scenes/MundoTierra/Modulo4.unity" });
        scenes.Add(new SceneInfo { sceneName = "Modulo6", scenePath = "Assets/Scenes/MundoTierra/Modulo6.unity" });
        scenes.Add(new SceneInfo { sceneName = "TemploDelSilencio", scenePath = "Assets/Scenes/TemploSilencio/TemploDelSilencio.unity" });

        // Añadir zonas de entrenamiento
        string[] trainingZones = new string[]
        {
            "ZonaEntrenamiento1",
            "ZonaEntrenamiento2",
            "ZonaEntrenamiento3"
        };

        foreach (string zone in trainingZones)
        {
            scenes.Add(new SceneInfo
            {
                sceneName = zone,
                scenePath = $"Assets/Scenes/ZonasEntrenamiento/{zone}.unity"
            });
        }
    }

    private void SetupLayers()
    {
        // Crear la capa Ground si no existe
        int groundLayer = LayerMask.NameToLayer(groundLayerName);
        if (groundLayer == -1)
        {
            Debug.LogWarning($"Layer '{groundLayerName}' no existe. Creando...");
            // Nota: No podemos crear capas desde el código, el usuario debe hacerlo manualmente
            return;
        }

        // Asignar la capa al plano
        if (ground != null)
        {
            ground.layer = groundLayer;
        }

        // Configurar el GroundMask en el PlayerSetup
        if (playerSetup != null)
        {
            playerSetup.groundMask = 1 << groundLayer;
        }
    }

    private void SetupReferences()
    {
        // Configurar UISetup
        if (uiSetup != null)
        {
            uiSetup.mainCanvas = mainCanvas;
        }

        // Configurar PlayerSetup
        if (playerSetup != null && player != null)
        {
            playerSetup.playerController = player.GetComponent<PlayerController>();
            playerSetup.health = player.GetComponent<Health>();
            Transform groundCheck = player.transform.Find("GroundCheck");
            if (groundCheck != null)
            {
                playerSetup.groundCheck = groundCheck;
            }
        }

        // Configurar StatusEffectSetup
        if (statusEffectSetup != null)
        {
            // Los sprites se deben asignar manualmente en el inspector
        }
    }

    public void AddScenesToBuildSettings()
    {
        #if UNITY_EDITOR
        // Obtener las escenas actuales en Build Settings
        List<UnityEditor.EditorBuildSettingsScene> buildScenes = new List<UnityEditor.EditorBuildSettingsScene>();

        // Añadir cada escena a Build Settings
        foreach (SceneInfo scene in scenes)
        {
            buildScenes.Add(new UnityEditor.EditorBuildSettingsScene(scene.scenePath, true));
        }

        // Actualizar Build Settings
        UnityEditor.EditorBuildSettings.scenes = buildScenes.ToArray();
        #endif
    }

    public void LoadScene(string sceneName)
    {
        SceneInfo scene = scenes.Find(s => s.sceneName == sceneName);
        if (scene != null)
        {
            SceneManager.LoadScene(scene.sceneName);
        }
        else
        {
            Debug.LogError($"Escena {sceneName} no encontrada!");
        }
    }

    public void LoadSceneAsync(string sceneName)
    {
        SceneInfo scene = scenes.Find(s => s.sceneName == sceneName);
        if (scene != null)
        {
            SceneManager.LoadSceneAsync(scene.sceneName);
        }
        else
        {
            Debug.LogError($"Escena {sceneName} no encontrada!");
        }
    }
} 