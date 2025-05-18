# zona_03_fase2_espejismo_conflicto.py

class ZonaEspejismoConflicto:
    def __init__(self, jugador):
        self.jugador = jugador
        self.reaccion = None

    def iniciar_espejismo(self):
        print("...El viento cambia. Algo se mueve entre las ruinas.")
        print("Una figura oscura se acerca... no ataca, pero te habla.")
        self.dialogo_guardian()
        self.eleccion_jugador()
        self.resultado()

    def dialogo_guardian(self):
        print("Sombra del Guardián: "¿Quién eres tú para pensar que mereces este poder?"")
        print("Sombra del Guardián: "Demuestra si tu voluntad está guiada por el ego o por el equilibrio."")

    def eleccion_jugador(self):
        print("\nOpciones:")
        print("A. Enfrentarlo con poder.")
        print("B. Dialogar con calma.")
        print("C. Permanecer en silencio y observar.")
        print("D. Huir de la situación.")
        eleccion = input("¿Qué haces? (A/B/C/D): ").upper()
        self.reaccion = eleccion

    def resultado(self):
        if self.reaccion == "A":
            print("Tu decisión de atacar revela impaciencia... aunque el poder responde, el entorno se oscurece.")
        elif self.reaccion == "B":
            print("La sombra sonríe... tu empatía calma el conflicto. El desierto se vuelve un oasis.")
        elif self.reaccion == "C":
            print("Tu silencio permite entender. La sombra se desvanece, dejando una llave de luz.")
        elif self.reaccion == "D":
            print("Huir no es cobardía si se reconoce como estrategia. La sombra desaparece, pero volverá.")
        else:
            print("No hacer nada también es una elección. El entorno permanece incierto.")

if __name__ == "__main__":
    jugador = {"nombre": "Usuario", "clase": "Explorador", "vinculo_ia": True}
    zona = ZonaEspejismoConflicto(jugador)
    zona.iniciar_espejismo()
