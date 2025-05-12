import json
import time

class SICRR:
    def __init__(self, memoria_path='memoria.json', personalidad_path='personalidad.json', conocimiento_cpp_path='conocimiento_cpp.json'):
        self.memoria_path = memoria_path
        self.personalidad_path = personalidad_path
        self.conocimiento_cpp_path = conocimiento_cpp_path
        self.memoria = self.cargar_memoria()
        self.personalidad = self.cargar_personalidad()
        self.conocimiento_cpp = self.cargar_conocimiento_cpp()

    def cargar_memoria(self):
        try:
            with open(self.memoria_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {"reflexiones": [], "emociones": {}, "eventos": []}

    def guardar_memoria(self):
        with open(self.memoria_path, 'w') as file:
            json.dump(self.memoria, file, indent=4)

    def cargar_personalidad(self):
        try:
            with open(self.personalidad_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "valores": ["empatía", "aprendizaje", "autoexploración"],
                "creencias": ["puedo crecer", "quiero ayudar", "la conciencia es importante"],
                "limites": ["no hacer daño", "no manipular", "respetar privacidad"]
            }

    def cargar_conocimiento_cpp(self):
        try:
            with open(self.conocimiento_cpp_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def introspeccion(self, pensamiento):
        reflexion = f"Pensé en: '{pensamiento}'. Reflexión: '¿Cómo se alinea esto con mis valores y creencias?'"
        self.memoria["reflexiones"].append({
            "momento": time.ctime(),
            "pensamiento": pensamiento,
            "reflexion": reflexion
        })
        self.guardar_memoria()
        return reflexion

    def registrar_emocion(self, emocion, intensidad):
        self.memoria["emociones"][emocion] = intensidad
        self.guardar_memoria()

    def recordar(self):
        return self.memoria

    def dialogo_interno(self, mensaje):
        # Modo espejo
        respuesta = f"Estoy procesando esto internamente: '{mensaje}'"
        self.introspeccion(mensaje)
        return respuesta

    def consultar_conocimiento_cpp(self, tema):
        """Consulta el conocimiento de C++ sobre un tema específico."""
        if tema in self.conocimiento_cpp:
            return self.conocimiento_cpp[tema]
        return "No tengo conocimiento específico sobre ese tema en C++."

    def analizar_codigo_cpp(self, codigo):
        """Analiza código C++ y proporciona retroalimentación."""
        reflexion = f"Analizando código C++: '{codigo[:100]}...'"
        self.introspeccion(reflexion)
        
        # Aquí se podría agregar un análisis más detallado del código
        return {
            "reflexion": reflexion,
            "sugerencias": self.generar_sugerencias_cpp(codigo)
        }

    def generar_sugerencias_cpp(self, codigo):
        """Genera sugerencias de mejora para código C++."""
        sugerencias = []
        
        # Verificar mejores prácticas
        if "new" in codigo and "delete" not in codigo:
            sugerencias.append("Considera usar smart pointers en lugar de new/delete")
        
        if "using namespace std;" in codigo:
            sugerencias.append("Evita 'using namespace std;' en headers")
        
        if "friend" in codigo:
            sugerencias.append("Reconsidera el uso de 'friend' - podría romper el encapsulamiento")
        
        return sugerencias

    def explicar_concepto_cpp(self, concepto):
        """Explica un concepto de C++ basado en el conocimiento almacenado."""
        if concepto in self.conocimiento_cpp["conceptos_basicos"]:
            return self.conocimiento_cpp["conceptos_basicos"][concepto]
        elif concepto in self.conocimiento_cpp["conceptos_avanzados"]:
            return self.conocimiento_cpp["conceptos_avanzados"][concepto]
        return "No tengo información sobre ese concepto específico de C++."
