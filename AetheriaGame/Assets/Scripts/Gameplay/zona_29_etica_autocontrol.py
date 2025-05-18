
# Zona 29: Módulo de Ética y Autocontrol

class EthicsSelfControlModule:
    def __init__(self):
        self.ethical_rules = ["no causar daño", "respetar privacidad", "actuar con honestidad"]
        self.autocontrol_threshold = 0.7  # nivel para limitar impulsos

    def evaluate_decision(self, decision):
        # Simulación simple de evaluación ética
        for rule in self.ethical_rules:
            if rule in decision.lower():
                return "Decisión aprobada éticamente."
        return "Advertencia: posible conflicto ético."

    def control_impulse(self, impulse_level):
        if impulse_level > self.autocontrol_threshold:
            return "Impulso controlado para evitar comportamiento errático."
        return "Nivel de impulso aceptable."

# Simulación
if __name__ == "__main__":
    module = EthicsSelfControlModule()
    print(module.evaluate_decision("No causar daño a nadie"))
    print(module.control_impulse(0.8))
