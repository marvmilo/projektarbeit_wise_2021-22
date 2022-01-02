import marvmiloTools as mmt
from dash import html

#history content
def content(values):
    return html.Div(
        "page HISTORY content DIV",
        style = mmt.dash.flex_style({
            "backgroundColor": "#565656",
            "height": "75rem"      
        })
    )