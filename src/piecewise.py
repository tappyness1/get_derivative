from __future__ import annotations
from src.main import Derivative
import numpy as np
import plotly.express as px


class Piecewise():
    def __init__(self, func_1: str, func_2: str, point: float, start_stop_num: List[int, int, int] = [-10, 10, 200]):
        start, stop, num = start_stop_num
        x_values = np.linspace(start= start, stop= stop, num = num)
        left_x_values = x_values[x_values < point]
        right_x_values = x_values[x_values >= point]

        self.left_func = Derivative(expression = func_1)
        self.right_func = Derivative(expression = func_2)

        self.left_func.x = left_x_values
        self.right_func.x = right_x_values

        self.left_func()
        self.right_func()
        
        self.piecewise_func_x = x_values
        self.piecewise_func_y = np.append(self.left_func.y, self.right_func.y)
        self.piecewise_func_derivative = np.append(self.left_func.derivative, self.right_func.derivative)

    def _plot_f(self):

        fig = px.scatter(x = self.piecewise_func_x, y = self.piecewise_func_y, title = "Piecewise Function")
        return fig
    
    def _plot_dev(self):
        fig = px.scatter(x = self.piecewise_func_x, y = self.piecewise_func_derivative, title = "Derivative")
        return fig
    
    def plot(self):
        return self._plot_f(), self._plot_dev()

        