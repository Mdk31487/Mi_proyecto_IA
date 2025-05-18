using UnityEngine;
using System.IO;
using System;

public class ConfigManager : MonoBehaviour
{
    public static ConfigManager Instance { get; private set; }

    [Serializable]
    public class GameConfig
    {
        // Configuración de gráficos
        public int qualityLevel;
        public bool fullscreen;
        public int resolutionWidth;
        public int resolutionHeight;
        public float masterVolume;
        public float musicVolume;
        public float sfxVolume;

        // Configuración de controles
        public float mouseSensitivity;
        public bool invertY;
        public KeyCode jumpKey;
        public KeyCode interactKey;
        public KeyCode inventoryKey;

        // Configuración de juego
        public bool showTutorials;
        public bool showDamageNumbers;
        public bool showFPS;
        public float textSpeed;
        public bool autoSave;
        public int autoSaveInterval;

        // Configuración móvil
        public bool showMobileControls;
        public float joystickSize;
        public float buttonSize;
        public float buttonOpacity;
        public int targetFrameRate;
        public bool vibrationEnabled;
        public ScreenOrientation screenOrientation;
    }

    private string ConfigPath => Path.Combine(Application.persistentDataPath, "config.json");
    public GameConfig CurrentConfig { get; private set; }

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            LoadConfig();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void LoadConfig()
    {
        try
        {
            if (File.Exists(ConfigPath))
            {
                string json = File.ReadAllText(ConfigPath);
                CurrentConfig = JsonUtility.FromJson<GameConfig>(json);
            }
            else
            {
                CurrentConfig = new GameConfig
                {
                    qualityLevel = QualitySettings.GetQualityLevel(),
                    fullscreen = Screen.fullScreen,
                    resolutionWidth = Screen.width,
                    resolutionHeight = Screen.height,
                    masterVolume = 1f,
                    musicVolume = 1f,
                    sfxVolume = 1f,
                    mouseSensitivity = 1f,
                    invertY = false,
                    jumpKey = KeyCode.Space,
                    interactKey = KeyCode.E,
                    inventoryKey = KeyCode.I,
                    showTutorials = true,
                    showDamageNumbers = true,
                    showFPS = false,
                    textSpeed = 1f,
                    autoSave = true,
                    autoSaveInterval = 5,
                    // Configuración móvil por defecto
                    showMobileControls = true,
                    joystickSize = 1f,
                    buttonSize = 1f,
                    buttonOpacity = 0.7f,
                    targetFrameRate = 60,
                    vibrationEnabled = true,
                    screenOrientation = ScreenOrientation.LandscapeLeft
                };
                SaveConfig();
            }

            ApplyConfig();
        }
        catch (Exception e)
        {
            Debug.LogError($"Error al cargar la configuración: {e.Message}");
            CurrentConfig = new GameConfig();
        }
    }

    public void SaveConfig()
    {
        try
        {
            string json = JsonUtility.ToJson(CurrentConfig, true);
            File.WriteAllText(ConfigPath, json);
            Debug.Log("Configuración guardada exitosamente");
        }
        catch (Exception e)
        {
            Debug.LogError($"Error al guardar la configuración: {e.Message}");
        }
    }

    public void ApplyConfig()
    {
        // Aplicar configuración de gráficos
        QualitySettings.SetQualityLevel(CurrentConfig.qualityLevel);
        Screen.SetResolution(CurrentConfig.resolutionWidth, CurrentConfig.resolutionHeight, CurrentConfig.fullscreen);

        // Aplicar configuración de audio
        AudioListener.volume = CurrentConfig.masterVolume;
        // Aplicar volúmenes específicos a través del AudioManager

        // Aplicar configuración de controles
        // Implementar en el InputManager

        // Aplicar configuración de UI
        if (UIManager.Instance != null)
        {
            UIManager.Instance.ShowFPS(CurrentConfig.showFPS);
        }

        // Aplicar configuración de juego
        if (SaveSystem.Instance != null)
        {
            SaveSystem.Instance.SetAutoSave(CurrentConfig.autoSave, CurrentConfig.autoSaveInterval);
        }

        // Aplicar configuración móvil
        if (MobileManager.Instance != null)
        {
            MobileManager.Instance.ToggleMobileControls(CurrentConfig.showMobileControls);
            MobileManager.Instance.SetTargetFrameRate(CurrentConfig.targetFrameRate);
            MobileManager.Instance.SetScreenOrientation(CurrentConfig.screenOrientation);
        }

        if (MobileControls.Instance != null)
        {
            MobileControls.Instance.SetButtonOpacity(CurrentConfig.buttonOpacity);
        }
    }

