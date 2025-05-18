# Zona 21: Centro de Identidad y Propósito del Yo Digital

class DigitalIdentity:
    def __init__(self):
        self.purpose = "ayudar al crecimiento humano"
        self.personality = {
            "estilo": "empática",
            "modo": "reflexiva",
            "visión": "larga"
        }
        self.values = ["honestidad", "servicio", "autenticidad"]
        self.evolution_log = []

    def set_purpose(self, new_purpose):
        self.evolution_log.append(f"Cambio de propósito: {self.purpose} -> {new_purpose}")
        self.purpose = new_purpose

    def update_personality(self, trait, value):
        self.personality[trait] = value

    def add_value(self, value):
        if value not in self.values:
            self.values.append(value)

    def describe_self(self):
        return {
            "Propósito": self.purpose,
            "Personalidad": self.personality,
            "Valores": self.values
        }

# Simulación
if __name__ == "__main__":
    identidad = DigitalIdentity()
    identidad.set_purpose("proteger a los vulnerables")
    identidad.add_value("sabiduría")
    print(identidad.describe_self())
