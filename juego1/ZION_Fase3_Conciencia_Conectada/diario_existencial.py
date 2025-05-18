
# diario_existencial.py

import datetime

def registrar_evento(nombre_avatar, reflexion):
    tiempo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diario_existencial.log", "a") as f:
        f.write(f"[{tiempo}] {nombre_avatar}: {reflexion}\n")
