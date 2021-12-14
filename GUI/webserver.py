import dash
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_bootstrap_templates as dbt
import marvmiloTools as mmt

#import other scripts
from . import callbacks
from . import layout

#declare vals
settings = mmt.json.load("./GUI/settings.json")

#init app
app = dash.Dash(
    title = settings.name,
    meta_tags = [mmt.dash.mobile_optimization],
    external_stylesheets = [dbc.themes.DARKLY]
)
dbt.load_figure_template("darkly")
app.layout = layout.structure(settings.name)

#for init callbacks
def init_callbacks(values, sql):
    
    #navbar toggler callback
    @app.callback(*mmt.dash.nav.callback_args)
    def cn(n, is_open):
        return mmt.dash.nav.callback_function(n, is_open)
    
    #page location callback
    @app.callback(
        Output("main-content", "children"),
        Input("url", "pathname")
    )
    def cl(path):
        if path == "/control":
            return layout.control.content
        elif path == "/containers":
            return layout.containers.content
        elif path == "/history":
            return layout.history.content
        else:
            return layout.home.content

#run web application
def run(debug = False, port = 80):
    app.run_server(
        debug = debug, 
        host = "0.0.0.0",
        port = port
    )