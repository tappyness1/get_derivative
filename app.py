import gradio as gr
from src.main import Derivative

# to run app: python -m gr_app or gradio gr_app.py

def get_fn(input: str):
    dev_obj = Derivative(expression = input)
    fn_df, _ = dev_obj()
    return fn_df

def get_dev(input: str):
    dev_obj = Derivative(expression = input)
    _, dev_df = dev_obj()
    return dev_df

dev_obj = Derivative(expression = "x**2")
fn_plot, dev_plot  = dev_obj()

with gr.Blocks() as scatterplot:
    inp = gr.Textbox(value = "x**2", info = "eg 'np.sqrt(x)'", label = "Enter Your Expression here")
    btn = gr.Button("Run!")
    
    with gr.Row():
        fn_scatter = gr.Plot(fn_plot)
        dev_scatter = gr.Plot(dev_plot)

    btn.click(fn=get_fn, inputs=inp, outputs=fn_scatter)
    btn.click(fn=get_dev, inputs=inp, outputs=dev_scatter)
    
if __name__ == "__main__":

    scatterplot.launch()