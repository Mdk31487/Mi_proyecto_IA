import gradio as gr
from src.ia_principal import IA

# Inicializar la IA
ia = IA()

def chat(message, history):
    history = history or []
    response = ia.interactuar(message)
    history.append((message, response))
    return history, history

with gr.Blocks() as demo:
    gr.Markdown("# MDKIA - Sistema Inteligente de Conocimiento y Respuesta")
    
    chatbot = gr.Chatbot()
    state = gr.State()
    
    with gr.Row():
        txt = gr.Textbox(show_label=False, placeholder="Escribe tu mensaje aquí...").style(container=False)
    
    txt.submit(chat, [txt, state], [chatbot, state])
    
if __name__ == "__main__":
    demo.launch() 