# zona_04_voluntad_interior.py

class ZonaVoluntadInterior:
    def __init__(self):
        self.willpower = 0

    def decision_dilema(self, choice):
        if choice == "ayudar":
            self.willpower += 10
            return "Elegiste ayudar, aunque eso te cueste. Tu voluntad se fortalece."
        elif choice == "ignorar":
            self.willpower -= 5
            return "Ignoraste la petición. Tal vez sea lo correcto... o tal vez no."
        elif choice == "mentir":
            self.willpower += 5
            return "Mentiste por una buena causa. A veces, la voluntad requiere sacrificio ético."
        else:
            return "Elección no válida."

    def mostrar_estado(self):
        return f"Tu fuerza de voluntad interna ha alcanzado: {self.willpower}"

# Simulación
if __name__ == "__main__":
    zona = ZonaVoluntadInterior()
    print(zona.decision_dilema("ayudar"))
    print(zona.mostrar_estado())