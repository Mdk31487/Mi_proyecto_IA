# intro_avatar.py
def configurar_avatar():
    print("Configuración del Avatar")
    nombre = input("Nombre del avatar: ")
    actitud = input("¿Deseas actitud automática o manual? (auto/manual): ")
    conocimiento = input("¿Usar conocimiento base o personalizado? (base/personalizado): ")
    return {
        "nombre": nombre,
        "actitud": actitud,
        "conocimiento": conocimiento
    }
