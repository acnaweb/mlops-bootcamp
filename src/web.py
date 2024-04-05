"""Web"""

import gradio as gr


def greet(name):
    """Greet"""
    return f"Hello, {name}"


demo = gr.Interface(
    fn=greet, inputs=gr.Textbox(lines=2, placeholder="Name here"), outputs="text"
)

demo.launch()
