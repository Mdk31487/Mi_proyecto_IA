# zona_02_fase2_jardin_calma.py

class ZonaJardinCalma:
    def __init__(self, jugador):
        self.jugador = jugador
        self.emociones_detectadas = []

    def iniciar_jardin(self):
        print("IA: Este jardín responde a ti. No hables... siente.")
        self.reaccion_flor_reflejo()
        self.interaccion_arbol_juicio()
        self.espejo_eco_interior()

    def reaccion_flor_reflejo(self):
        eleccion = input("Una flor se abre... ¿Qué color eliges observar? (Rojo, Azul, Verde, Negro): ").lower()
        if eleccion == "rojo":
            emocion = "ira"
        elif eleccion == "azul":
            emocion = "calma"
        elif eleccion == "verde":
            emocion = "esperanza"
        elif eleccion == "negro":
            emocion = "temor"
        else:
            emocion = "confusión"
        self.emociones_detectadas.append(emocion)
        print(f"IA: La flor ha mostrado un rastro de {emocion}. Nada es definitivo... solo una señal.")

    def interaccion_arbol_juicio(self):
        print("IA: El árbol quiere saber cómo ves al mundo...")
        respuesta = input("¿El mundo es...? (A. Injusto B. Misterioso C. Un reto D. Hermoso): ").upper()
        juicios = {"A": "negatividad", "B": "curiosidad", "C": "determinación", "D": "gratitud"}
        emocion = juicios.get(respuesta, "neutralidad")
        self.emociones_detectadas.append(emocion)
        print(f"IA: Has mostrado {emocion}... esto será útil para entenderte sin juzgarte.")

    def espejo_eco_interior(self):
        from random import choice
        frases = [
            "El fuego no destruye al que danza con él.",
            "Quien conoce su sombra no le teme a la noche.",
            "Los muros hablan más de quien los construye que de lo que encierran.",
            "Cada emoción es una puerta... no una jaula."
        ]
        resultado = choice(frases)
        print(f"Eco del espejo: "{resultado}"")

if __name__ == "__main__":
    jugador = {"nombre": "Usuario", "clase": "Explorador", "vinculo_ia": True}
    zona = ZonaJardinCalma(jugador)
    zona.iniciar_jardin()
