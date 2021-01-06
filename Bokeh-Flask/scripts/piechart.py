from math import pi
import pandas as pd
from bokeh.io import show
from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
from bokeh.models import LabelSet, ColumnDataSource
from bokeh.io import output_notebook
output_notebook()
import pandas as  pd

def piechart(width, height, df):
    column = list(df.groupby('bedrooms')['bedrooms'].sum().index)
    #turns list to string
    column = ['{:.2f}'.format(x) for x in column]
    value = list(df.groupby('bedrooms')['bedrooms'].sum())

    data = pd.DataFrame({'column': column,
         'value': value})

    data['angle'] = data['value']/data['value'].sum() * 2*pi
    data['color'] = Category20c[len(data)]
    data['percentage'] = data['value']/data['value'].sum() * 100
    data['percentage'] = data['percentage'].astype(int)

    piechart = figure(plot_width=width, plot_height=height, title="Hover Over Pie Chart For Information", toolbar_location=None,
               tools="hover", tooltips=[("Room Count",'@column'), ('Percent of Total', '@percentage%')], x_range=(-0.5, 1.0))

    piechart.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='column', source=data)

    data["value"] = data['value'].astype(str)
    data["value"] = data["value"].str.pad(35, side = "left")
    source = ColumnDataSource(data)
    
    piechart.axis.visible=False
    piechart.grid.grid_line_color = None
    return piechart