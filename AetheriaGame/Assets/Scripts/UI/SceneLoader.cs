using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;

public class SceneLoader : MonoBehaviour
{
    [Header("Loading Settings")]
    public float minLoadingTime = 1f;
    public string[] loadingTips;

    private UIManager uiManager;
    private AudioManager audioManager;
    private LoadingPanel loadingPanel;
    private AsyncOperation loadingOperation;
    private bool isLoading;

    private void Start()
    {
        uiManager = GetComponent<UIManager>();
        audioManager = GetComponent<AudioManager>();
        loadingPanel = GetComponent<LoadingPanel>();
    }

    public void LoadScene(string sceneName)
    {
        if (!isLoading)
        {
            StartCoroutine(LoadSceneAsync(sceneName));
        }
    }

    public void LoadSceneAsync(string sceneName)
    {
        if (!isLoading)
        {
            if (loadingPanel != null)
            {
                loadingPanel.ShowLoading(sceneName);
            }
            else
            {
                StartCoroutine(LoadSceneAsync(sceneName));
            }
        }
    }

    private IEnumerator LoadSceneAsync(string sceneName)
    {
        isLoading = true;
        float startTime = Time.time;

        if (audioManager != null)
        {
            audioManager.PlaySFX("LoadingStart");
        }

        loadingOperation = SceneManager.LoadSceneAsync(sceneName);
        loadingOperation.allowSceneActivation = false;

        while (!loadingOperation.isDone)
        {
            if (loadingOperation.progress >= 0.9f)
            {
                if (Time.time - startTime >= minLoadingTime)
                {
                    loadingOperation.allowSceneActivation = true;
                }
            }

            yield return null;
        }

        if (audioManager != null)
        {
            audioManager.PlaySFX("LoadingComplete");
        }

        isLoading = false;
    }

    public void ReloadCurrentScene()
    {
        LoadScene(SceneManager.GetActiveScene().name);
    }

    public void LoadNextScene()
    {
        int currentSceneIndex = SceneManager.GetActiveScene().buildIndex;
        if (currentSceneIndex < SceneManager.sceneCountInBuildSettings - 1)
        {
            LoadScene(SceneManager.GetSceneByBuildIndex(currentSceneIndex + 1).name);
        }
    }

    public void LoadPreviousScene()
    {
        int currentSceneIndex = SceneManager.GetActiveScene().buildIndex;
        if (currentSceneIndex > 0)
        {
            LoadScene(SceneManager.GetSceneByBuildIndex(currentSceneIndex - 1).name);
        }
    }

    public bool IsLoading()
    {
        return isLoading;
    }

    public float GetLoadingProgress()
    {
        if (loadingOperation != null)
        {
            return loadingOperation.progress;
        }
        return 0f;
    }
} 