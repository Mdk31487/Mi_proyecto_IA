
# Zona 25: Centro de Interacción Multimodal

class MultimodalInteractionCenter:
    def __init__(self):
        self.active_channels = {"text": True, "voice": False, "image": False, "gesture": False}

    def receive_input(self, input_data, channel):
        if channel not in self.active_channels or not self.active_channels[channel]:
            return f"Canal {channel} no activo."
        return self.process_input(input_data, channel)

    def process_input(self, input_data, channel):
        if channel == "text":
            return f"Procesando texto: {input_data}"
        elif channel == "voice":
            return f"Procesando voz: {input_data}"
        elif channel == "image":
            return f"Procesando imagen con datos: {input_data}"
        elif channel == "gesture":
            return f"Procesando gesto: {input_data}"
        else:
            return "Canal desconocido."

    def set_active_channels(self, channels_status):
        self.active_channels.update(channels_status)

# Simulación
if __name__ == "__main__":
    mic = MultimodalInteractionCenter()
    mic.set_active_channels({"text": True, "voice": True})
    print(mic.receive_input("Hola, ¿cómo estás?", "text"))
    print(mic.receive_input("Audio data stream", "voice"))
    print(mic.receive_input("Imagen data", "image"))
