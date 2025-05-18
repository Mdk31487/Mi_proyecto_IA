label zona7_laboratorio_proyectos:

    scene bg_hightech_lab
    with fade

    show ia_avatar at center
    with dissolve

    ia_avatar "Bienvenido al Laboratorio de Proyectos Avanzados."
    ia_avatar "Aquí podemos co-crear proyectos complejos: apps, bots y asistentes."
    ia_avatar "Primero selecciona qué deseas iniciar."

    menu:
        "Crear asistente de voz":
            jump proyecto_asistente_voz
        "Crear página web":
            jump proyecto_web
        "Crear app móvil":
            jump proyecto_app
        "Otro proyecto":
            jump proyecto_otro

label proyecto_asistente_voz:
    ia_avatar "Has elegido un asistente de voz. Genial."
    ia_avatar "Responde estas preguntas para configurarlo:"

    "IA" "¿Cuál es el nombre de tu asistente?"
    $ assistant_name = renpy.input("Nombre del asistente:")
    "IA" "¿Qué funciones básicas debe tener tu asistente de voz?"
    menu:
        "Responder preguntas generales":
            $ func = "qa"
        "Controlar dispositivos":
            $ func = "device_control"
        "Agendar citas":
            $ func = "schedule"
        "Otra función":
            $ func = "other"

    ia_avatar "Perfecto, crearé la base del asistente [assistant_name] con la función [func]."
    jump fin_zona7

label fin_zona7:
    ia_avatar "Tu asistente de voz está listo para probarse."
    return
