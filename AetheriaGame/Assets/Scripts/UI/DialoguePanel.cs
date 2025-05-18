using UnityEngine;
using UnityEngine.UI;
using TMPro;
using System.Collections;
using System.Collections.Generic;

public class DialoguePanel : MonoBehaviour
{
    [Header("Dialogue Elements")]
    public TextMeshProUGUI speakerNameText;
    public TextMeshProUGUI dialogueText;
    public Image speakerPortrait;
    public GameObject choicesContainer;
    public GameObject choiceButtonPrefab;

    [Header("Animation Settings")]
    public float typingSpeed = 0.05f;
    public float choiceDelay = 0.5f;

    [Header("Audio")]
    public AudioClip typingSound;
    public AudioClip choiceSelectSound;

    private UIManager uiManager;
    private AudioManager audioManager;
    private List<GameObject> choiceButtons = new List<GameObject>();
    private Coroutine typingCoroutine;
    private bool isTyping;
    private string currentDialogue;

    private void Start()
    {
        uiManager = GetComponent<UIManager>();
        audioManager = GetComponent<AudioManager>();
        HideDialogue();
    }

    public void ShowDialogue(string speakerName, string dialogue, Sprite portrait = null)
    {
        gameObject.SetActive(true);
        
        if (speakerNameText != null)
        {
            speakerNameText.text = speakerName;
        }

        if (speakerPortrait != null && portrait != null)
        {
            speakerPortrait.sprite = portrait;
            speakerPortrait.gameObject.SetActive(true);
        }
        else if (speakerPortrait != null)
        {
            speakerPortrait.gameObject.SetActive(false);
        }

        currentDialogue = dialogue;
        if (typingCoroutine != null)
        {
            StopCoroutine(typingCoroutine);
        }
        typingCoroutine = StartCoroutine(TypeText(dialogue));
    }

    public void ShowChoices(List<DialogueChoice> choices)
    {
        if (choicesContainer == null || choiceButtonPrefab == null) return;

        ClearChoices();

        foreach (DialogueChoice choice in choices)
        {
            GameObject choiceButton = Instantiate(choiceButtonPrefab, choicesContainer.transform);
            Button button = choiceButton.GetComponent<Button>();
            TextMeshProUGUI buttonText = choiceButton.GetComponentInChildren<TextMeshProUGUI>();

            if (buttonText != null)
            {
                buttonText.text = choice.text;
            }

            if (button != null)
            {
                button.onClick.AddListener(() => OnChoiceSelected(choice));
            }

            choiceButtons.Add(choiceButton);
        }

        choicesContainer.SetActive(true);
    }

    private void ClearChoices()
    {
        foreach (GameObject button in choiceButtons)
        {
            Destroy(button);
        }
        choiceButtons.Clear();
        choicesContainer.SetActive(false);
    }

    private IEnumerator TypeText(string text)
    {
        isTyping = true;
        dialogueText.text = "";

        foreach (char c in text)
        {
            dialogueText.text += c;
            if (typingSound != null && audioManager != null)
            {
                audioManager.PlaySFX(typingSound);
            }
            yield return new WaitForSeconds(typingSpeed);
        }

        isTyping = false;
    }

    private void OnChoiceSelected(DialogueChoice choice)
    {
        if (choiceSelectSound != null && audioManager != null)
        {
            audioManager.PlaySFX(choiceSelectSound);
        }

        if (choice.onSelect != null)
        {
            choice.onSelect.Invoke();
        }

        HideDialogue();
    }

    public void HideDialogue()
    {
        gameObject.SetActive(false);
        ClearChoices();
        if (typingCoroutine != null)
        {
            StopCoroutine(typingCoroutine);
        }
        isTyping = false;
    }

    public void SkipTyping()
    {
        if (isTyping && typingCoroutine != null)
        {
            StopCoroutine(typingCoroutine);
            dialogueText.text = currentDialogue;
            isTyping = false;
        }
    }
}

[System.Serializable]
public class DialogueChoice
{
    public string text;
    public UnityEngine.Events.UnityEvent onSelect;
} 