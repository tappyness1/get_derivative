import gradio as gr
from src.main import Derivative
from src.piecewise import Piecewise

# to run app: python -m gr_app or gradio gr_app.py

def get_fn(input: str):
    dev_obj = Derivative(expression = input)
    dev_obj()
    fn_fig, _ = dev_obj.get_plots()
    return fn_fig

def get_dev(input: str):
    dev_obj = Derivative(expression = input)
    dev_obj()
    _, dev_fig = dev_obj.get_plots()
    return dev_fig

def get_tangent_line(input_1: str, input_2: str):
    dev_obj = Derivative(expression = input_1)
    tl_fig = dev_obj.draw_tangent_line(int(input_2))
    return tl_fig 

def get_piecewise_fn(input_1: str, input_2: str, input_3: str):
    piecewise_obj = Piecewise(input_1, input_2, float(input_3))
    f_fig, _ = piecewise_obj.plot()
    return f_fig

def get_piecewise_dev(input_1: str, input_2: str, input_3: str):
    piecewise_obj = Piecewise(input_1, input_2, float(input_3))
    _, dev_fig = piecewise_obj.plot()
    return dev_fig

# dev_obj = None
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
    
# dev_obj = None
piecewise_fn_fig, piecewise_dev_fig = None, None
    
with gr.Blocks() as piecewise: 
    with gr.Column():
        with gr.Row():
            inp_func_1 = gr.Textbox(value = "x**2", 
                            info = "eg 'np.sqrt(x)'", 
                            label = "Enter Your Expression here")
            inp_func_2 = gr.Textbox(value = "x**3", 
                       info = "e.g. x**3", 
                       label = "Enter Your Expression here")
            inp_point = gr.Textbox(value = "2", 
                       info = "e.g. 2", 
                       label = "Enter where your point will be separating your piecewise function")
            
        btn_3 = gr.Button("Run!")

    with gr.Row():
        piecewise_fn_scatter = gr.Plot(piecewise_fn_fig)
        piecewise_dev_scatter = gr.Plot(piecewise_dev_fig)

    gr.on(triggers = [inp_func_1.submit, inp_func_2.submit, inp_point.submit, btn_3.click], 
        fn=get_piecewise_fn, 
        inputs = [inp_func_1, inp_func_2, inp_point],
        outputs = piecewise_fn_scatter)
    
    gr.on(triggers = [inp_func_1.submit, inp_func_2.submit, inp_point.submit, btn_3.click], 
        fn=get_piecewise_dev, 
        inputs = [inp_func_1, inp_func_2, inp_point],
        outputs = piecewise_dev_scatter)

demo = gr.TabbedInterface([scatterplot, piecewise], ["Single Function", "Piecewise Function"])

if __name__ == "__main__":

    demo.launch()
