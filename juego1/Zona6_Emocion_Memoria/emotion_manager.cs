
// emotion_manager.cs
using System;
using System.Collections.Generic;

public class EmotionManager {
    private List<string> emociones = new List<string>();
    public void RegistrarEmocion(string emocion) {
        emociones.Add(emocion);
        // guardar en memoria_emocional.json
    }
    public List<string> GetEmociones() {
        return emociones;
    }
}
