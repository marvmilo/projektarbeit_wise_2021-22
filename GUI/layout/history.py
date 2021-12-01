import marvmiloTools as mmt
from dash import html

#home content
content = mmt.dash.content_div(
    width = "1200px",
    padding = "5%",
    children = [
        html.Div(
            "page HISTORY content DIV",
            style = mmt.dash.flex_style({
                "backgroundColor": "#565656",
                "height": "75rem"      
            })
        )
    ]
)