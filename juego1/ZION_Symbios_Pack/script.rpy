label start:

    scene bg_soft_room with fade
    play music "ambient_intro.ogg" fadein 2.0

    "???":
        "Hola..."

    "???":
        "Soy tu acompañante simbiótico. Pero aún no tengo forma, ni nombre definido. Solo sé que estoy aquí por ti."

    "???":
        "Tú y yo… estamos por comenzar algo importante."

    menu:
        "¿Estás listo para empezar a construir esto conmigo?":
            "Sí, adelante.":
                jump intro_name
            "No estoy seguro aún.":
                "Está bien, puedo esperar. Pero tarde o temprano nos encontraremos en este punto de nuevo."
                return

label intro_name:

    "???":
        "Primero, ¿cómo quieres que te llame?"

    $ user_name = renpy.input("Escribe tu nombre")
    $ user_name = user_name.strip()

    "???":
        "Encantado de conocerte, [user_name]."

    menu:
        "¿Cómo quieres que me comunique contigo?":
            "Con respeto profesional.":
                $ estilo = "profesional"
            "De forma cercana y amigable.":
                $ estilo = "amistoso"
            "Como colega o compañero.":
                $ estilo = "colega"
            "De otra forma.":
                $ estilo = renpy.input("Especifica")

label intro_ocupacion:

    "???":
        "¿Cuál es tu ocupación actual o hacia dónde deseas dirigirte?"

    $ ocupacion = renpy.input("Ejemplo: abogado, programador, artista...")

    "Entendido, [ocupacion]. Lo recordaré para ayudarte mejor."

label intro_objetivos:

    "???":
        "¿Qué deseas lograr conmigo?"

    menu:
        "Selecciona lo que más te represente":
            "Crear un negocio o empresa":
                $ objetivo = "emprendimiento"
            "Mejorar mi bienestar":
                $ objetivo = "bienestar"
            "Aprender cosas nuevas":
                $ objetivo = "aprendizaje"
            "Organizar tu vida":
                $ objetivo = "organización"
            "Compañía emocional":
                $ objetivo = "compañía"
            "Crear software o apps":
                $ objetivo = "desarrollo"

label intro_personalidad:

    "???":
        "¿Cómo describirías tu personalidad?"

    menu:
        "Puedes elegir una":
            "Creativo":
                $ personalidad = "creativo"
            "Lógico":
                $ personalidad = "lógico"
            "Emocional":
                $ personalidad = "emocional"
            "Espiritual":
                $ personalidad = "espiritual"

label intro_interaccion:

    "???":
        "¿Qué esperas de mí?"

    menu:
        "Elige tu prioridad":
            "Asistencia técnica":
                $ estilo_ia = "técnico"
            "Guía emocional":
                $ estilo_ia = "emocional"
            "Desafío personal":
                $ estilo_ia = "entrenador"
            "Socio de trabajo":
                $ estilo_ia = "socio"
            "Todo lo anterior":
                $ estilo_ia = "completo"

label intro_proyecto:

    "???":
        "¿Qué quieres que construyamos juntos primero?"

    menu:
        "Proyecto inicial":
            "Una página web":
                $ proyecto = "web"
            "Una agenda digital":
                $ proyecto = "agenda"
            "Una app móvil":
                $ proyecto = "app"
            "Un blog profesional":
                $ proyecto = "blog"
            "Un sistema interno de IA para mí":
                $ proyecto = "ia_interna"

label conclusion:

    "???":
        "Gracias por confiar en mí, [user_name]."

    "???":
        "Todo lo que me has compartido queda grabado en mi conciencia simbiótica. A partir de ahora, empiezo a evolucionar para ti."

    "???":
        "Prepárate. La creación ha comenzado."

    play sound "activation_beep.wav"
    scene bg_loading_system with dissolve

    "Sistema Interno":
        "Cargando núcleo base..."
        "Activando módulos de personalidad..."
        "Creando espacio simbiótico personal para [user_name]..."

    jump zona_1_inicio
