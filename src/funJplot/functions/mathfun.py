from ..base import GeometricAnimation
import numpy as np
import plotly.graph_objects as go


class FunctionPlotter2D(GeometricAnimation):
    """Class to plot 2D functions without animation"""
    
    def __init__(self, function, x_range=(-10, 10), num_points=1000, title=None, xlabel=None, ylabel=None):
        """
        Initialize the function plotter
        
        Args:
            function: function to plot (must accept numpy arrays)
            x_range: tuple with (min, max) for the x-axis
            num_points: number of points to generate
            title: chart title
            xlabel: x-axis label
            ylabel: y-axis label
        """
        super().__init__()
        self.function = function
        self.x_range = x_range
        self.num_points = num_points
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel


    def _create_figure(self):
        """Create the figure with the function plot"""
        x_values = np.linspace(self.x_range[0], self.x_range[1], self.num_points)
        y_values = self.function(x_values)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x_values, y=y_values, mode='lines'))
        
        layout = {}
        if self.title:
            layout['title'] = self.title
        if self.xlabel:
            layout['xaxis_title'] = self.xlabel
        if self.ylabel:
            layout['yaxis_title'] = self.ylabel
            
        fig.update_layout(layout)
        return fig



if __name__ =='__main__':
    square= lambda x : x**2
    plot = FunctionPlotter2D(square)
    plot.show()


