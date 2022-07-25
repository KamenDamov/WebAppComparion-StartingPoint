import gradio as gr

def app(inp):
    pass
text = gr.Textbox(label = "What is your name")

app = gr.Interface(
    fn = app,
    inputs = text,
    outputs = "label",
    label = "What is your name"
)

app.launch()