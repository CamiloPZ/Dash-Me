import dash
import dash_bootstrap_components as dbc
import pathlib
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt
from datetime import timedelta
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output,State
import dash_trich_components as dtc
from dash_extensions import Lottie
# from dash_extensions import Sync
import math
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()



df = px.data.gapminder()
print(df.year.unique())
df_2020 = df.query("year==2007")



fig = px.scatter(df_2020,
                x="gdpPercap", y="lifeExp", size="pop", color="continent",
                log_x=True, size_max=60,
                template="plotly_dark", title="Gapminder 2020")



url_ytb = "https://assets2.lottiefiles.com/packages/lf20_JoLzcd.json"
link_ytb = "https://www.youtube.com/channel/UCAlUNyWsCyJeEMRnKKeWsxg"

url_linke = "https://assets8.lottiefiles.com/packages/lf20_yNYxCH.json"
link_linke = "https://www.linkedin.com/in/camilo-d-vinchi-poma-zamudio-142711139/"

url_mail = "https://assets4.lottiefiles.com/packages/lf20_odef4xnr.json"
link_mail = "mailto:cpomaz@uni.pe?subject=Mail from our Website"

url_git = "https://assets8.lottiefiles.com/packages/lf20_Cko7Sr.json"
link_git = "https://github.com/CamiloPZ"

url_face = "https://assets7.lottiefiles.com/private_files/lf30_pb3we3yk.json"
link_face = "https://www.facebook.com/CamiloPomaZ/"

url_inst = "https://assets7.lottiefiles.com/private_files/lf30_igdzkfxv.json"
link_insta = "https://www.instagram.com/camilo_poma/"

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))







layout = html.Div([
    html.Br(),
    html.H1(children='All my social media',style={'textAlign':'center','font-weight':"bold",'font-family':'Comic Sans MS'}),
    html.Br(),
    
    # dcc.Markdown('''
    #     ```python
    #     def f(a, b):
    #         return a + b
    #     ```

     


    #     | Tables   |      Are      |  Cool |
    #     |----------|:-------------:|------:|
    #     | col 1 is |  left-aligned | 1600  |
    #     | col 2 is |    centered   | 12    |
    #     | col 3 is | right-aligned |   1   |

    #     '''),
    dbc.CardDeck([
    # dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="52%", height="67%", url=url_ytb)),
                dbc.CardBody([
                    dbc.CardLink("Youtube", href=link_ytb),
                    html.H2(id='content-connections', children="000")
                ], style={'textAlign':'center','font-family':'Comic Sans MS'})
            ]),
        ],xs=6 ,md =4,sm=6 ,lg=2,xl = 2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="52%", height="32%", url=url_linke)),
                dbc.CardBody([
                    dbc.CardLink("LinkedIn", href=link_linke),
                    html.H2(id='content-companies', children="000")
                ], style={'textAlign':'center','font-family':'Comic Sans MS'})
            ]),
        ],xs=6 ,md =4,sm=6 ,lg=2,xl = 2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="53%", height="25%", url=url_mail)),
                dbc.CardBody([
                    dbc.CardLink("Mail", href=link_mail),
                    html.H2(id='content-msg-in', children="000")
                ], style={'textAlign':'center','font-family':'Comic Sans MS'})
            ]),
        ],xs=6 ,md =4,sm=6 ,lg=2,xl = 2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="53%", height="53%", url=url_git)),
                dbc.CardBody([
                    dbc.CardLink("GitHub", href=link_git),
                    html.H2(id='content-msg-out', children="000")
                ], style={'textAlign': 'center','font-family':'Comic Sans MS'})
            ]),
        ],xs=6 ,md =4,sm=6 ,lg=2,xl = 2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="54%", height="25%", url=url_face)),
                dbc.CardBody([
                    dbc.CardLink("Facebook", href=link_face),
                    html.H2(id='content-reactions', children="000")
                ], style={'textAlign': 'center','font-family':'Comic Sans MS'})
            ]),
        ],xs=6 ,md =4,sm=6 ,lg=2,xl = 2),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(Lottie(options=options, width="55%", height="85%", url=url_inst)),
                dbc.CardBody([
                    dbc.CardLink("Instagram", href=link_insta),
                    html.H2(id='content-reactions2', children="000")
                ], style={'textAlign': 'center','font-family':'Comic Sans MS'})
            ]),
        ],xs=6 ,md =4,sm=6 ,lg=2,xl = 2),
    # ],
    # justify="center",),
    ]),
    html.H3(''),
    dcc.Graph(id='figure1',figure=fig),
    dbc.Row([
            dbc.Col([
                    html.Div(
                        [
                            
                        ]
                    ),

            ],xs=12 ,sm=9, lg=4),
         
            dbc.Col(
            [

                     

                           ]),
            dbc.Col(
            [

                   

                           ])

            ],justify="center"
    ),

    dbc.Row(
        [
            html.Br(),
            # dbc.Col(card),

            dbc.Col(),
            dbc.Col(),
            dbc.Col(),


        ]




    ),

    html.Br(),
    
])

