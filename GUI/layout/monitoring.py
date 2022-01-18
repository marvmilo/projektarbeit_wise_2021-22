import marvmiloTools as mmt
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

#for getting color dict of values
def get_color_dict(values):
    dictionary = dict()
    #getting containers
    for i in [100, 200, 300]:
        #getting color
        try:
            color = [c for c in values.colors.keys() if values.colors[c].container_num == i][0]
        except IndexError:
            color = None
        #getting done
        try:
            done = values.colors[color].sorted
        except KeyError:
            done = 0
        #getting total
        try:
            total = values.colors[color].total
        except KeyError:
            total = 0
        #set hex color
        if color == "red":
            hex_color = "#dc3545"
        elif color == "green": 
            hex_color = "#198754"
        elif color == "yellow":
            hex_color = "#ffc107"
        else:
            hex_color = None
        #set text
        try:
            text = f"{int(done/total*100)}%"
        except ZeroDivisionError:
            text = "0%"
        
        container = f"container{int(i/100)}"
        dictionary[container] = {
            "total": total,
            "bar": {
                "color": hex_color,
                "done": done,
                "text": text
            }
        }
    #getting tablet
    amount_red = values.colors.red.total - values.colors.red.sorted
    amount_green = values.colors.green.total - values.colors.green.sorted
    amount_yellow = values.colors.yellow.total - values.colors.yellow.sorted
    dictionary["tablet"] = {
        "total": values.ball.total,
        "remaining": values.ball.total - values.ball.done,
        "bars": [
            {"color": "#dc3545", "done": amount_red, "text": amount_red},
            {"color": "#198754", "done": amount_green, "text": amount_green},
            {"color": "#ffc107", "done": amount_yellow, "text": amount_yellow},
        ]
    }
    dictionary = mmt.dictionary.toObj(dictionary)
    return dictionary

#for displaying container levels
def progress_level(bars, current, total, total_sum = False):
    progress_bars = list()
    
    if total_sum:
        form_text = f"Total: {total}"
    else:
        form_text = f"Noch {total-current} übrig"
    
    for bar in bars:
        try:
            progress = bar["done"]/total*100
        except ZeroDivisionError:
            progress = 0
        progress_bars.append(
            dbc.Progress(
                html.Div(
                    bar["text"],
                    style = {
                        "fontWeight": "bold",
                        "fontSize": "2rem"
                    }
                ),
                value = progress,
                color = bar["color"],
                bar = True
            )
        )
    return html.Div(
        children = [
            html.Div(
                progress_bars,
                style = {"height": "4rem"},
                className = "progress"
            ),
            dbc.FormText(
                form_text, 
                color = "#aaaaaa",
                style = {"fontSize": "1rem"}
            ),
        ]
    )
    
#for displaing current ball
def current_ball(color = "...", x = "...", y = "..."):
    if color == "red":
        hex_color = "#dc3545"
    elif color == "green":
        hex_color = "#198754"
    elif color == "yellow":
        hex_color = "#ffc107"
    else:
        hex_color = "#444444"
    
    return html.Div(
        children = [
            html.Div(
                html.H2(
                    "Aktuelle Kugel:",
                    style = {"fontWeight": "bold"}
                ),
                style = mmt.dash.flex_style()
            ),
            html.Div(
                dbc.Alert(
                    html.H1(
                        color, 
                        style = {
                            "fontWeight": "bold",
                            "textAlign": "center"
                        },
                    ),
                    color = hex_color,
                    style = mmt.dash.flex_style({
                        "borderRadius": "6rem",
                        "height": "12rem",
                        "width": "12rem",
                    })
                ),
                style = mmt.dash.flex_style()
            ),
            html.Div(
                dbc.Row(
                    children = [
                        dbc.Col(
                            html.H3("X:", style = {"fontWeight": "bold"}),
                            width = "auto"
                        ),
                        dbc.Col(
                            html.H3(x),
                            width = "auto"
                        ),
                        dbc.Col(width = 1),
                        dbc.Col(
                            html.H3("Y:", style = {"fontWeight": "bold"}),
                            width = "auto"  
                        ),
                        dbc.Col(
                            html.H3(y),
                            width = "auto"
                        )
                    ]
                ),
                style = mmt.dash.flex_style()
            )
        ]
    )

