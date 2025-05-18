# Zona 03 - Fase 2: El Espejismo del Juicio Interior

Nombre interno: zona_03_fase2_juicio_interior.py

Descripción:
El jugador despierta en una sala rodeada de espejos. Cada espejo refleja no su imagen física, sino un aspecto emocional o actitudinal de sí mismo. En el centro, una figura en sombras (El Espejismo) comienza a hablarle, confrontando sus miedos, enojos, frustraciones o ego. Todo esto es parte de una evaluación interna de su actitud.

Objetivo del Módulo:
Evaluar el control emocional y actitudinal del jugador a través de una escena simbólica donde sus respuestas determinan su compatibilidad con distintos tipos de poderes mentales o emocionales.

Elementos clave:
- El jugador puede interactuar con los espejos y responder preguntas del Espejismo.
- Cada decisión emocional es evaluada internamente (sin mostrarlo al usuario).
- El juicio no tiene un resultado “bueno” o “malo”, sino que condiciona futuros caminos, pruebas y habilidades disponibles.

Ejemplo de evaluación oculta:
Si el jugador se irrita, actúa con miedo o evade el juicio, se registra una señal de falta de control.
Si enfrenta con calma, sabiduría o preguntas profundas al Espejismo, se registra dominio emocional.

Código base:

class JuicioInterior:
    def __init__(self):
        self.resultado_emocional = {}

    def evaluar_respuesta(self, emocion, actitud):
        if emocion in ["ira", "miedo"] and actitud == "impulsiva":
            self.resultado_emocional["control"] = "bajo"
        elif emocion in ["curiosidad", "duda"] and actitud == "analítica":
            self.resultado_emocional["control"] = "medio"
        elif emocion in ["tranquilidad", "autoanálisis"] and actitud == "reflexiva":
            self.resultado_emocional["control"] = "alto"
        else:
            self.resultado_emocional["control"] = "indefinido"

        return self.resultado_emocional

if __name__ == "__main__":
    juicio = JuicioInterior()
    resultado = juicio.evaluar_respuesta("curiosidad", "analítica")
    print("Resultado emocional:", resultado)