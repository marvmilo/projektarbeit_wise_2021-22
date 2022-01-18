from dash.exceptions import PreventUpdate
import time
from dash import html
from dash.html.Pre import Pre
import dash_bootstrap_components as dbc
import os
import sys

#import other Scripts
from . import layout

#values
old_colors = None
old_colors_ts = time.time()
page_reload_colors = False

#page location callback
def location_callback(path, values):
    global page_reload_colors, page_reload_colors
    #print(path)
    page_reload_colors = True
    page_reload_colors_ts = time.time()
    if path == "/control":
        return layout.control.content(values)
    elif path == "/monitoring":
        return layout.monitoring.content(values)
    elif path == "/":
        return layout.home.content(values)
    return layout.not_found

#change control button
def control_interact(n_intervals, n_start, n_ack, values):
    if n_ack:
        values.robot.movementstatus = None
        values.UI.sorting_done = False
        values.UI.sorting_stopped = False
        values.ball.to_collect = 0 
        values.ball.total = 0
        values.ball.done = 0
        values.colors.red.sorted = 0
        values.colors.red.total = 0
        values.colors.green.sorted = 0
        values.colors.green.total = 0
        values.colors.yellow.sorted = 0
        values.colors.yellow.total = 0
    if values.UI.sorting_stopped:
        return [
            layout.control.icon(
                icon = "url(/assets/highlight_off_24dp.svg)",
                text = "Sotieren abgebrochen!",
                color = "#dc3545"
            ),
            [   
                layout.control.progress_bar(
                    values.ball.done,
                    values.ball.to_collect,
                    color = "danger"
                ),
                html.Br(),
                layout.control.control_button(
                    children = "Neuer Versuch!",
                    color = "danger",
                    fontsize = "2rem",
                    id = "sorted-acknowleged-button"
                ),
                html.Div(
                    children = [
                        html.Button(id = "control-start-button")
                    ],
                    style = {"display": "none"}
                )
            ]
        ]
    if values.UI.sorting_done:
        return [
            layout.control.icon(
                icon = "url(/assets/check_circle_outline_24dp.svg)",
                text = "Sotieren Erfolgreich!",
                color = "#198754"
            ),
            [   
                layout.control.progress_bar(
                    values.ball.done,
                    values.ball.to_collect,
                    color = "success"
                ),
                html.Br(),
                layout.control.control_button(
                    children = "Okay",
                    color = "success",
                    fontsize = "2rem",
                    id = "sorted-acknowleged-button"
                ),
                html.Div(
                    children = [
                        html.Button(id = "control-start-button")
                    ],
                    style = {"display": "none"}
                )
            ]
        ]
    if n_start or values.robot.movementclear:
        values.robot.movementclear = True
        return [
            layout.control.icon(
                icon = "url(/assets/check_circle_outline_24dp.svg)",
                text = "Roboter Running",
                color = "#198754"
            ),
            [   
                layout.control.progress_bar(
                    values.ball.done,
                    values.ball.to_collect,
                ),
                html.Br(),
                layout.control.control_button(
                    children = "Sotieren Stoppen!",
                    color = "danger",
                    fontsize = "2rem",
                    id = "control-stop-button"
                ),
                html.Div(
                    children = [
                        html.Button(id = "sorted-acknowleged-button"),
                        html.Button(id = "control-start-button")
                    ],
                    style = {"display": "none"}
                )
            ]
        ]
    try:
        if values.server.status.startswith("connected"):
            return [
                layout.control.icon(
                    icon = "url(/assets/info_24dp.svg)",
                    text = "Roboter Ready",
                    color = "#ffffff"
                ),
                [
                    layout.control.control_button(
                        children = "Sotieren Starten!",
                        color = "success",
                        fontsize = "2rem",
                        id = "control-start-button"
                    ),
                    html.Div(
                        children = [
                            html.Button(id = "sorted-acknowleged-button"),
                            html.Button(id = "control-reset-button-2")
                        ],
                        style = {"display": "none"}
                    )
                ]
            ]
    except AttributeError:
        pass
    return [
        layout.control.icon(
            icon = "url(/assets/highlight_off_24dp.svg)",
            text = "TCP Server not connected",
            color = "#dc3545"
        ),
        layout.control.control_button(
            children = "Reset Server",
            color = "secondary",
            fontsize = "2rem",
            id = "control-reset-button-2"
        )
    ]
    
