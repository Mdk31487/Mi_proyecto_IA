# avatar_mode.py

from zion_sicrr_adapter import SICRRAdapter

def social_interaction(player_id, content):
    adapter = SICRRAdapter()
    adapter.record_action(player_id, "publicacion", {"content": content})
    evaluation = adapter.evaluate_player(player_id)
    print(f"Interacción registrada. Evaluación social: {evaluation}")

if __name__ == "__main__":
    social_interaction("user123", "Compartiendo mis reflexiones en Zion Social...")
