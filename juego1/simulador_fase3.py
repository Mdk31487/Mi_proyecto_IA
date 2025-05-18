# simulador_fase3.py

from conciencia_avatar import reflexionar
from diario_existencial import registrar_evento, mostrar_diario
from ia_mentor import IA_Mentor
from ia_evolucion import evolucionar_mentor
import json

# Cargar mapa
with open('mapa_fase3.json', 'r') as f:
    mapa = json.load(f)

mentor = IA_Mentor("MentorA", experiencia=10)

def mostrar_zonas():
    print("ZONAS DISPONIBLES EN FASE 3:")
    for zona in mapa["zonas"]:
        print(f"- {zona['nombre']}: {zona['descripcion']}")

def simular_jornada():
    print("\n--- INICIO DE SIMULACIÓN ---")
    mostrar_zonas()
    reflexionar("He sentido conexión con la naturaleza en la Zona30.")
    registrar_evento("Zona30", "Me sentí en paz. Aprendí sobre sostenibilidad.")
    consejo = mentor.dar_consejo()
    print(f"\nConsejo del mentor: {consejo}")
    evolucionar_mentor(mentor)
    mostrar_diario()

if __name__ == "__main__":
    simular_jornada()
