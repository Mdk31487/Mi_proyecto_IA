# zona_05_juicio_emocional.py

class ZonaJuicioEmocional:
    def __init__(self):
        self.emociones_superadas = []

    def enfrentar_emocion(self, emocion, respuesta):
        if emocion == "ira" and respuesta == "control":
            self.emociones_superadas.append("ira")
            return "Has canalizado tu ira en determinación. Has superado esta emoción."
        elif emocion == "tristeza" and respuesta == "aceptar":
            self.emociones_superadas.append("tristeza")
            return "Aceptaste la pérdida y creciste. Has superado esta emoción."
        elif emocion == "miedo" and respuesta == "enfrentar":
            self.emociones_superadas.append("miedo")
            return "Te mantuviste firme ante el miedo. Has superado esta emoción."
        else:
            return "La emoción aún te domina. Sigue intentando."

    def resumen(self):
        return f"Emociones superadas: {', '.join(self.emociones_superadas)}"

if __name__ == "__main__":
    zona = ZonaJuicioEmocional()
    print(zona.enfrentar_emocion("ira", "control"))
    print(zona.resumen())
