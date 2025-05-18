# Aetheria Game

## Descripción
Aetheria es un juego de aventura y acción desarrollado en Unity. Este proyecto incluye soporte completo para plataformas móviles.

## Requisitos del Sistema

### PC
- Windows 10/11, macOS 10.15+, o Linux
- Unity 2022.3 LTS o superior
- 8GB RAM mínimo
- GPU compatible con DirectX 11 o OpenGL 3.3+

### Android
- Android 7.0 (API 24) o superior
- 2GB RAM mínimo
- GPU compatible con OpenGL ES 3.0

## Configuración del Proyecto

1. Clona el repositorio:
```bash
git clone https://github.com/tu-usuario/aetheria-game.git
```

2. Abre el proyecto en Unity 2022.3 LTS o superior

3. Instala las dependencias necesarias:
   - Input System Package
   - TextMeshPro
   - Cinemachine
   - Post Processing

## Compilación para Android

### Requisitos Previos
1. Instalar Android Studio
2. Instalar JDK (Java Development Kit) 11 o superior
3. Configurar las variables de entorno:
   - JAVA_HOME
   - ANDROID_HOME
   - ANDROID_SDK_ROOT

### Pasos para Compilar
1. En Unity, ve a File > Build Settings
2. Selecciona Android como plataforma
3. Configura los siguientes ajustes:
   - Player Settings:
     - Company Name: Tu nombre o empresa
     - Product Name: Aetheria
     - Package Name: com.tunombre.aetheria
     - Minimum API Level: Android 7.0 (API 24)
     - Target API Level: Android 13.0 (API 33)
   - Graphics:
     - Color Space: Linear
     - Auto Graphics API: Desactivado
     - Graphics APIs: OpenGLES3
   - Other Settings:
     - Scripting Backend: IL2CPP
     - Target Architectures: ARM64
     - Scripting Define Symbols: MOBILE_PLATFORM

4. Configura la firma del APK:
   - Crea un keystore o usa uno existente
   - Configura la contraseña y alias
   - Guarda el keystore en una ubicación segura

5. Haz clic en "Build" o "Build and Run"

### Optimizaciones para Móvil
- Calidad de texturas reducida
- Shaders optimizados
- Sistema de LOD (Level of Detail)
- Culling de objetos
- Física simplificada
- Controles táctiles personalizables

## Estructura del Proyecto

### Carpetas Principales
- **Assets/**
  - **Scripts/**: Contiene todos los scripts del juego
    - **Managers/**: Sistemas principales del juego
    - **Test/**: Pruebas unitarias
    - **UI/**: Scripts de interfaz de usuario
    - **StatusEffects/**: Sistema de efectos de estado
    - **Player/**: Scripts del jugador
    - **Scene/**: Gestión de escenas
    - **Audio/**: Sistema de audio
    - **Gameplay/**: Mecánicas de juego
    - **IA/**: Comportamiento de enemigos
    - **Mobile/**: Scripts para móviles
  - **Sprites/**: Recursos gráficos
  - **Prefabs/**: Prefabs reutilizables
  - **Scenes/**: Escenas del juego
  - **Resources/**: Recursos cargados en tiempo de ejecución
  - **Audio/**: Archivos de sonido
  - **Materials/**: Materiales del juego
  - **UI/**: Elementos de interfaz de usuario

### Sistemas Implementados
1. **Sistema de UI**
   - Paneles dinámicos con fade
   - Sistema de diálogos
   - Notificaciones
   - Tooltips
   - Efectos de estado

2. **Sistema de Efectos de Estado**
   - Quemadura
   - Aturdimiento
   - Sistema extensible
   - Pruebas unitarias

3. **Sistema de Diálogos**
   - Diálogos con elecciones
   - Retratos de personajes
   - Sistema de eventos

4. **Sistema de Escenas**
   - Carga asíncrona
   - Transiciones
   - Gestión de zonas

5. **Sistema de Eventos**
   - Eventos predefinidos
   - Sistema de suscripción
   - Manejo de errores
   - Eventos para todos los sistemas

6. **Sistema de Guardado**
   - Guardado de datos del juego
   - Carga de partidas
   - Sistema de autoguardado
   - Manejo de errores

7. **Sistema de Configuración**
   - Configuración de gráficos
   - Configuración de audio
   - Configuración de controles
   - Configuración de juego
   - Persistencia de configuración

## Requisitos
- Unity 2022.3 LTS o superior
- Visual Studio 2022 o JetBrains Rider

## Instalación
1. Clonar el repositorio
2. Abrir el proyecto en Unity
3. Abrir la escena principal en `Assets/Scenes/MundoTierra/Modulo2.unity`

## Uso
### Controles
- WASD: Movimiento
- Espacio: Saltar
- E: Interactuar
- ESC: Menú de pausa

### Desarrollo
1. Crear una nueva rama para cada característica
2. Seguir las convenciones de código
3. Documentar cambios significativos
4. Realizar pruebas antes de hacer merge

## Convenciones de Código
- Usar PascalCase para clases y métodos
- Usar camelCase para variables
- Documentar métodos públicos
- Seguir el patrón de diseño Singleton para managers
- Implementar pruebas unitarias para nuevos sistemas

## Contribución
1. Fork el proyecto
2. Crear una rama para tu característica
3. Commit tus cambios
4. Push a la rama
5. Abrir un Pull Request

## Licencia
Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto
- Desarrollador: [Tu Nombre]
- Email: [Tu Email]
- GitHub: [Tu GitHub]

Link del proyecto: [https://github.com/tu-usuario/aetheria-game](https://github.com/tu-usuario/aetheria-game) 