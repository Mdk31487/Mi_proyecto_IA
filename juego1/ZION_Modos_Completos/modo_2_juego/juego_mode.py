# juego_mode.py

from zion_sicrr_adapter import SICRRAdapter

def completar_mision(player_id, zona, decision, resultado):
    adapter = SICRRAdapter()
    action = {"zona": zona, "accion": decision, "resultado": resultado}
    adapter.record_action(player_id, "mision", action)
    actitud = adapter.evaluate_player(player_id)
    print(f"Misión completada en {zona}. Actitud evaluada: {actitud}")

if __name__ == "__main__":
    completar_mision("user123", "Bosque del Recuerdo", "Salvó al enemigo", "Éxito pacífico")
