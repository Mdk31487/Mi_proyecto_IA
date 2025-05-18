using UnityEngine;
using UnityEngine.UI;

public class IntroUI : MonoBehaviour {
    public Text messageText;
    public Button continueButton;

    void Start() {
        messageText.text = "¿Estás listo para continuar al siguiente mundo?";
        continueButton.onClick.AddListener(OnContinue);
    }

    void OnContinue() {
        // Lógica para cargar siguiente mundo
    }
}
