# zona_11_interaccion_ia.py

class SocialInteractionEngine:
    def __init__(self):
        self.user_profile = {}
        self.scenario = "plaza"
        self.emotion_level = "neutral"
        self.progress_log = []

    def detect_emotion(self, user_input):
        if "enojo" in user_input or "frustrado" in user_input:
            self.emotion_level = "angry"
        elif "triste" in user_input:
            self.emotion_level = "sad"
        else:
            self.emotion_level = "neutral"

    def interact(self, user_input):
        self.detect_emotion(user_input)
        if self.emotion_level == "angry":
            return "Parece que estás molesto. ¿Quieres practicar técnicas para calmarte?"
        elif self.emotion_level == "sad":
            return "Veo que te sientes triste. Aquí estoy para escucharte."
        else:
            return "¿Sobre qué te gustaría conversar hoy?"

if __name__ == "__main__":
    engine = SocialInteractionEngine()
    print(engine.interact("Estoy muy frustrado con este juego"))
