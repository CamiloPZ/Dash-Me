import dash
import dash_bootstrap_components as dbc
import pathlib
import dash_core_components as dcc
import pandas as pd
import dash_html_components as html

from app import app

layout = html.Div([
    html.Br(),
    dbc.Row(
        [
            dbc.Col(
                html.Iframe(src=app.get_asset_url('CV_CamiloPoma.pdf'),
                style={"height": "750px", "width": "50%"})
            )
        ],
        justify="center"
    ),
    dcc.Markdown(
        '''
        # Hola
        '''
    )
])
