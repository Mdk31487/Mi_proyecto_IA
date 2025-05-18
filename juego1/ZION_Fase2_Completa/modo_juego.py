# modo_juego.py

def modo_juego():
    print("Selecciona tu modo de juego:")
    print("1. Guiado por IA")
    print("2. Juego Libre")
    print("3. Modo Maestro")

    eleccion = input("Elige (1/2/3): ")
    if eleccion == "1":
        print("Modo Guiado por IA seleccionado.")
    elif eleccion == "2":
        print("Modo Juego Libre seleccionado.")
    elif eleccion == "3":
        print("Modo Maestro seleccionado.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    modo_juego()
