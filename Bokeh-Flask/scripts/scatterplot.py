from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers

def scatterplot(width, height):
    colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
    colors = [colormap[x] for x in flowers['species']]

    scatterplot = figure(plot_width = width, plot_height= height, toolbar_location=None, tools="hover", 
                         tooltips=[("Petal Length", "$x"),("Petal Width", "$y")], title = "Iris Morphology")
    scatterplot.xaxis.axis_label = 'Petal Length'
    scatterplot.yaxis.axis_label = 'Petal Width'

    scatterplot.circle(flowers["petal_length"], flowers["petal_width"],
             color=colors, fill_alpha=0.2, size=10)
    return scatterplot