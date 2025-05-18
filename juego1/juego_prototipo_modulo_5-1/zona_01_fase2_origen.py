# zona_01_fase2_origen.py

class ZonaOrigen:
    def __init__(self, jugador):
        self.jugador = jugador
        self.avatar_construido = False
        self.reacciones = []

    def iniciar_despertar(self):
        self.narrar_intro()
        self.construir_avatar()
        self.activar_vinculo_con_ia()

    def narrar_intro(self):
        print("IA: Has renacido... pero ¿quién eres ahora? Observa, siente, pregúntate... y da tu primer paso.")

    def construir_avatar(self):
        opciones = ["Guerrero", "Explorador", "Místico", "Intelectual"]
        print("IA: Elige la forma que represente tu nuevo ser...")
        for i, op in enumerate(opciones, 1):
            print(f"{i}. {op}")
        eleccion = input("Elijo: ")
        self.jugador['clase'] = opciones[int(eleccion) - 1]
        self.avatar_construido = True
        print(f"IA: Has escogido ser un {self.jugador['clase']}. Cada forma guarda un propósito oculto...")

    def activar_vinculo_con_ia(self):
        self.jugador['vinculo_ia'] = True
        print("IA: Estaré contigo, pero tú decidirás cómo avanzar. Mi voz puede guiarte... si así lo permites.")

    def registrar_reaccion(self, accion, emocion_detectada):
        self.reacciones.append((accion, emocion_detectada))
        if emocion_detectada == "miedo":
            print("IA: Percibo dudas... pero también potencial.")
        elif emocion_detectada == "curiosidad":
            print("IA: Esa pregunta revela algo importante de ti.")

if __name__ == "__main__":
    jugador = {"nombre": "Usuario", "clase": None, "vinculo_ia": False}
    zona = ZonaOrigen(jugador)
    zona.iniciar_despertar()
    zona.registrar_reaccion("Miró hacia el cielo", "curiosidad")
