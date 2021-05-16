import datetime

import dash
# from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_trich_components as dtc


from app import app


card1 = dtc.Card(
            link='https://www.instagram.com/camilo_poma/',
            image=app.get_asset_url('vaex.png'),
            title='Vaex Library',
            description='Description text',
            badges=['Badge 1', 'Badge 2', 'Badge 3'],
            git='https://github.com/CamiloPZ',
            dark=True
        )

card2 = dtc.Card(
            link='https://www.instagram.com/camilo_poma/',
            image=app.get_asset_url('dash.png'),
            title='Dash Library',
            description='Description text',
            badges=['Badge 1', 'Badge 2', 'Badge 3'],
            git='https://github.com/CamiloPZ',
            dark=True
        )
        
card3 = dtc.Card(
            link='https://www.instagram.com/camilo_poma/',
            image=app.get_asset_url('python.png'),
            title='Python',
            description='Description text',
            badges=['Badge 1', 'Badge 2', 'Badge 3'],
            git='https://github.com/CamiloPZ',
            dark=True
        )

card4 = dtc.Card(
            link='https://www.instagram.com/camilo_poma/',
            image=app.get_asset_url('pyspark.jpg'),
            title='Pyspark',
            description='Description text',
            badges=['Badge 1', 'Badge 2', 'Badge 3'],
            git='https://github.com/CamiloPZ',
            dark=True
        )

layout = html.Div([
    html.Br(),
    html.H2('Some of my publications',style={"textAlign":"center","font-weight":"bold","font-family":"Comic Sans MS"}),
    html.Br(),
    dbc.Row([
        dbc.Col([
            card1,       
        
        ]),
        dbc.Col([
            card2,        
        
        ]),
        dbc.Col([
            card3,        
        
        ]),
         dbc.Col([
            card4,        
        
        ]),
    
    ],
    justify="center")
    
])


