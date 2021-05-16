import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from app import app
from app import server
import plotly.graph_objects as go

# Connect to your app pages
from apps import historia,me,detalle,analisis

app.layout = html.Div([


    html.Div([
        dbc.NavbarSimple(
            children=[
                # collapse,
                #toast,
                dbc.NavLink("Social Media", href="/apps/me", id="page-1-link",style={"font-size": "1.35em"}),
                dbc.NavLink("Detalle", href="/apps/detalle", id="page-2-link",style={"font-size": "1.35em"}),
                dbc.NavLink("Histórico", href="/apps/historia", id="page-3-link",style={"font-size": "1.35em"}),
                dbc.NavLink("Análisis", href="/apps/analisis", id="page-4-link",style={"font-size": "1.35em"}),
            ],
            # fill=True,
            brand="Dash Me - Camilo Poma",
            color="primary",
            dark=True,
        ),
    ], #className="row"
    ),
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content'
    , children=[

        #html.Div(
         #   html.Img(src=app.get_asset_url('itdc.jpg')))

        ],
    # style={"background":"#F5F5F5","padding":"0.7%"}
    ),


])


portada = html.Div(
    [
        html.H2 ('Welcome to Camilo Poma Dash App',style={"textAlign": "center"}),
        html.Br(),
        dbc.Row([
          dbc.Col(html.Img(src=app.get_asset_url('itdc.jpg'),style={'height':'100%', 'width':'98%'}),xs=12, sm=12, md=11, lg=6, xl=6),
          dbc.Col([html.H3('Contents',style={"textAlign": "center"}),
                        dcc.Markdown(
                                '''
                                
                                * ***Dash:*** Vista Resumen
                                * ***Detalle:*** Se muestran filtros adicionales
                                * ***Blog:*** Evolución de la ventas mensuales
                                * ***Some plotly graphs:*** medición de adquisición y retención
                                '''
                            ),
                   html.H3('Indicadores', style={"textAlign": "center"}),
                   dcc.Markdown(
                       '''

                       * ***CcC:*** Clientes con Comprea
                       * ***Mix de Categoría:*** Número promedio de categorías que compran los clientes
                       * ***Mix de Familia:*** Número promedio de familia que compran los clientes
                       * ***Profundidad:*** Número promedio de sku's que compran los clientes
                       '''
                   )


                   ],xs=12, sm=12, md=11, lg=6, xl=6),
        ]

        ),

        html.Br(),
        html.Br(),
        html.H5('Cualquier comentario o consulta contactarse con el área de Inteligencia Comercial',style={"textAlign": "center"}),
        html.H5('cpomaz@uni.pe',style={"textAlign": "center"}),
        html.Br(),
        html.H5('https://github.com/CamiloPZ',style={"textAlign": "center"}),
        html.Br(),
        html.H5('https://www.instagram.com/camilo_poma/',style={"textAlign": "center"}),
        html.Br(),




    ]



)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return portada
     #   return me.layout
    if pathname == '/apps/me':
        return me.layout
    if pathname == '/apps/detalle':
        return detalle.layout
    if pathname == '/apps/historia':
        return historia.layout
    # if pathname == '/apps/evolutivo':
    #     return evolutivo.layout
    if pathname == '/apps/analisis':
        return analisis.layout
    else:
        return portada


if __name__ == '__main__':
    app.run_server(debug=True)
