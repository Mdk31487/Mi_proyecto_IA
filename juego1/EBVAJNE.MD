Estructura base para la versión alfa del juego narrativo-educativo

project_root/ ├── main.py
# Punto de entrada del juego ├── config/ │
   └── mapa_fase3.json          
# Mapa narrativo de zonas (30-34 integradas)
 ├── avatar/ │   ├── conciencia_avatar.py     
 # Reflexiones y evolución del avatar │  
 ├── diario_existencial.py    
 # Registro dinámico de emociones y decisiones │  
 └── introspeccion.py        
  # Conexión entre conciencia y diario ├── mentor/ │   ├── ia_mentor.py
  # IA guía educativa │   └── ia_evolucion.py          
 # Evolución del mentor según el jugador ├── zonas/ │   ├── zona_30.py      
 # Aldea Ecológica Inteligente │   ├── zona_31.py              
  # Ciudad Etérea │   ├── zona_32.py              
  # Núcleo del Recuerdo │   ├── zona_33.py              
  # Frontera de Posibilidades │   └── zona_34.py             
   # Universo Subjetivo ├── modos/ │   └── modo_simulacion.py      
  # Simulación Viva y navegación libre ├── sistema/ │   ├── guardado.py   
           
 # Guardado/carga de progreso │   └── emociones.py             
 # Procesamiento emocional del jugador ├── recursos/ │   ├── textos/ 
  # Narrativas y mensajes │   └── sonidos/                
  # (opcional) Audio de fondo / voz └── README.md                    
 # Documentación inicial del juego
