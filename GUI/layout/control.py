import marvmiloTools as mmt
from dash import html

#control content
content = html.Div(
    "page CONTROL content DIV",
    style = mmt.dash.flex_style({
        "backgroundColor": "#565656",
        "height": "75rem"      
    })
)