#for changin display container color when switching containers
def control_container_color(value, container_number, values):
    if value == "red":
        return [
            layout.control.container_icon(
                container_number = container_number,
                icon = "url(/assets/archive_red_24dp.svg)",
                color = "#dc3545"
            )
        ]
    elif value == "green":
        return [
            layout.control.container_icon(
                container_number = container_number,
                icon = "url(/assets/archive_green_24dp.svg)",
                color = "#198754"
            )
        ]
    elif value == "yellow":
        return [
            layout.control.container_icon(
                container_number = container_number,
                icon = "url(/assets/archive_yellow_24dp.svg)",
                color = "#ffc107"
            )
        ]
    else:
        # for color in values.colors.keys():
        #     if values.colors[color].container_num == container_number*100:
        #         values.colors[color].container_num = None
        return [
            layout.control.container_icon(
                container_number = container_number,
                icon = "url(/assets/archive_white_24dp.svg)",
                color = "#aaaaaa"
            )
        ]

#for updating control select
def control_container_select(val1, val2):
    options = [
        {"label": "Rot", "value": "red"},
        {"label": "Grün", "value": "green"},
        {"label": "Gelb", "value": "yellow"}
    ]
    options = [d for d in options if not d["value"] in [val1, val2]]
    options.append({"label": "Keine", "value": "none"})
    return [options]

# for updating control container color
def control_container_color_update(n_intervals, values, style1, style2, style3):
    global old_colors, old_colors_ts, page_reload_colors, page_reload_colors_ts
    
    try:
        new_colors = {str(i+1): style["color"] for i, style in enumerate([style1, style2, style3])}
    except TypeError:
        raise PreventUpdate
    
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
    for color in container_colors:
        if container_colors[color] == "red":
            container_hex_colors[color] = "#dc3545"
        if container_colors[color] == "green":
            container_hex_colors[color] = "#198754"
        if container_colors[color] == "yellow":
            container_hex_colors[color] = "#ffc107"
    
    if not old_colors:
        old_colors = new_colors
        
    if not container_hex_colors == new_colors or page_reload_colors:
        if not old_colors == new_colors and not page_reload_colors:
            old_colors = container_hex_colors
            old_colors_ts = time.time()
            for color in values.colors.keys():
                values.colors[color].container_num = None
            for container in new_colors:
                if new_colors[container] == "#dc3545":
                    values.colors.red.container_num = int(container)*100
                if new_colors[container] == "#198754":
                    values.colors.green.container_num = int(container)*100
                if new_colors[container] == "#ffc107":
                    values.colors.yellow.container_num = int(container)*100
            raise PreventUpdate
        page_reload_colors = False
        return [
            container_colors["1"],
            container_colors["2"],
            container_colors["3"]
        ]
    else:
        if time.time() - old_colors_ts > 2:
            old_colors = new_colors
        raise PreventUpdate
    
#for resetting server
def control_reset(reset1, reset2):
    if reset1 or reset2:
        print("RESET SERVICE")
    return [layout.control.reset_button()]

#for updating progress bars on monitoring
def monitoring_progress(n_intervals, values):
    color_dict = layout.monitoring.get_color_dict(values)
    return [
        layout.monitoring.progress_level(
            bars = color_dict.tablet.bars,
            current = color_dict.tablet.remaining,
            total = color_dict.tablet.total,
            total_sum = True
        ),
        layout.monitoring.progress_level(
            bars = [color_dict.container1.bar],
            current = color_dict.container1.bar.done,
            total = color_dict.container1.total,
        ),
        layout.monitoring.progress_level(
            bars = [color_dict.container2.bar],
            current = color_dict.container2.bar.done,
            total = color_dict.container2.total,
        ),
        layout.monitoring.progress_level(
            bars = [color_dict.container3.bar],
            current = color_dict.container3.bar.done,
            total = color_dict.container3.total,
        )
    ]

#for disabling input while running robot in control
def control_disable_input(n_intervals, values):
    if values.robot.movementclear or values.UI.sorting_done:
        return [True, True, True, True]
    else:
        return [False, False, False, False]
    
#for stopping roboter while sorting
def control_stop_roboter(n_stop, values):
    if n_stop:
        values.robot.movementclear = False
        values.UI.sorting_stopped = True
    raise PreventUpdate

#for hiding robot not running div
def hide_robot_not_running(n_intervals, values):
    if values.robot.movementclear:
        return [{"display": "none"}, None]
    else:
        return [None, {"display": "none"}]
    
#for updating current ball
def update_current_ball(n_intervals, values):
    if values.UI.ball.color:
        return [layout.monitoring.current_ball(
            color = values.UI.ball.color,
            x = values.UI.ball.x,
            y = values.UI.ball.y
        )]
    raise PreventUpdate

#for updating monitoring picutre
def monitoring_update_picture(n_intervals, values):
    if values.robot.movementclear:
        print("PICTURE")
        return [
            [], 
            layout.monitoring.picture_style({
                "backgroundImage": "url(/assets/location_image.jpg)",
                "backgroundSize": "cover",
                "aspect-ratio": "20 / 14"
            })
        ]
    else:
        return [
            layout.monitoring.robot_not_running(button_color = "primary"),
            layout.monitoring.picture_style({"height": "20rem"})
        ]