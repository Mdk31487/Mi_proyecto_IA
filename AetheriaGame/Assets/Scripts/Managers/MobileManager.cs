using UnityEngine;
using UnityEngine.UI;

public class MobileManager : MonoBehaviour
{
    public static MobileManager Instance { get; private set; }

    [Header("UI References")]
    public GameObject mobileControls;
    public CanvasScaler canvasScaler;

    [Header("Mobile Settings")]
    public bool forceMobileUI = false;
    public float defaultDPI = 160f;
    public float defaultScale = 1f;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            InitializeMobileSettings();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void InitializeMobileSettings()
    {
        // Detectar si estamos en una plataforma móvil
        bool isMobile = Application.isMobilePlatform || forceMobileUI;

        if (isMobile)
        {
            // Configurar UI para móvil
            SetupMobileUI();
            
            // Activar controles táctiles
            if (mobileControls != null)
            {
                mobileControls.SetActive(true);
            }

            // Configurar calidad gráfica para móvil
            QualitySettings.vSyncCount = 0;
            Application.targetFrameRate = 60;
            
            // Ajustar resolución
            Screen.SetResolution(Screen.width, Screen.height, true);
        }
        else
        {
            // Desactivar controles táctiles en PC
            if (mobileControls != null)
            {
                mobileControls.SetActive(false);
            }
        }
    }

    private void SetupMobileUI()
    {
        if (canvasScaler != null)
        {
            // Calcular escala basada en DPI
            float dpi = Screen.dpi;
            if (dpi == 0) dpi = defaultDPI;
            
            float scale = dpi / defaultDPI;
            canvasScaler.scaleFactor = scale * defaultScale;

            // Configurar para diferentes resoluciones
            canvasScaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
            canvasScaler.referenceResolution = new Vector2(1920, 1080);
            canvasScaler.screenMatchMode = CanvasScaler.ScreenMatchMode.MatchWidthOrHeight;
            canvasScaler.matchWidthOrHeight = 0.5f;
        }
    }

    public void SetMobileQuality(int qualityLevel)
    {
        QualitySettings.SetQualityLevel(qualityLevel, true);
    }

    public void SetTargetFrameRate(int frameRate)
    {
        Application.targetFrameRate = frameRate;
    }

    public void ToggleMobileControls(bool show)
    {
        if (mobileControls != null)
        {
            mobileControls.SetActive(show);
        }
    }

    public void SetMobileUI(bool force)
    {
        forceMobileUI = force;
        InitializeMobileSettings();
    }

    // Método para manejar la orientación de la pantalla
    public void SetScreenOrientation(ScreenOrientation orientation)
    {
        Screen.orientation = orientation;
    }

    // Método para manejar el modo de pantalla completa
    public void SetFullscreen(bool fullscreen)
    {
        Screen.fullScreen = fullscreen;
    }
} 