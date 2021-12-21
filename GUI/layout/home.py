import marvmiloTools as mmt
from dash import html
import dash_bootstrap_components as dbc

#variables
button_width = "10rem"
button_height = "5rem"
button_padding = "1rem"

#for creating buttons columns
def button_col(text, href = "/"):
    return dbc.Col(
        html.A(
            dbc.Button(
                text,
                size = "lg",
                style = {
                    "width": button_width,
                    "height": button_height
                }
            ),
            href = href
        ),
        width = "auto",
        style = {"padding": button_padding},
    )

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
                style = {
                    "textAlign": "center",
                    "fontWeight": "bold",
                }
            ),
            style = mmt.dash.flex_style()
        ),
        html.Br(),
        html.Div(
            html.H4(
                "Kuka Agilus KR6 Kugel Sotierroboter",
                style = {"textAlign": "center"}
            ),
            style = mmt.dash.flex_style()
        ),
        html.Br(),
        html.Div(
            html.Div(
                """
                Roboterarm zum sotieren von gelben, grünen und roten Kugeln in Container.
                Kugeln werden über ein Kamerasystem aus einem chaotischen Lagersystem ausgewertet.
                Container, in die die Kugeln sotiert werden, können dabei selbst festgelegt werden.
                """,
                style = {"textAlign": "center"}
            ),
            style = mmt.dash.flex_style()
        ),
        html.Br(),
        dbc.Row(
            children = [
                button_col("Control", "/control"),
                button_col("Containers", "/containers"),
                button_col("History", "/history"),
            ],
            justify = "center"
        )
    ]
)