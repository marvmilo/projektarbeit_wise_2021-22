from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#main structure of page
def structure(title, page_content):
    return html.Div(
        children = [
            navbar(title),
            page_content
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
            mmt.dash.nav.item.normal(
                "NavItem1",
                id = "navitem1",
                size = "lg"
            ),
            mmt.dash.nav.item.normal(
                "NavItem2",
                id = "navitem2",
                size = "lg"
            )
        ]
    )

#main content of page
main_content = mmt.dash.content_div(
    width = "1200px",
    padding = "5%",
    children = [
        html.Div(
            "page content DIV",
            style = mmt.dash.flex_style({
                "backgroundColor": "#565656",
                "height": "100rem"      
            })
        )
    ]
)