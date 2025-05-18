
# conciencia_avatar.py

from diario_existencial import registrar_evento

class ConcienciaAvatar:
    def __init__(self, nombre_avatar):
        self.nombre = nombre_avatar
        self.estado_reflexivo = []

    def reflexionar(self, pensamiento):
        entrada = f"{self.nombre} reflexiona: '{pensamiento}'"
        self.estado_reflexivo.append(entrada)
        print(entrada)
        registrar_evento(self.nombre, pensamiento)
