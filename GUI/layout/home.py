import marvmiloTools as mmt
from dash import html
import dash_bootstrap_components as dbc

#home content
content = html.Div(
    children = [
        html.Div(
            html.Div(
                style = {
                    "backgroundImage": "url(\"/assets/robot.png\")",
                    "backgroundSize": "cover",
                    "marginBottom": "2rem",
                    "maxWidth": "12.5rem",
                    "minWidth": "12.5rem",
                    "height": "20rem"
                }
            ),
            style = mmt.dash.flex_style()
        ),
        html.Div(
            html.H1(
                "Projektarbeit SoSe 2021/22",
                style = {"text-align": "center"}
            ),
            style = mmt.dash.flex_style()
        ),
        html.Br(),
        html.Div(
            html.Div(),
            style = mmt.dash.flex_style()
        )
    ]
)