#for displaing robot not running
def robot_not_running(button_color = "secondary"):
    return html.Div([
        dbc.Row(
            children = [
                dbc.Col(
                    html.Div(
                        style = {
                            "backgroundImage": "url(/assets/info_24dp.svg)",
                            "height":"75px",
                            "width":"75px",
                            "backgroundSize": "cover"
                        }
                    ),
                    width = "auto"
                ),
                dbc.Col(
                    html.H4(
                        "Robot läuft gerade nicht. Klicke hier um neu zu starten:",
                        style = {
                            "fontWeight": "bold",
                            "width": "200px"
                        }
                    ),
                    width = "auto"
                )
            ],
            justify = "center"
        ),
        html.Div(style = {"height": "0.5rem"}),
        html.Div(
            html.A(
                dbc.Button(
                    "Starte Roboter!",
                    style = {
                        "fontWeight": "bold",
                        "fontSize": "1.5rem",
                        "height": "5rem",
                        "width": "12.5rem",
                    },
                    color = button_color
                ),
                href = "/control"
            ),
            style = mmt.dash.flex_style()
        )
    ])

#for creating style of picture
def picture_style(additional = {}):
    style = mmt.dash.flex_style({
        "width": "100%",
        "backgroundColor": "#444444",
        "borderRadius": "0.5rem"
    })
    style = style | additional
    return mmt.dash.flex_style(style)

#containers content
def content(values):
    color_dict = get_color_dict(values)
    if values.robot.movementclear:
        robot_not_running_style = {"display": "none"}
        current_ball_style = None
    else:
        robot_not_running_style = None
        current_ball_style = {"display": "none"}
    
    return html.Div(
        children = [
            html.Div(
                children = robot_not_running(),
                id = "monitoring-robot-not-running-div",
                style = robot_not_running_style
            ),
            html.Br(),
            html.Div(
                children = current_ball(),  
                id = "monitoring-current-ball-div",
                style = current_ball_style
            ),
            html.Br(),
            html.H3(
                "Tablett:",
                style = {"fontWeight": "bold"}
            ),
            html.Div(
                progress_level(
                    bars = color_dict.tablet.bars,
                    current = color_dict.tablet.remaining,
                    total = color_dict.tablet.total
                ),
                id = "monitoring-tablet-progress"
            ),
            html.Br(),
            html.Div(
                html.Div(
                    style = {
                        "backgroundImage": "url(/assets/keyboard_double_arrow_down_24dp.svg)",
                        "height":"100px",
                        "width":"100px",
                        "backgroundSize": "cover"
                    }
                ),
                style = mmt.dash.flex_style()
            ),
            html.H3(
                "Container 1:",
                style = {"fontWeight": "bold"}
            ),
            html.Div(
                progress_level(
                    bars = [color_dict.container1.bar],
                    current = color_dict.container1.bar.done,
                    total = color_dict.container1.total,
                ),
                id = "monitoring-container1-progress"
            ),
            html.Br(),
            html.H3(
                "Container 2:",
                style = {"fontWeight": "bold"}
            ),
            html.Div(
                progress_level(
                    bars = [color_dict.container2.bar],
                    current = color_dict.container2.bar.done,
                    total = color_dict.container2.total,
                ),
                id = "monitoring-container2-progress"
            ),
            html.Br(),
            html.H3(
                "Container 3:",
                style = {"fontWeight": "bold"}
            ),
            html.Div(
                progress_level(
                    bars = [color_dict.container3.bar],
                    current = color_dict.container3.bar.done,
                    total = color_dict.container3.total,
                ),
                id = "monitoring-container3-progress"
            ),
            html.Br(),
            html.Br(),
            html.H2("Kamera Erkennung:"),
            html.Div(
                dbc.Spinner(),
                id = "monitoring-picture",
                style = picture_style()
            ),
            dcc.Interval(id = "monitoring-interval")
        ]
    )