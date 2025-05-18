# actitudes_usuario.py

class EvaluadorActitud:
    def __init__(self):
        self.perfil = {
            "niño": 0,
            "joven": 0,
            "adulto": 0,
            "tercer_despertar": 0
        }

    def registrar_accion(self, tipo, valor=1):
        if tipo in self.perfil:
            self.perfil[tipo] += valor

    def obtener_actitud_predominante(self):
        return max(self.perfil, key=self.perfil.get)

    def mostrar_perfil(self):
        return self.perfil

# Ejemplo de uso
if __name__ == "__main__":
    eval = EvaluadorActitud()
    eval.registrar_accion("niño")
    eval.registrar_accion("adulto", 2)
    print("Perfil:", eval.mostrar_perfil())
    print("Actitud predominante:", eval.obtener_actitud_predominante())
