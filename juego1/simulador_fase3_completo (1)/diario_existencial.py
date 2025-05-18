diario = []

def registrar_evento(zona, emocion):
    entrada = f"En {zona} sentí: {emocion}"
    diario.append(entrada)
    print(f"[Diario] {entrada}")

def mostrar_diario():
    return "\n".join(diario)