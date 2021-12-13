import marvmiloTools as mmt
from dash import html

#containers content
content = html.Div(
    "page CONTAINERS content DIV",
    style = mmt.dash.flex_style({
        "backgroundColor": "#565656",
        "height": "75rem"      
    })
)