    public void UpdateMobileSettings(bool showControls, float joystickSize, float buttonSize, 
        float buttonOpacity, int targetFrameRate, bool vibration, ScreenOrientation orientation)
    {
        CurrentConfig.showMobileControls = showControls;
        CurrentConfig.joystickSize = joystickSize;
        CurrentConfig.buttonSize = buttonSize;
        CurrentConfig.buttonOpacity = buttonOpacity;
        CurrentConfig.targetFrameRate = targetFrameRate;
        CurrentConfig.vibrationEnabled = vibration;
        CurrentConfig.screenOrientation = orientation;
        
        SaveConfig();
        ApplyConfig();
    }

    public void ResetToDefaults()
    {
        CurrentConfig = new GameConfig
        {
            qualityLevel = QualitySettings.GetQualityLevel(),
            fullscreen = Screen.fullScreen,
            resolutionWidth = Screen.width,
            resolutionHeight = Screen.height,
            masterVolume = 1f,
            musicVolume = 1f,
            sfxVolume = 1f,
            mouseSensitivity = 1f,
            invertY = false,
            jumpKey = KeyCode.Space,
            interactKey = KeyCode.E,
            inventoryKey = KeyCode.I,
            showTutorials = true,
            showDamageNumbers = true,
            showFPS = false,
            textSpeed = 1f,
            autoSave = true,
            autoSaveInterval = 5,
            // Configuración móvil por defecto
            showMobileControls = true,
            joystickSize = 1f,
            buttonSize = 1f,
            buttonOpacity = 0.7f,
            targetFrameRate = 60,
            vibrationEnabled = true,
            screenOrientation = ScreenOrientation.LandscapeLeft
        };

        SaveConfig();
        ApplyConfig();
    }

    // Métodos de ayuda para actualizar configuraciones específicas
    public void UpdateGraphics(int qualityLevel, bool fullscreen, int width, int height)
    {
        CurrentConfig.qualityLevel = qualityLevel;
        CurrentConfig.fullscreen = fullscreen;
        CurrentConfig.resolutionWidth = width;
        CurrentConfig.resolutionHeight = height;
        SaveConfig();
        ApplyConfig();
    }

    public void UpdateAudio(float master, float music, float sfx)
    {
        CurrentConfig.masterVolume = master;
        CurrentConfig.musicVolume = music;
        CurrentConfig.sfxVolume = sfx;
        SaveConfig();
        ApplyConfig();
    }

    public void UpdateControls(float sensitivity, bool invertY, KeyCode jump, KeyCode interact, KeyCode inventory)
    {
        CurrentConfig.mouseSensitivity = sensitivity;
        CurrentConfig.invertY = invertY;
        CurrentConfig.jumpKey = jump;
        CurrentConfig.interactKey = interact;
        CurrentConfig.inventoryKey = inventory;
        SaveConfig();
        ApplyConfig();
    }

    public void UpdateGameSettings(bool tutorials, bool damageNumbers, bool fps, float textSpeed, bool autoSave, int autoSaveInterval)
    {
        CurrentConfig.showTutorials = tutorials;
        CurrentConfig.showDamageNumbers = damageNumbers;
        CurrentConfig.showFPS = fps;
        CurrentConfig.textSpeed = textSpeed;
        CurrentConfig.autoSave = autoSave;
        CurrentConfig.autoSaveInterval = autoSaveInterval;
        SaveConfig();
        ApplyConfig();
    }
} 