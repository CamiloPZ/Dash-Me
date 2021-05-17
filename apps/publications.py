import datetime

import dash
# from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_trich_components as dtc


from app import app

card_content_1 = [
    dbc.CardImg(src=app.get_asset_url('py.png'), top=True),
    dbc.CardBody(
        [
            html.H5("How to install python", className="card-title"),
            html.P(
                "This card has an image on top, and a button below",
                className="card-text"
            ),
            dbc.Button("Take me there!", color="dark"),
        ]
    ),
]

card_content_2 = [
    dbc.CardImg(src=app.get_asset_url('py.png'), top=True),
    dbc.CardBody(
        [
            html.H5("How to setup python in VS Code", className="card-title"),
            html.P(
                "This card has an image on top",
                className="card-text"
            ),
            dbc.Button("Take me there!", color="dark"),
        ]
    ),
]

card_content_3 = [
    dbc.CardImg(src=app.get_asset_url('py.png'), top=True),
    dbc.CardBody(
        [
            html.H5("How to plot in python", className="card-title"),
            html.P(
                "This card has an image on top, and a button below",
                className="card-text"
            ),
            dbc.Button("Take me there!", color="dark"),
        ]
    ),
]

card_content_4 = [
    dbc.CardImg(src=app.get_asset_url('py.png'), top=True),
    dbc.CardBody(
        [
            html.H5("How to generate an app", className="card-title"),
            html.P(
                "This card has an image on top, and a button below",
                className="card-text"
            ),
            dbc.Button("Take me there!", color="dark"),
        ]
    ),
]

# cards = dbc.CardColumns(
#     [
       
#         dbc.Card(card_content_3, color="info", inverse=True,className="w-25",),
#         dbc.Card(card_content_3, color="light",className="w-25"),
#         dbc.Card(card_content_3, color="warning",className="w-25"),
#         dbc.Card(card_content_3, color="danger",className="w-25"),

#     ]
# )

first_card = dbc.Card(card_content_1, color="dark", inverse=True,className="mx-2 shadow pb-4",)

second_card = dbc.Card(card_content_2, color="dark", inverse=False,className="mx-2 shadow pb-4")

third_card = dbc.Card(card_content_3, color="dark", inverse=False,className="mx-2 shadow pb-4")

fourth_card = dbc.Card(card_content_4, color="dark", inverse=False,className="mx-2 shadow pb-4")


cards = dbc.Row([
        dbc.Col(first_card,xs=12,sm=6,md=4 ,lg=3,xl=3), 
        dbc.Col(second_card,xs=12,sm=6,md=4 ,lg=3,xl=3),
        dbc.Col(third_card,xs=12,sm=6,md=4 ,lg=3,xl=3),
        dbc.Col(fourth_card,xs=12,sm=6,md=4 ,lg=3,xl=3)])

# card1 = dtc.Card(
#             link='https://www.instagram.com/camilo_poma/',
#             image=app.get_asset_url('vaex.png'),
#             title='Vaex Library',
#             description='Description text',
#             badges=['Badge 1', 'Badge 2', 'Badge 3'],
#             git='https://github.com/CamiloPZ',
#             dark=True,
#             style={"height": "70%", "width": "10%"}
#         )

# card2 = dtc.Card(
#             link='https://www.instagram.com/camilo_poma/',
#             image=app.get_asset_url('dash.png'),
#             title='Dash Library',
#             description='Description text',
#             badges=['Badge 1', 'Badge 2', 'Badge 3'],
#             git='https://github.com/CamiloPZ',
#             dark=True
#         )
        
# card3 = dtc.Card(
#             link='https://www.instagram.com/camilo_poma/',
#             image=app.get_asset_url('python.png'),
#             title='Python',
#             description='Description text',
#             badges=['Badge 1', 'Badge 2', 'Badge 3'],
#             git='https://github.com/CamiloPZ',
#             dark=True
#         )

# card4 = dtc.Card(
#             link='https://www.instagram.com/camilo_poma/',
#             image=app.get_asset_url('pyspark.jpg'),
#             title='Pyspark',
#             description='Description text',
#             badges=['Badge 1', 'Badge 2', 'Badge 3'],
#             git='https://github.com/CamiloPZ',
#             dark=True
#         )


# cards = dbc.Col(
#     [   
#         cards,
#         dbc.CardDeck([
#         card1,
#         card2,
#         card3,
#         card4,


#     ],)

    
#     ],lg=12
# )



layout = html.Div([
    html.Br(),
    html.H2('Some of my publications',style={"textAlign":"center","font-weight":"bold","font-family":"Comic Sans MS"}),
    html.Br(),
    cards,
    html.Br(),
    cards,
    html.Br(),
    cards,
    html.Br(),
    cards,
    html.Br(),
    cards, 
    
    
])


