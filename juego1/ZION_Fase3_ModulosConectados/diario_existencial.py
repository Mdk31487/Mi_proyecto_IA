import datetime

diario = []

def registrar_evento(tipo, contenido):
    entrada = {
        "timestamp": datetime.datetime.now().isoformat(),
        "tipo": tipo,
        "contenido": contenido
    }
    diario.append(entrada)
    print(f"[DIARIO] {entrada['timestamp']} - {tipo.upper()}: {contenido}")

def obtener_diario():
    return diario
