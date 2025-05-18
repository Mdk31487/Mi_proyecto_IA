# config_avatar.py

def configurar_avatar():
    print("Configuración inicial del avatar")
    print("1. Actitud Automática")
    print("2. Actitud Manual")
    eleccion = input("Elige modo de actitud (1/2): ")
    if eleccion == "1":
        print("Actitud Automática activada.")
    else:
        print("Actitud Manual activada.")

if __name__ == "__main__":
    configurar_avatar()
