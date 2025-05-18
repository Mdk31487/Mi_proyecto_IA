# robot_mode.py

from zion_sicrr_adapter import SICRRAdapter

def diseñar_robot(player_id, design_details):
    adapter = SICRRAdapter()
    adapter.record_action(player_id, "diseño_robot", design_details)
    perfil = adapter.get_personality(player_id)
    print(f"Robot diseñado con detalles: {design_details}. Perfil IA: {perfil}")

if __name__ == "__main__":
    diseñar_robot("user123", {"tipo": "compasivo", "funcion": "asistente"}) 
