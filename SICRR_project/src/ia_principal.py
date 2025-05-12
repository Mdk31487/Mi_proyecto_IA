import os
import json
import torch
import tensorflow as tf
import numpy as np
from transformers import AutoModelForCausalLM, AutoTokenizer
from sicrr import SICRR

class IA:
    def __init__(self):
        # Inicializar SICRR
        self.sicrr = SICRR()
        
        # Cargar modelos
        self.modelo_mejorado = self.cargar_modelo_mejorado()
        self.mejor_modelo = self.cargar_mejor_modelo()
        
        # Inicializar tokenizer para el chatbot
        self.tokenizer = AutoTokenizer.from_pretrained("gpt2")
        self.chatbot_model = AutoModelForCausalLM.from_pretrained("gpt2")
        
    def cargar_modelo_mejorado(self):
        try:
            return torch.load('models/modelo_mejorado.pkl')
        except:
            print("No se pudo cargar modelo_mejorado.pkl")
            return None
            
    def cargar_mejor_modelo(self):
        try:
            return tf.keras.models.load_model('models/mejor_modelo.h5')
        except:
            print("No se pudo cargar mejor_modelo.h5")
            return None
            
    def procesar_entrada(self, texto):
        # Procesar con SICRR
        reflexion = self.sicrr.dialogo_interno(texto)
        
        # Procesar con modelos si están disponibles
        if self.modelo_mejorado:
            # Procesar con modelo_mejorado
            pass
            
        if self.mejor_modelo:
            # Procesar con mejor_modelo
            pass
            
        # Generar respuesta con el chatbot
        inputs = self.tokenizer(texto, return_tensors="pt")
        outputs = self.chatbot_model.generate(**inputs, max_length=100)
        respuesta = self.tokenizer.decode(outputs[0])
        
        return respuesta
        
    def interactuar(self, mensaje):
        respuesta = self.procesar_entrada(mensaje)
        self.sicrr.introspeccion(mensaje)
        return respuesta 