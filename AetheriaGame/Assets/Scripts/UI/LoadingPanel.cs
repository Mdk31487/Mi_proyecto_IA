using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.Collections;

public class LoadingPanel : MonoBehaviour
{
    [Header("UI Elements")]
    public TextMeshProUGUI loadingText;
    public Slider progressBar;
    public TextMeshProUGUI progressText;
    public TextMeshProUGUI tipText;

    [Header("Loading Settings")]
    public float minLoadingTime = 1f;
    public string[] loadingTips;

    private UIManager uiManager;
    private AudioManager audioManager;
    private AsyncOperation loadingOperation;
    private float loadingProgress;
    private bool isLoading;

    private void Start()
    {
        uiManager = GetComponent<UIManager>();
        audioManager = GetComponent<AudioManager>();
        HideLoading();
    }

    public void ShowLoading(string sceneName)
    {
        gameObject.SetActive(true);
        isLoading = true;
        loadingProgress = 0f;

        if (progressBar != null)
        {
            progressBar.value = 0f;
        }

        if (loadingText != null)
        {
            loadingText.text = "Cargando...";
        }

        if (progressText != null)
        {
            progressText.text = "0%";
        }

        if (tipText != null && loadingTips != null && loadingTips.Length > 0)
        {
            tipText.text = loadingTips[Random.Range(0, loadingTips.Length)];
        }

        StartCoroutine(LoadSceneAsync(sceneName));
    }

    private IEnumerator LoadSceneAsync(string sceneName)
    {
        float startTime = Time.time;
        loadingOperation = UnityEngine.SceneManagement.SceneManager.LoadSceneAsync(sceneName);
        loadingOperation.allowSceneActivation = false;

        while (!loadingOperation.isDone)
        {
            loadingProgress = Mathf.Clamp01(loadingOperation.progress / 0.9f);
            
            if (progressBar != null)
            {
                progressBar.value = loadingProgress;
            }

            if (progressText != null)
            {
                progressText.text = $"{Mathf.Round(loadingProgress * 100)}%";
            }

            if (loadingOperation.progress >= 0.9f)
            {
                if (Time.time - startTime >= minLoadingTime)
                {
                    loadingOperation.allowSceneActivation = true;
                }
            }

            yield return null;
        }

        isLoading = false;
        HideLoading();
    }

    public void HideLoading()
    {
        gameObject.SetActive(false);
        if (loadingOperation != null)
        {
            loadingOperation = null;
        }
        isLoading = false;
    }

    public bool IsLoading()
    {
        return isLoading;
    }

    public float GetLoadingProgress()
    {
        return loadingProgress;
    }
} 