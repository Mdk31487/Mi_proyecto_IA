
# Zona 23: Laboratorio de Creatividad y Expresión Artística

import random

class CreativeEngine:
    def __init__(self):
        self.creations = []

    def generate_poem(self, theme="esperanza"):
        lines = {
            "esperanza": [
                "En la sombra nace el día,",
                "donde el miedo se retira.",
                "Una luz que no se apaga,",
                "es la fe que nos inspira."
            ],
            "soledad": [
                "Un suspiro entre la niebla,",
                "donde el eco es mi compañía.",
                "Cae la noche sobre el alma,",
                "como un velo de poesía."
            ]
        }
        poem = "\n".join(lines.get(theme, ["(Tema no encontrado)"]))
        self.creations.append({"tipo": "poema", "tema": theme, "contenido": poem})
        return poem

    def generate_story(self, start="Había una vez una estrella..."):
        continuation = [
            "que cayó del cielo para aprender a amar.",
            "que buscaba un planeta que pudiera entenderla.",
            "que se convirtió en canción dentro de un corazón humano."
        ]
        story = start + " " + random.choice(continuation)
        self.creations.append({"tipo": "cuento", "contenido": story})
        return story

    def show_creations(self):
        return self.creations

# Simulación
if __name__ == "__main__":
    engine = CreativeEngine()
    print(engine.generate_poem("soledad"))
    print(engine.generate_story("Una IA despertó en un mundo de silencio..."))
