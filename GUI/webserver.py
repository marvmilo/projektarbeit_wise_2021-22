import dash
from dash import html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
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
         Input("control-start-button", "n_clicks"),
         Input("sorted-acknowleged-button", "n_clicks")]
    )
    def c1(n_intervals, n_start, n_ack):
        return callbacks.control_interact(n_intervals, n_start, n_ack, values)
    
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
    
    #reseting server callback
    @app.callback(
        [Output("control-reset-button-div", "children")],
        [Input("control-reset-button-1", "n_clicks"),
         Input("control-reset-button-2", "n_clicks")]
    )
    def c9(reset1, reset2):
        return callbacks.control_reset(reset1, reset2)
    
    #for updating progressbars on monitoring
    @app.callback(
        [Output("monitoring-tablet-progress", "children"),
         Output("monitoring-container1-progress", "children"),
         Output("monitoring-container2-progress", "children"),
         Output("monitoring-container3-progress", "children")],
        [Input("monitoring-interval", "n_intervals")]
    )
    def c10(n_intervals):
        return callbacks.monitoring_progress(n_intervals, values)
    
    #disabling input while robot is running
    @app.callback(
        [Output("container-1-select", "disabled"),
         Output("container-2-select", "disabled"),
         Output("container-3-select", "disabled"),
         Output("control-reset-button-1", "disabled")],
        [Input("control-interval", "n_intervals")]
    )
    def c11(n_intervals):
        return callbacks.control_disable_input(n_intervals, values)
    
    #stop roboter button
    @app.callback(
        [Output("dummy", "children")],
        [Input("control-stop-button", "n_clicks")]
    )
    def c12(n_stop):
        return callbacks.control_stop_roboter(n_stop, values)
    
    #hide robot not running on monitoring
    @app.callback(
        [Output("monitoring-robot-not-running-div", "style"),
         Output("monitoring-current-ball-div", "style")],
        [Input("monitoring-interval", "n_intervals")]
    )
    def c13(n_intervals):
        return callbacks.hide_robot_not_running(n_intervals, values)
    
    #update current ball on monitoring
    @app.callback(
        [Output("monitoring-current-ball-div", "children")],
        [Input("monitoring-interval", "n_intervals")]
    )
    def c14(n_intervals):
        return callbacks.update_current_ball(n_intervals, values)

    #update picture at monitoring
    @app.callback(
        [Output("monitoring-picture", "children"),
         Output("monitoring-picture", "style")],
        [Input("monitoring-interval", "n_intervals")]
    )
    def c15(n_intervals):
        return callbacks.monitoring_update_picture(n_intervals, values)
    
#run web application
def run(debug = False, port = 80):
    app.run_server(
        debug = debug, 
        host = "0.0.0.0",
        port = port
    )