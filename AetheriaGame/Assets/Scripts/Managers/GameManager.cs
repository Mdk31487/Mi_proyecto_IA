using UnityEngine;

public class GameManager : MonoBehaviour
{
    public static GameManager Instance { get; private set; }

    [Header("Managers")]
    public UIManager uiManager;
    public AudioManager audioManager;
    public SceneLoader sceneLoader;

    [Header("Test Components")]
    public UITest uiTest;

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

    private void Start()
    {
        if (uiTest != null)
        {
            uiTest.RunTests();
        }
    }

    public void PauseGame()
    {
        Time.timeScale = 0f;
        if (uiManager != null)
        {
            uiManager.ShowPauseMenu();
        }
    }

    public void ResumeGame()
    {
        Time.timeScale = 1f;
        if (uiManager != null)
        {
            uiManager.HidePauseMenu();
        }
    }

    public void QuitGame()
    {
        #if UNITY_EDITOR
            UnityEditor.EditorApplication.isPlaying = false;
        #else
            Application.Quit();
        #endif
    }
} 