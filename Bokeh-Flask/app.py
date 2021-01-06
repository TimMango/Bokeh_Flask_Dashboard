
import flask

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
app = flask.Flask(__name__)

@app.route("/")
def dashboard1():
    from scripts.barchart import barchart
    from scripts.piechart import piechart
    from scripts.multi_barchart import multi_barchart
    from scripts.scatterplot import scatterplot
    from scripts.timeseries import timeseries
    from scripts.datatable import datatable
    import pandas as pd

    df = pd.read_csv('Data/kc_house_data.csv')
    
    barchart = barchart(400,400,df)
    piechart = piechart(400,400,df)
    multiple_barchart = multi_barchart(400,400)
    scatterplot = scatterplot(800,400)
    timeseries = timeseries(800,400)
    datatable = datatable()

    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()

    script, div = components(barchart)
    script2, div2 = components(piechart)
    script3, div3 = components(multiple_barchart)
    script4, div4 = components(scatterplot)
    script5, div5 = components(timeseries)

    render_template = flask.render_template('index.html', datatable=datatable, script=script, 
                      div=div, script2= script2, div2=div2, script3 = script3,
                      div3 = div3, script4=script4, div4=div4, script5 = script5, div5=div5,
                      js_resources=js_resources, css_resources=css_resources)   
    return render_template

if __name__ == "__main__":
    print(__doc__)
    app.run()