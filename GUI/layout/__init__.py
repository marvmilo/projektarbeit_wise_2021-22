from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import marvmiloTools as mmt

#import other page contents
from . import home
from . import control
from . import containers
from . import history

#main structure of page
def structure(title):
    return html.Div(
        children = [
            navbar(title),
            html.Div(
                children = [
                    mmt.dash.content_div(
                        width = "1200px",
                        padding = "5%",
                        children = [
                            html.Div(
                                dbc.Spinner(spinner_style = {"width": "3rem", "height": "3rem"}),
                                style = mmt.dash.flex_style({"height": "20rem"})
                            )
                        ]
                    )
                ]  
            ),
            dcc.Location(id = "url")
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
                "Containers",
                href = "/containers"
            ),
            mmt.dash.nav.item.href(
                "History",
                href = "/history"
            ),
            mmt.dash.nav.item.href(
                "Github",
                href = "https://github.com/marvmilo/projektarbeit_wise_2021-22",
                target = "_blank"
            )
        ]
    )