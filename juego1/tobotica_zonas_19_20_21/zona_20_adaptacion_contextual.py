# Zona 20: Núcleo de Adaptación Contextual

class ContextAdapter:
    def __init__(self):
        self.context = "default"
        self.history = []

    def update_context(self, new_context):
        self.history.append(self.context)
        self.context = new_context

    def respond(self, input_data):
        return f"[{self.context}] Procesando: {input_data}"

# Simulación
if __name__ == "__main__":
    adapter = ContextAdapter()
    adapter.update_context("terapia")
    print(adapter.respond("¿Cómo te sientes hoy?"))
