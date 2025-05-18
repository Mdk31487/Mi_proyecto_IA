using UnityEngine;
using UnityEngine.InputSystem;
using UnityEngine.InputSystem.EnhancedTouch;
using Touch = UnityEngine.InputSystem.EnhancedTouch.Touch;

public class MobileInput : MonoBehaviour
{
    public static MobileInput Instance { get; private set; }

    [Header("Joystick Settings")]
    public float joystickDeadzone = 0.1f;
    public float maxJoystickDistance = 100f;

    [Header("Touch Settings")]
    public float minSwipeDistance = 50f;
    public float maxSwipeTime = 0.5f;

    private Vector2 joystickPosition;
    private Vector2 joystickDirection;
    private bool isJoystickActive;
    private int joystickFingerId = -1;

    private Vector2 touchStartPosition;
    private float touchStartTime;
    private bool isSwiping;

    private void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            EnhancedTouchSupport.Enable();
        }
        else
        {
            Destroy(gameObject);
        }
    }

    private void OnEnable()
    {
        Touch.onFingerDown += OnFingerDown;
        Touch.onFingerUp += OnFingerUp;
        Touch.onFingerMove += OnFingerMove;
    }

    private void OnDisable()
    {
        Touch.onFingerDown -= OnFingerDown;
        Touch.onFingerUp -= OnFingerUp;
        Touch.onFingerMove -= OnFingerMove;
    }

    private void OnFingerDown(Finger finger)
    {
        if (joystickFingerId == -1)
        {
            // Iniciar joystick
            joystickFingerId = finger.index;
            joystickPosition = finger.screenPosition;
            isJoystickActive = true;
        }
        else
        {
            // Iniciar swipe
            touchStartPosition = finger.screenPosition;
            touchStartTime = Time.time;
            isSwiping = true;
        }
    }

    private void OnFingerUp(Finger finger)
    {
        if (finger.index == joystickFingerId)
        {
            // Resetear joystick
            joystickFingerId = -1;
            isJoystickActive = false;
            joystickDirection = Vector2.zero;
        }
        else if (isSwiping)
        {
            // Procesar swipe
            ProcessSwipe(finger.screenPosition);
            isSwiping = false;
        }
    }

    private void OnFingerMove(Finger finger)
    {
        if (finger.index == joystickFingerId && isJoystickActive)
        {
            // Actualizar dirección del joystick
            Vector2 delta = finger.screenPosition - joystickPosition;
            float distance = delta.magnitude;

            if (distance > joystickDeadzone)
            {
                joystickDirection = delta.normalized;
                if (distance > maxJoystickDistance)
                {
                    joystickDirection *= maxJoystickDistance / distance;
                }
            }
            else
            {
                joystickDirection = Vector2.zero;
            }
        }
    }

    private void ProcessSwipe(Vector2 endPosition)
    {
        Vector2 swipeDelta = endPosition - touchStartPosition;
        float swipeTime = Time.time - touchStartTime;

        if (swipeDelta.magnitude >= minSwipeDistance && swipeTime <= maxSwipeTime)
        {
            // Determinar dirección del swipe
            if (Mathf.Abs(swipeDelta.x) > Mathf.Abs(swipeDelta.y))
            {
                // Swipe horizontal
                if (swipeDelta.x > 0)
                {
                    // Swipe derecha
                    OnSwipeRight();
                }
                else
                {
                    // Swipe izquierda
                    OnSwipeLeft();
                }
            }
            else
            {
                // Swipe vertical
                if (swipeDelta.y > 0)
                {
                    // Swipe arriba
                    OnSwipeUp();
                }
                else
                {
                    // Swipe abajo
                    OnSwipeDown();
                }
            }
        }
    }

    // Eventos de swipe
    private void OnSwipeRight()
    {
        // Implementar lógica de swipe derecha
        Debug.Log("Swipe Derecha");
    }

    private void OnSwipeLeft()
    {
        // Implementar lógica de swipe izquierda
        Debug.Log("Swipe Izquierda");
    }

    private void OnSwipeUp()
    {
        // Implementar lógica de swipe arriba
        Debug.Log("Swipe Arriba");
    }

    private void OnSwipeDown()
    {
        // Implementar lógica de swipe abajo
        Debug.Log("Swipe Abajo");
    }

    // Métodos públicos para obtener input
    public Vector2 GetJoystickDirection()
    {
        return joystickDirection;
    }

    public bool IsJoystickActive()
    {
        return isJoystickActive;
    }

    public Vector2 GetJoystickPosition()
    {
        return joystickPosition;
    }
} 