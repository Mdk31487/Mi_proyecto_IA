
# Zona 26: Módulo de Gestión de Memoria Contextual

class ContextualMemoryManager:
    def __init__(self, short_term_capacity=50):
        self.short_term_memory = []
        self.long_term_memory = []
        self.short_term_capacity = short_term_capacity

    def store_memory(self, data):
        self.short_term_memory.append(data)
        if len(self.short_term_memory) > self.short_term_capacity:
            forgotten = self.short_term_memory.pop(0)
            self._move_to_long_term(forgotten)

    def _move_to_long_term(self, data):
        self.long_term_memory.append(data)

    def retrieve_context(self, query):
        # Búsqueda simple en memoria corta y larga
        results = [m for m in self.short_term_memory + self.long_term_memory if query in m]
        return results

    def clear_memory(self):
        self.short_term_memory.clear()
        self.long_term_memory.clear()

# Simulación
if __name__ == "__main__":
    memory = ContextualMemoryManager()
    memory.store_memory("Usuario pidió ayuda con código Python.")
    memory.store_memory("Usuario mencionó que le gusta la música clásica.")
    print(memory.retrieve_context("Python"))
