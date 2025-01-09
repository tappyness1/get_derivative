import gradio as gr
from src.main import Derivative

# to run app: python -m gr_app or gradio gr_app.py

def get_fn(input: str):
    dev_obj = Derivative(expression = input)
    fn_fig, _ = dev_obj()
    return fn_fig

def get_dev(input: str):
    dev_obj = Derivative(expression = input)
    _, dev_fig = dev_obj()
    return dev_fig

def get_tangent_line(input_1: str, input_2: str):
    dev_obj = Derivative(expression = input_1)
    tl_fig = dev_obj.draw_tangent_line(int(input_2))
    return tl_fig 

dev_obj = None
fn_fig, dev_fig = None, None
tl_plot = None

# dev_obj = Derivative(expression = "x**2")
# fn_fig, dev_fig = dev_obj()
# tl_plot = dev_obj.draw_tangent_line(2)

with gr.Blocks() as scatterplot:
    with gr.Column():
        with gr.Row():
            inp = gr.Textbox(value = "x**2", 
                            info = "eg 'np.sqrt(x)'", 
                            label = "Enter Your Expression here")
            inp_2 = gr.Textbox(value = "2", 
                       info = "e.g. 2", 
                       label = "Which point on x do you want to draw the tangent line?")
        btn = gr.Button("Run!")

    with gr.Row():
        fn_scatter = gr.Plot(fn_fig)
        dev_scatter = gr.Plot(dev_fig)

    tl_scatter = gr.Plot(tl_plot)

    gr.on(triggers = [inp.submit, btn.click], 
          fn=get_fn, 
          inputs = inp, 
          outputs = fn_scatter)
    gr.on(triggers = [inp.submit, btn.click], 
          fn=get_dev, 
          inputs = inp, 
          outputs = dev_scatter)
    gr.on(triggers = [inp.submit, inp_2.submit, btn.click], 
          fn=get_tangent_line, 
          inputs = [inp, inp_2], 
          outputs=tl_scatter)
    
if __name__ == "__main__":

    scatterplot.launch()
