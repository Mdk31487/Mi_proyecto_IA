from ia_mentor import IAMentor

class IAMentorEvolutivo(IAMentor):
    def __init__(self):
        super().__init__()
        self.nivel_experiencia = 0

    def adaptar_consejo(self, retroalimentacion):
        self.nivel_experiencia += 1
        consejo = f"Consejo adaptado tras feedback: '{retroalimentacion}'. Nivel IA: {self.nivel_experiencia}"
        self.consejos.append(consejo)
        return consejo
