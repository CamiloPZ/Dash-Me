import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
from app import app
from app import server
import plotly.graph_objects as go

# Connect to your app pages
from apps import historia,dashboard,detalle,analisis
#from scikit_image import io

# You can give path to the
# image as first argument
app.layout = html.Div([


    html.Div([
        dbc.NavbarSimple(
            children=[
                # collapse,
                #toast,
                dbc.NavLink("Dash", href="/apps/dashboard", id="page-1-link",style={"font-size": "1.35em"}),
                dbc.NavLink("Detalle", href="/apps/detalle", id="page-2-link",style={"font-size": "1.35em"}),
                dbc.NavLink("Histórico", href="/apps/historia", id="page-3-link",style={"font-size": "1.35em"}),
                dbc.NavLink("Análisis", href="/apps/analisis", id="page-4-link",style={"font-size": "1.35em"}),
            ],
            # fill=True,
            brand="Dash App - Intradevco",
            color="success",
            dark=True,
        ),
    ], #className="row"
    ),
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content'
    , children=[

        #html.Div(
         #   html.Img(src=app.get_asset_url('itdc.jpg')))

        ]
    ,style={"background":"#F5F5F5","padding":"0.7%"}),


])


portada = html.Div(
    [
        html.H2 ('Bienvenido al Dash App de Intradevco Bolivia',style={"textAlign": "center"}),
        html.Br(),
        dbc.Row([
          dbc.Col(html.Img(src=app.get_asset_url('itdc.jpg'),style={'height':'100%', 'width':'98%'}),xs=12, sm=12, md=11, lg=6, xl=6),
          dbc.Col([html.H3('Contenido',style={"textAlign": "center"}),
                        dcc.Markdown(
                                '''
                                
                                * ***Dash:*** Vista Resumen
                                * ***Detalle:*** Se muestran filtros adicionales
                                * ***Histórico:*** Evolución de la ventas mensuales
                                * ***Análisis:*** Medición de adquisición y retención
                                '''
                            ),
                   html.H3('Indicadores', style={"textAlign": "center"}),
                   dcc.Markdown(
                       '''

                       * ***CcC:*** Clientes con Comprea
                       * ***Mix de Categoría:*** Número promedio de categorías que compran los clientes
                       * ***Mix de Familia:*** Número promedio de familia que compran los clientes
                       * ***Profundidad:*** Número promedio de sku's que compran los clientes
                       * ***Ticket Promedio:*** Volumen o venta promedio que compran los clientes
                       * ***Frecuencia de Compra:*** Cantidad de veces que compran en promedio los clientes
                       * ***Pordentaje de Recompra:*** Porcentaje de clientes que compran más de una vez
                       '''
                   )


                   ],xs=12, sm=12, md=11, lg=6, xl=6),
        ]

        ),

        html.Br(),
        html.Br(),
        html.H5('Cualquier comentario o consulta contactarse con el área de Inteligencia Comercial',style={"textAlign": "center"}),
        html.H5('ic@alicorp.com.pe',style={"textAlign": "center"})




    ]



)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
         return portada
     #   return dashboard.layout
    if pathname == '/apps/dashboard':
        return dashboard.layout
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
