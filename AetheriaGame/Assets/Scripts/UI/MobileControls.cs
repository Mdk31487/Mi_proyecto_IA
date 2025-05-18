using UnityEngine;
using UnityEngine.UI;
using UnityEngine.EventSystems;

public class MobileControls : MonoBehaviour
{
    public static MobileControls Instance { get; private set; }

    [Header("Joystick")]
    public Joystick moveJoystick;
    public float joystickDeadzone = 0.1f;

    [Header("Botones de Acción")]
    public Button jumpButton;
    public Button interactButton;
    public Button attackButton;
    public Button inventoryButton;

    [Header("Configuración")]
    public bool showControls = true;
    public float buttonOpacity = 0.7f;

    private PlayerController playerController;
    private CanvasGroup controlsCanvasGroup;

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

        controlsCanvasGroup = GetComponent<CanvasGroup>();
        if (controlsCanvasGroup == null)
        {
            controlsCanvasGroup = gameObject.AddComponent<CanvasGroup>();
        }
    }

    private void Start()
    {
        playerController = FindObjectOfType<PlayerController>();
        SetupButtons();
        UpdateControlsVisibility();
    }

    private void Update()
    {
        if (playerController != null && showControls)
        {
            // Obtener input del joystick
            Vector2 joystickInput = new Vector2(moveJoystick.Horizontal, moveJoystick.Vertical);
            
            // Aplicar deadzone
            if (joystickInput.magnitude < joystickDeadzone)
            {
                joystickInput = Vector2.zero;
            }

            // Enviar movimiento al jugador
            playerController.SetMovementInput(joystickInput);
        }
    }

    private void SetupButtons()
    {
        if (jumpButton != null)
        {
            jumpButton.onClick.AddListener(() => {
                if (playerController != null)
                {
                    playerController.Jump();
                }
            });
        }

        if (interactButton != null)
        {
            interactButton.onClick.AddListener(() => {
                if (playerController != null)
                {
                    playerController.Interact();
                }
            });
        }

        if (attackButton != null)
        {
            attackButton.onClick.AddListener(() => {
                if (playerController != null)
                {
                    playerController.Attack();
                }
            });
        }

        if (inventoryButton != null)
        {
            inventoryButton.onClick.AddListener(() => {
                if (playerController != null)
                {
                    playerController.ToggleInventory();
                }
            });
        }
    }

    public void UpdateControlsVisibility()
    {
        if (controlsCanvasGroup != null)
        {
            controlsCanvasGroup.alpha = showControls ? buttonOpacity : 0f;
            controlsCanvasGroup.interactable = showControls;
            controlsCanvasGroup.blocksRaycasts = showControls;
        }
    }

    public void ToggleControls()
    {
        showControls = !showControls;
        UpdateControlsVisibility();
    }

    public void SetButtonOpacity(float opacity)
    {
        buttonOpacity = Mathf.Clamp01(opacity);
        if (controlsCanvasGroup != null)
        {
            controlsCanvasGroup.alpha = showControls ? buttonOpacity : 0f;
        }
    }
} 