from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.embed import components


def multi_barchart(width, height):
    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    years = ['2015', '2016', '2017']

    data = {'fruits' : fruits,
            '2015'   : [2, 1, 4, 3, 2, 4],
            '2016'   : [5, 3, 3, 2, 4, 6],
            '2017'   : [3, 2, 4, 4, 5, 3]}

    palette = ["Green", "Blue", "Orange"]

    # this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
    x = [ (fruit, year) for fruit in fruits for year in years ]
    counts = sum(zip(data['2015'], data['2016'], data['2017']), ()) # like an hstack

    source = ColumnDataSource(data=dict(x=x, counts=counts))

    multi_barchart = figure(x_range=FactorRange(*x), plot_height=width, plot_width=height, title="Fruit Counts by Year",
            toolbar_location=None, tools="hover", tooltips=[("Number of Fruit","@counts")])

    multi_barchart.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
        fill_color=factor_cmap('x', palette=palette, factors=years, start=1, end=2))

    multi_barchart.y_range.start = 0
    multi_barchart.x_range.range_padding = 0.1
    multi_barchart.xaxis.major_label_orientation = 1
    multi_barchart.xgrid.grid_line_color = None
    return multi_barchart