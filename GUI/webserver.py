import dash
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash_bootstrap_templates as dbt
import marvmiloTools as mmt

#import other scripts
from . import callbacks

#declare vals
settings = mmt.json.load("./GUI/settings.json")

#init app
app = dash.Dash(
    title = settings.name,
    meta_tags = [mmt.dash.mobile_optimization],
    external_stylesheets = [dbc.themes.DARKLY]
)
dbt.load_figure_template("darkly")

#init app layout
app.layout = html.Div(
    children = [
        "hello world!",
        html.Br(),
        dbc.Button(
            "Test",
            id = "test-in"
        )
    ],
    id = "test-out"
)

#for init callbacks
def init_callbacks(values, sql):
    #test callback
    @app.callback(
        [Output("test-out", "children")],
        [Input("test-in", "n_clicks")]
    )
    def ct(n_clicks):
        return callbacks.test_callback(values, n_clicks)

#run web application
def run(debug = False):
    app.run_server(debug = debug)

if __name__ == '__main__':
    app.run_server(debug = True)