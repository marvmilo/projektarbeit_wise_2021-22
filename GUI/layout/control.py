import marvmiloTools as mmt
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc

#for displaying icon
def icon(icon, text, color):
    return html.Div(
        children = [
            html.Div(
                html.Div(
                    style = {
                        "backgroundImage": icon,
                        "height":"200px",
                        "width":"200px",
                        "backgroundSize": "cover"
                    }
                ),
                style = mmt.dash.flex_style()
            ),
            html.Div(
                html.H2(
                    text,
                    style = {
                        "fontWeight": "bold",
                        "color": color,
                        "textAlign": "center"
                    }
                ),
                style = mmt.dash.flex_style()
            )
        ]
    )

#main control button
def control_button(children, color, fontsize, id = "control-button"):
    return html.Div(
        dbc.Button(
            children,
            color = color,
            id = id,
            style = {
                "fontWeight": "bold",
                "fontSize": fontsize,
                "height": "7.5rem",
                "width": "20rem",
            }
        ),
        style = mmt.dash.flex_style()
    )
    
#container icons
def container_icon(container_number, icon, color):
    return html.Div(
        children = [
            html.Div(
                html.Div(
                    style = {
                        "backgroundImage": icon,
                        "height":"150px",
                        "width":"150px",
                        "backgroundSize": "cover"
                    }
                ),
                style = mmt.dash.flex_style()
            ),
            html.Div(
                html.H2(
                    f"Container {container_number}",
                    style = {
                        "fontWeight": "bold",
                        "textAlign": "center",
                        "color": color
                    },
                    id = f"control-container-{container_number}-color"
                ),
                style = mmt.dash.flex_style()
            ),
            html.Br()
        ]
    )

#color radios for container
def color_select(id, value, options = None):
    if not options:
        options = [
            {"label": "Rot", "value": "red"},
            {"label": "Grün", "value": "green"},
            {"label": "Gelb", "value": "yellow"},
            {"label": "Keine", "value": "none"}
        ]
    
    return html.Div(
        children = [
            dbc.InputGroup(
                children = [
                    dbc.InputGroupText("Kugeln:"),
                    dbc.Select(
                        id = f"{id}-select",
                        options = options,
                        value = value
                    )
                ]
            )
        ]
    )
  

#control content
def content(values):
    #prepare page
    container_colors = {str(i+1): "none" for i in range(3)}
    for color in values.colors.keys(): 
        container_number = values.colors[color].container_num
        if container_number == 100:
            container_colors["1"] = color
        if container_number == 200:
            container_colors["2"] = color
        if container_number == 300:
            container_colors["3"] = color
    
    container_hex_colors = {str(i+1): "#aaaaaa" for i in range(3)}
    container_icons = {str(i+1): "url(/assets/archive_white_24dp.svg)" for i in range(3)}
    for color in container_colors:
        if container_colors[color] == "red":
            container_hex_colors[color] = "#dc3545"
            container_icons[color] = "url(/assets/archive_red_24dp.svg)"
        if container_colors[color] == "green":
            container_hex_colors[color] = "#198754"
            container_icons[color] = "url(/assets/archive_green_24dp.svg)"
        if container_colors[color] == "yellow":
            container_hex_colors[color] = "#ffc107"
            container_icons[color] = "url(/assets/archive_yellow_24dp.svg)"
    
    
    #content
    return html.Div(
        children = [
            html.Div(
                icon(
                    icon = "url(/assets/pending_24dp.svg)",
                    text = "Loading ...",
                    color = "#aaaaaa"
                ),
                id = "control-icon-div"
            ),
            html.Br(),
            html.Div(
                control_button(
                    children = dbc.Spinner(),
                    color = "secondary",
                    fontsize = "1rem"
                ),
                id = "control-interact-div"
            ),
            html.Br(),
            html.Br(),
            dbc.Row(
                children = [
                    dbc.Col(
                        children = [
                            html.Div(
                                container_icon(
                                    container_number = 1,
                                    icon = container_icons["1"], 
                                    color = container_hex_colors["1"]
                                ),
                                id = "container-1-icon-div"
                            ),
                            color_select(
                                id = "container-1",
                                value = container_colors["1"]
                            )
                        ]
                    ),
                    dbc.Col(
                        children = [
                            html.Div(
                                container_icon(
                                    container_number = 2,
                                    icon = container_icons["2"], 
                                    color = container_hex_colors["2"]
                                ),
                                id = "container-2-icon-div"
                            ),
                            color_select(
                                id = "container-2",
                                value = container_colors["2"]
                            )
                        ]
                    ),
                    dbc.Col(
                        children = [
                            html.Div(
                                container_icon(
                                    container_number = 3,
                                    icon = container_icons["3"], 
                                    color = container_hex_colors["3"]
                                ),
                                id = "container-3-icon-div"
                            ),
                            color_select(
                                id = "container-3",
                                value = container_colors["3"]
                            )
                        ]
                    ),
                ]
            ),
            html.Br(),
            html.Br(),
            html.Div(
                children = [
                    "Bei Problemen kann hier der Server neu gestartet werden:"
                ], 
                style = mmt.dash.flex_style({"textAlign": "center"})
            ),
            html.Br(),
            html.Div(
                dbc.Button(
                    "Reset Server",
                    style = {
                        "fontWeight": "bold",
                        "fontSize": "1.5rem",
                        "height": "5rem",
                        "width": "12.5rem",
                    }
                ),
                style = mmt.dash.flex_style()
            ),
            dcc.Interval(id = "control-interval")
        ]
    )