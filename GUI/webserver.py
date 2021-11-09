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
app.layout = layout.structure(settings.name, layout.main_content)

#for init callbacks
def init_callbacks(values, sql):
    pass
    # #test callback
    # @app.callback(
    #     [Output("test-out", "children")],
    #     [Input("test-in", "n_clicks")]
    # )
    # def ct(n_clicks):
    #     return callbacks.test_callback(values, n_clicks)

#run web application
def run(debug = False):
    app.run_server(debug = debug)