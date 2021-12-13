import dash
from dash import html
import dash_bootstrap_components as dbc
import dash_bootstrap_templates as dbt
import marvmiloTools as mmt
import os

#init app
app = dash.Dash(
    title = "HSV Color Justifier",
    meta_tags = [mmt.dash.mobile_optimization],
    external_stylesheets = [dbc.themes.DARKLY]
)
dbt.load_figure_template("darkly")

#picture rgb
def create_rgb(file):
    return dbc.Carousel(
        items = [{"key": "1", "src": file}],
            controls=False,
            indicators=False,
            interval=None,
    )

#layout
app.layout = mmt.dash.content_div(
    width = "1000px",
    padding = "5%",
    children = [
        dbc.Label("File:"),
        dbc.Select(
            id = "file",
            options = [
                {"label": f, "value": f}
                for f in os.listdir("./pictures")
            ],
            value = os.listdir("./pictures")[1]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            children = [
                dbc.Col(
                    html.Div(
                        style = {
                            "backgroundImage": "url(/assets/demo.jpg)",
                            "height": "20rem"
                        }
                    )
                ),
                dbc.Col(
                    "pic 2"
                )
            ]
        ),
        dbc.Row(
            children = [
                dbc.Col(
                    "adj 1"
                ),
                dbc.Col(
                    "adj 2"
                )
            ]
        )
    ]
)

app.run_server(
    debug=True,
    host = "0.0.0.0"
)