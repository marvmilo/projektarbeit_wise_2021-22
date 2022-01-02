import dash
from dash import html
from dash.dependencies import Input, Output, State
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
    external_stylesheets = [dbc.themes.DARKLY],
    update_title = False
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
        return callbacks.location_callback(path, values)
    
    #change control interact container
    @app.callback(
        [Output("control-icon-div", "children"),
         Output("control-interact-div", "children")],
        [Input("control-interval", "n_intervals"),
         Input("control-start-button", "n_clicks")]
    )
    def c1(n_intervals, n_start):
        return callbacks.control_interact(n_intervals, n_start, values)
    
    #control containers color callbacks
    @app.callback(
        [Output("container-1-icon-div", "children")],
        [Input("container-1-select", "value")]
    )
    def c2(value):
        return callbacks.control_container_color(value, 1, values)
    @app.callback(
        [Output("container-2-icon-div", "children")],
        [Input("container-2-select", "value")]
    )
    def c3(value):
        return callbacks.control_container_color(value, 2, values)
    @app.callback(
        [Output("container-3-icon-div", "children")],
        [Input("container-3-select", "value")]
    )
    def c4(value):
        return callbacks.control_container_color(value, 3, values)
    
    #control color selects callbacks
    @app.callback(
        [Output("container-1-select", "options")],
        [Input("container-2-select", "value"),
         Input("container-3-select", "value")]
    )
    def c5(container_2_value, container_3_value):
        return callbacks.control_container_select(
            val1 = container_2_value,
            val2 = container_3_value,
        )
    @app.callback(
        [Output("container-2-select", "options")],
        [Input("container-1-select", "value"),
         Input("container-3-select", "value")]
    )
    def c6(container_1_value, container_3_value):
        return callbacks.control_container_select(
            val1 = container_1_value,
            val2 = container_3_value,
        )
    @app.callback(
        [Output("container-3-select", "options")],
        [Input("container-1-select", "value"),
         Input("container-2-select", "value")]
    )
    def c7(container_1_value, container_2_value):
        return callbacks.control_container_select(
            val1 = container_1_value,
            val2 = container_2_value,
        )
    
    #control color selects update callback
    @app.callback(
        [Output("container-1-select", "value"),
         Output("container-2-select", "value"),
         Output("container-3-select", "value")],
        [Input("control-interval", "n_intervals")],
        [State("control-container-1-color", "style"),
         State("control-container-2-color", "style"),
         State("control-container-3-color", "style")]
    )
    def c8(n_intervals, style1, style2, style3):
        return callbacks.control_container_color_update(n_intervals, values, style1, style2, style3)
    
#run web application
def run(debug = False, port = 80):
    app.run_server(
        debug = debug, 
        host = "0.0.0.0",
        port = port
    )