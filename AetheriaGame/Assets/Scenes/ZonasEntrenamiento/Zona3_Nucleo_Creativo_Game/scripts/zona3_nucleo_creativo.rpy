
label zona3_nucleo_creativo:

    scene bg_lab_interior
    with fade

    show ia_avatar at center
    with dissolve

    ia_avatar "Bienvenido al Núcleo Creativo, Carlos G."
    ia_avatar "Aquí empieza la construcción de tu herramienta ideal: una app, página web o asistente personalizado."

    ia_avatar "Primero, necesito conocerte un poco más. ¿A qué te dedicas?"

    menu:
        "Soy abogado":
            $ profesion = "abogado"
        "Soy programador":
            $ profesion = "programador"
        "Soy artista digital":
            $ profesion = "artista digital"
        "Otra profesión":
            $ profesion = "otro"

    ia_avatar "Perfecto, siendo un [profesion], tu herramienta debe ayudarte en tu día a día."

    ia_avatar "Ahora dime, ¿para qué deseas esta herramienta?"

    menu:
        "Agendar citas o clientes":
            $ objetivo = "agenda"
        "Mostrar mis servicios en línea":
            $ objetivo = "portafolio"
        "Desarrollar ideas o proyectos":
            $ objetivo = "desarrollo"
        "Aprender o estudiar mejor":
            $ objetivo = "aprendizaje"

    ia_avatar "Gracias por compartirlo. Diseñaré la estructura interna adecuada..."

    scene black with fade
    pause 1

    ia_avatar "He terminado una versión preliminar de tu asistente. ¿Quieres probarla ya o seguir personalizándola?"

    menu:
        "Probar ahora":
            jump probar_asistente
        "Seguir personalizando":
            jump personalizar_mas

    return
