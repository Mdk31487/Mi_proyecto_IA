from diario_existencial import registrar_evento

class ConcienciaAvatar:
    def __init__(self, nombre_avatar):
        self.nombre = nombre_avatar
        self.reflexiones = []

    def reflexionar(self, pensamiento):
        mensaje = f"{self.nombre} reflexiona: '{pensamiento}'"
        self.reflexiones.append(pensamiento)
        registrar_evento("reflexion", mensaje)
        return mensaje
