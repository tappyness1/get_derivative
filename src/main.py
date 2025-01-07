from __future__ import annotations
import numpy as np
import plotly.express as px
import pandas as pd

class Derivative:
    def __init__(self, start_stop_num: List[int, int, int] = [-10, 10, 200], expression: str = "x", function_name: str = None):
        start, stop, num = start_stop_num
        
        self.x = np.linspace(start= start, stop= stop, num = num)
        self.function_name = function_name if function_name else expression
        self.expression = expression
        self.h = 0.0001
        self.y = None
        self.delta_y = None

    def _function(self):
        
        def _make_function(x):
            return eval(self.expression)
        
        self.y = _make_function(self.x)
        self.delta_y = _make_function(self.x + self.h)
    
    def _get_derivative(self):  

        if self.delta_y is None or self.y is None:
            raise Exception("Define your y and delta_y first")
        
        self.derivative =  (self.delta_y - self.y) / self.h
        return self.derivative
    
    def _get_f_plot(self):
        return px.scatter(x = self.x, y = self.y, title = self.function_name)
    
    def _get_dev_plot(self):
        return px.scatter(x = self.x, y = self.derivative, title = f"Derivative of {self.function_name}")

    def __call__(self):
        
        self._function()
        self._get_derivative()
        return self._get_f_plot(), self._get_dev_plot()

    
# if __name__== "__main__":
#     dev_obj = Derivative(expression = "1/x")
#     dev_obj()
