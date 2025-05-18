from diario_existencial import registrar_evento

class IAMentor:
    def __init__(self):
        self.consejos = []

    def dar_consejo(self, situacion):
        consejo = f"Ante {situacion}, recuerda mantener la calma y aprender."
        self.consejos.append(consejo)
        registrar_evento("consejo_ia", consejo)
        return consejo
