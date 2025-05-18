label zona10_laboratorio_ensueno:

    scene bg_dreamscape with fade
    play music "dreamy_ambience.ogg"

    "IA":
        "Bienvenido al Laboratorio de Ensueño, donde tu imaginación toma forma."
    "IA":
        "Describe la meta o el recuerdo que deseas explorar."

    $ user_input = renpy.input("Escribe tu visión:")
    "IA":
        "Excelente. Generando tu sueño interactivo..."

    jump fin_zona10

label fin_zona10:
    "IA":
        "Tu mundo de ensueño está listo. Explóralo cuando quieras."
    return
