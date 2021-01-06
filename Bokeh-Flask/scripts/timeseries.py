import numpy as np
import pandas as pd
from bokeh.layouts import gridplot
from bokeh.plotting import figure
from bokeh.models import HoverTool
from bokeh.models import LabelSet, ColumnDataSource
from bokeh.sampledata.stocks import AAPL, GOOG

def timeseries(width, height):
    data = pd.DataFrame({'Date_AAPL': AAPL['date'][-2148:], 'AAPL_Price': AAPL['adj_close'][-2148:],
                     'Date_GOOG': GOOG['date'], 'GOOG_Price': GOOG['adj_close']})

    data['Date_AAPL'] = np.array(data['Date_AAPL'], dtype=np.datetime64)
    data['Date_GOOG'] = np.array(data['Date_GOOG'], dtype=np.datetime64)
    data["DateString"] = data["Date_AAPL"].dt.strftime("%Y-%m-%d")

    cds = ColumnDataSource(data)

    timeseries = figure(plot_width = width, plot_height= height,x_axis_type="datetime", title="Stock Closing Prices",
                        toolbar_location=None, tools="hover", tooltips=[("Date", "@DateString"),("Price", "$y")])

    timeseries.grid.grid_line_alpha=0.3
    timeseries.xaxis.axis_label = 'Date'
    timeseries.yaxis.axis_label = 'Price'

    ##This isjust a list for the date and a list for the price
    timeseries.line("Date_AAPL", "AAPL_Price", color = "Red", alpha = 0.5, source = cds, legend_label = "AAPL")
    timeseries.line("Date_GOOG", "GOOG_Price", color = "Blue", alpha = 0.5, source = cds, legend_label = "GOOG")
    timeseries.legend.location = "top_left"
    return timeseries