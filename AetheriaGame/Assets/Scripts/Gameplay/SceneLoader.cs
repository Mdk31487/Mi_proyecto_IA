using UnityEngine;
using UnityEngine.SceneManagement;
using System.Collections;
using UnityEngine.UI;

public class SceneLoader : MonoBehaviour
{
    public static SceneLoader Instance { get; private set; }

    [SerializeField] private CanvasGroup fadeCanvasGroup;
    [SerializeField] private float fadeDuration = 1f;
    [SerializeField] private Image fadeImage;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            InitializeFadeCanvas();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void InitializeFadeCanvas()
    {
        if (fadeCanvasGroup == null)
        {
            GameObject canvasObj = new GameObject("FadeCanvas");
            fadeCanvasGroup = canvasObj.AddComponent<CanvasGroup>();
            Canvas canvas = canvasObj.AddComponent<Canvas>();
            canvas.renderMode = RenderMode.ScreenSpaceOverlay;
            canvas.sortingOrder = 999;

            fadeImage = new GameObject("FadeImage").AddComponent<Image>();
            fadeImage.transform.SetParent(canvasObj.transform, false);
            fadeImage.color = Color.black;
            fadeImage.rectTransform.anchorMin = Vector2.zero;
            fadeImage.rectTransform.anchorMax = Vector2.one;
            fadeImage.rectTransform.sizeDelta = Vector2.zero;

            DontDestroyOnLoad(canvasObj);
        }
    }

    public void LoadScene(string sceneName, bool useFade = true)
    {
        if (useFade)
        {
            StartCoroutine(LoadSceneWithFade(sceneName));
        }
        else
        {
            SceneManager.LoadScene(sceneName);
        }
    }

    public void LoadScene(int sceneIndex, bool useFade = true)
    {
        if (useFade)
        {
            StartCoroutine(LoadSceneWithFade(sceneIndex));
        }
        else
        {
            SceneManager.LoadScene(sceneIndex);
        }
    }

    private IEnumerator LoadSceneWithFade(string sceneName)
    {
        yield return StartCoroutine(FadeOut());
        
        AsyncOperation asyncLoad = SceneManager.LoadSceneAsync(sceneName);
        asyncLoad.allowSceneActivation = false;

        while (asyncLoad.progress < 0.9f)
        {
            yield return null;
        }

        asyncLoad.allowSceneActivation = true;
        yield return StartCoroutine(FadeIn());
    }

    private IEnumerator LoadSceneWithFade(int sceneIndex)
    {
        yield return StartCoroutine(FadeOut());
        
        AsyncOperation asyncLoad = SceneManager.LoadSceneAsync(sceneIndex);
        asyncLoad.allowSceneActivation = false;

        while (asyncLoad.progress < 0.9f)
        {
            yield return null;
        }

        asyncLoad.allowSceneActivation = true;
        yield return StartCoroutine(FadeIn());
    }

    private IEnumerator FadeOut()
    {
        float elapsedTime = 0f;
        fadeCanvasGroup.alpha = 0f;

        while (elapsedTime < fadeDuration)
        {
            elapsedTime += Time.deltaTime;
            fadeCanvasGroup.alpha = Mathf.Clamp01(elapsedTime / fadeDuration);
            yield return null;
        }

        fadeCanvasGroup.alpha = 1f;
    }

    private IEnumerator FadeIn()
    {
        float elapsedTime = 0f;
        fadeCanvasGroup.alpha = 1f;

        while (elapsedTime < fadeDuration)
        {
            elapsedTime += Time.deltaTime;
            fadeCanvasGroup.alpha = 1f - Mathf.Clamp01(elapsedTime / fadeDuration);
            yield return null;
        }

        fadeCanvasGroup.alpha = 0f;
    }

    public void LoadNextScene(bool useFade = true)
    {
        int nextSceneIndex = SceneManager.GetActiveScene().buildIndex + 1;
        if (nextSceneIndex < SceneManager.sceneCountInBuildSettings)
        {
            LoadScene(nextSceneIndex, useFade);
        }
    }

    public void ReloadCurrentScene(bool useFade = true)
    {
        LoadScene(SceneManager.GetActiveScene().buildIndex, useFade);
    }
} 