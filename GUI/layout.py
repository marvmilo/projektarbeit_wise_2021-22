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
            "background-size": "cover",
        },
        title = title,
            title_style = {
            "width": "10rem",
            "font-size": "1.5rem"
        }, 
        expand = "lg",
        items = [
            mmt.dash.nav.item.normal(
                "NavItem1",
                id = "navitem1"
            ),
            mmt.dash.nav.item.normal(
                "NavItem2",
                id = "navitem2"
            )
        ]
    )

#main content of page
main_content = html.Div(
    "page content",
    style = {"padding": "5%"}
)