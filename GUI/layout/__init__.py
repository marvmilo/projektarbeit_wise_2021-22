from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#import other page contents
from . import home
from . import control
from . import monitoring

#main structure of page
def structure(title):
    return html.Div(
        children = [
            navbar(title),
            mmt.dash.content_div(
                width = "1200px",
                padding = "5%",
                children = [
                    html.Div(
                        html.Div(
                            dbc.Spinner(spinner_style = {"width": "3rem", "height": "3rem"}),
                            style = mmt.dash.flex_style({"height": "20rem"})
                        ),
                        id = "main-content"
                    )
                ]
            ),
            dcc.Location(id = "url"),
            html.Div(
                children = [
                    dcc.Interval(id = "control-interval", disabled = True),
                    dcc.Interval(id = "monitoring-interval", disabled = True),
                    html.Div(id = "control-icon-div"),
                    html.Div(id = "container-1-icon-div"),
                    html.Div(id = "container-2-icon-div"),
                    html.Div(id = "container-3-icon-div"),
                    html.Div(id = "control-container-1-color"),
                    html.Div(id = "control-container-2-color"),
                    html.Div(id = "control-container-3-color"),
                    html.Div(id = "control-interact-div"),
                    html.Div(id = "control-reset-button-div"),
                    html.Div(id = "monitoring-tablet-progress"),
                    html.Div(id = "monitoring-container1-progress"),
                    html.Div(id = "monitoring-container2-progress"),
                    html.Div(id = "monitoring-container3-progress"),
                    html.Div(id = "monitoring-robot-not-running-div"),
                    html.Div(id = "monitoring-current-ball-div"),
                    html.Div(id = "monitoring-picture"),
                    dbc.Select(id = "container-1-select"),
                    dbc.Select(id = "container-2-select"),
                    dbc.Select(id = "container-3-select"),
                    dbc.Button(id = "control-start-button"),
                    dbc.Button(id = "sorted-acknowleged-button"),
                    dbc.Button(id = "control-reset-button-1"),
                    dbc.Button(id = "control-reset-button-2"),
                    dbc.Button(id = "control-stop-button"),
                    html.Div(id = "dummy")
                ],
                style = {"display": "none"}
            )
        ]
    )

#navbar of page
def navbar(title):
    return mmt.dash.nav.bar(
        logo = "url(/assets/logo.png)",
        logo_style = {
            "width": "3.25rem", 
            "height": "3rem",
            "backgroundSize": "cover",
        },
        title = title,
            title_style = {
            "width": "10rem",
            "fontSize": "1.5rem"
        }, 
        expand = "lg",
        items = [
            mmt.dash.nav.item.href(
                "Control",
                href = "/control"
            ),
            mmt.dash.nav.item.href(
                "Monitoring",
                href = "/monitoring"
            ),
            mmt.dash.nav.item.href(
                "Github",
                href = "https://github.com/marvmilo/projektarbeit_wise_2021-22",
                target = "_blank"
            )
        ]
    )

#not found page
not_found = html.Div(
    html.Div(
        children = [
            html.Div(
                "404",
                style = mmt.dash.flex_style({
                    "fontSize": "7rem",
                    "fontWeight": "bold"
                })
            ),
            html.Div(
                "Not Found!",
                style = mmt.dash.flex_style({
                    "fontSize": "2rem",
                    "fontWeight": "bold"
                })
            )
        ]
    ),
    style = mmt.dash.flex_style({"height": "30rem"})
)