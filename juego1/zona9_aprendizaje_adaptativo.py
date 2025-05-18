from zion_sicrr_adapter import SICRRManager

# Inicializar la interfaz con SICRR
sicrr = SICRRManager()

# Datos simulados después de completar un reto
usuario_id = "jugador_001"
evento = {
    "zona": "Zona9_Aprendizaje_Adaptativo",
    "accion": "Completó el reto lógico bajo presión",
    "resultado": "Éxito con ayuda mínima",
    "emocion": "concentración"
}

# Registrar experiencia en memoria SICRR
sicrr.registrar_evento(usuario_id, evento)

# Evaluar actitud según el evento
actitud = sicrr.evaluar_actitud(usuario_id, evento)
print(f"Actitud evaluada: {actitud}")

# Actualizar personalidad con los nuevos datos
sicrr.actualizar_personalidad(usuario_id, actitud)
