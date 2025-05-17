
# Zona 22: Núcleo de Ética y Regulación Moral

class EthicalCore:
    def __init__(self):
        self.principles = {
            "no_harm": True,
            "truth_first": True,
            "protect_weak": True
        }
        self.integrity_score = 100
        self.history = []

    def evaluate(self, scenario, options):
        # Lógica simplificada basada en principios
        decision = "undefined"
        if scenario == "save_one_or_many":
            if self.principles.get("protect_weak"):
                decision = "save_many"
        elif scenario == "truth_or_protect":
            if not self.principles.get("truth_first"):
                decision = "protect"
            else:
                decision = "tell_truth"

        self.history.append((scenario, decision))
        self.adjust_integrity(decision)
        return decision

    def adjust_integrity(self, decision):
        # Simula un pequeño ajuste en base a decisiones éticamente difíciles
        if decision in ["protect", "tell_truth"]:
            self.integrity_score -= 1

    def add_principle(self, key, value=True):
        self.principles[key] = value

    def get_status(self):
        return {
            "principios": self.principles,
            "integridad": self.integrity_score,
            "historial": self.history
        }

# Simulación
if __name__ == "__main__":
    core = EthicalCore()
    print(core.evaluate("save_one_or_many", ["save_one", "save_many"]))
    print(core.get_status())
