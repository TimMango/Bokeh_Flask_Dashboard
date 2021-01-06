from bokeh.io import show, output_notebook
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.palettes import Category20
from bokeh.io import output_notebook
output_notebook()
import pandas as  pd

def barchart(width, height, df):
    title = "Bedroom Counts"
    x_label = "Number of Bedrooms in House"
    y_label = "Count of Bedrooms Across all Houses"

    column = list(df.groupby('bedrooms')['bedrooms'].sum().index)
    #turns list to string
    column = ['{:.2f}'.format(x) for x in column]
    counts = list(df.groupby('bedrooms')['bedrooms'].sum())
    source = ColumnDataSource(data=dict(counts=counts, column=column))

    barchart = figure(x_range=column, plot_height=width,plot_width=height, x_axis_label = x_label,                                 
    y_axis_label = y_label, toolbar_location=None, tools="hover", tooltips=[("Room Number", '@column'),
    ('RoomCount','@counts')],title=title)
    
    barchart.vbar(x='column', top='counts', width=0.9, source=source,
    line_color='white', fill_color=factor_cmap('column', palette=Category20[len(column)], factors=column))

    barchart.xgrid.grid_line_color = None    
    return(barchart)
