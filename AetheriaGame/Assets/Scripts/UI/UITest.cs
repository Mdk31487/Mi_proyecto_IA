using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.Collections;

public class UITest : MonoBehaviour
{
    [Header("Test Settings")]
    public float testDelay = 2f;
    public bool runTestsOnStart = true;

    private UIManager uiManager;
    private AudioManager audioManager;
    private SceneLoader sceneLoader;
    private HUD hud;
    private DialoguePanel dialoguePanel;
    private PauseMenu pauseMenu;
    private LoadingPanel loadingPanel;

    private void Start()
    {
        uiManager = GetComponent<UIManager>();
        audioManager = GetComponent<AudioManager>();
        sceneLoader = GetComponent<SceneLoader>();
        hud = GetComponent<HUD>();
        dialoguePanel = GetComponent<DialoguePanel>();
        pauseMenu = GetComponent<PauseMenu>();
        loadingPanel = GetComponent<LoadingPanel>();

        if (runTestsOnStart)
        {
            StartCoroutine(RunTests());
        }
    }

    private IEnumerator RunTests()
    {
        Debug.Log("Iniciando pruebas del sistema UI...");

        // Test 1: Menú Principal
        Debug.Log("Test 1: Mostrando menú principal");
        uiManager.ShowMainMenu();
        yield return new WaitForSeconds(testDelay);

        // Test 2: Menú de Pausa
        Debug.Log("Test 2: Mostrando menú de pausa");
        uiManager.ShowPauseMenu();
        yield return new WaitForSeconds(testDelay);
        uiManager.HidePauseMenu();

        // Test 3: Sistema de Diálogo
        Debug.Log("Test 3: Probando sistema de diálogo");
        dialoguePanel.ShowDialogue("Test NPC", "Este es un mensaje de prueba para verificar el sistema de diálogo.");
        yield return new WaitForSeconds(testDelay);
        dialoguePanel.HideDialogue();

        // Test 4: HUD
        Debug.Log("Test 4: Probando HUD");
        uiManager.ShowHUD();
        hud.UpdateHealth(75f, 100f);
        hud.UpdateExperience(50f, 100f, 2);
        hud.ShowNotification("¡Nivel 2 alcanzado!");
        yield return new WaitForSeconds(testDelay);

        // Test 5: Sistema de Audio
        Debug.Log("Test 5: Probando sistema de audio");
        audioManager.PlayMusic("MainTheme");
        yield return new WaitForSeconds(testDelay);
        audioManager.PlaySFX("ButtonClick");
        yield return new WaitForSeconds(1f);
        audioManager.StopMusic();

        // Test 6: Transición de Escena
        Debug.Log("Test 6: Probando transición de escena");
        loadingPanel.ShowLoading("TestScene");
        yield return new WaitForSeconds(testDelay);

        Debug.Log("Pruebas completadas");
    }

    // Métodos para pruebas manuales
    public void TestMainMenu()
    {
        uiManager.ShowMainMenu();
    }

    public void TestPauseMenu()
    {
        uiManager.ShowPauseMenu();
    }

    public void TestDialogue()
    {
        dialoguePanel.ShowDialogue("Test NPC", "Este es un mensaje de prueba.");
    }

    public void TestHUD()
    {
        uiManager.ShowHUD();
        hud.UpdateHealth(75f, 100f);
        hud.UpdateExperience(50f, 100f, 2);
    }

    public void TestAudio()
    {
        audioManager.PlayMusic("MainTheme");
    }

    public void TestLoading()
    {
        loadingPanel.ShowLoading("TestScene");
    }
} 