from __future__ import annotations
import numpy as np
import plotly.express as px
import math
import plotly.graph_objects as go

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

    def _plot_f(self):

        fig = px.scatter(x = self.x, y = self.y, title = self.function_name)
        return fig

    def _plot_derivative(self):

        fig = px.scatter(x = self.x, y = self.derivative, title = f"Derivative of {self.function_name}")
        return fig

    def get_slope_one_point(self, x):
        # using x and y, obtain the slope
        # y = eval(self.expression)
        math_expression = self.expression.replace("np", "math")

        def _make_function(x): 
            return eval(math_expression)
        
        y = _make_function(x)
        delta_y = _make_function(x + self.h)
        slope = (delta_y - y) / self.h

        return slope, y

    def get_tangent_line_vals(self, x):
        slope, y = self.get_slope_one_point(x)
        tangent_line_y_vals = slope * (self.x - x) + y
        return y, tangent_line_y_vals

    def draw_tangent_line(self, x):
        y, tl_y_vals = self.get_tangent_line_vals(x)

        title = f"Tangent line at point({x},{round(y, 2)}) of {self.function_name}"

        if self.y is None:
            self._function()

        fig = go.Figure()
        fig.update_layout(title = title)
        fig.add_trace(go.Scatter(x = self.x, y = tl_y_vals, name = f"Tangent Line at ({x},{round(y, 2)})"))
        fig.add_trace(go.Scatter(x = self.x, y = self.y, name = self.function_name))

        return fig

    def get_plots(self): 
        return self._plot_f(), self._plot_derivative()

    def __call__(self):
        
        self._function()
        self._get_derivative()
