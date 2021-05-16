import dash
import dash_bootstrap_components as dbc
import pathlib
import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt
from datetime import timedelta
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output,State

from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()

df = pd.read_csv(DATA_PATH.joinpath("BASE_TOTAL.csv"),sep = ';',dtype={"REAL_TM": "float","ID": "int8","MARCA": "category","CATEGORIA": "category","CANAL": "category","OFICINA": "category","FAMILIA": "category","MATERIAL": "category","CLIENTE": "category"})

df.DIA = pd.to_datetime(df.DIA , dayfirst = True)
df['MES_ANO'] = df['DIA'].dt.to_period('M').astype(str)
df.set_index('DIA',inplace = True)


fig = go.Figure(go.Indicator(
    mode = "number+delta",
    value = 492,
    delta = {"reference": 512, "valueformat": ".0f"},
    title = {"text": "Users online"},
    domain = {'y': [0, 1], 'x': [0.25, 0.75]}))

fig.add_trace(go.Scatter(
    y = [325, 324, 405, 400, 424, 404, 417, 432, 419, 394, 410, 426, 413, 419, 404, 408, 401, 377, 368, 361, 356, 359, 375, 397, 394, 418, 437, 450, 430, 442, 424, 443, 420, 418, 423, 423, 426, 440, 437, 436, 447, 460, 478, 472, 450, 456, 436, 418, 429, 412, 429, 442, 464, 447, 434, 457, 474, 480, 499, 497, 480, 502, 512, 492]))

fig.update_layout(xaxis = {'range': [0, 62]})

layout = html.Div([
    dbc.Row([
            dbc.Col([
                    html.Div(
                        [
                            dbc.Button("Filtros", id="open",color="warning",),
                            dbc.Modal(
                                [
                                    dbc.ModalHeader("Filtros:"),
                                    dbc.ModalBody(dbc.FormGroup([

                                                    #dbc.Label("CATEGORIA: ", html_for="Mi_selector_CAT"),
                                                    #dcc.Dropdown(id='Mi_selector_CAT', multi=True,
                                                    # value=df.CATEGORIA.unique(),
                                                     #placeholder="Seleccione Categoría ...",
                                                     #options=[{'label': x, 'value': x} for x in
                                                    #          sorted(df.CATEGORIA.unique())],
                                                    # ),
                                                    dbc.Label("OFICINA: ",html_for="Mi_selector_ofi"),
                                                    dcc.Dropdown(id='Mi_selector_ofi', multi=True,
                                                    value=df.OFICINA.unique(),
                                                    placeholder="Seleccione Oficina ...",
                                                    options=[{'label': x, 'value': x} for x in sorted(df.OFICINA.unique())],
                                                ),
                                                 html.Br(),

                                                    dbc.Label("GRUPO DE VENDEDOR: ",html_for="Mi_selector_gv"),
                                                    dcc.Dropdown(id='Mi_selector_gv', multi=True,
                                                    value=df.GRUPO_VENDEDOR.unique(),
                                                    placeholder="Seleccione Grupo de Vendedor ...",
                                                    options=[{'label': x, 'value': x} for x in sorted(df.GRUPO_VENDEDOR.unique())],
                                                ),
                                                html.Br(),
                                                    dbc.Label("CANAL: ",html_for="Mi_selector_can"),
                                                    dcc.Dropdown(id='Mi_selector_can', multi=True,
                                                    value=df.CANAL.unique(),
                                                    placeholder="Seleccione Canal ...",
                                                    options=[{'label': x, 'value': x} for x in sorted(df.CANAL.unique())],
                                                ),


                                    ])),
                                    dbc.ModalFooter(
                                        dbc.Button("Cerrar", id="close", className="ml-auto")
                                    ),
                                ],
                                id="modal",
                                # size="lg",
                                # centered=True,
                            ),
                        ]
                    ),

            ],xs=12 ,sm=9, lg=4),
            dbc.Col(
                html.H1('Indicadores Comerciales', style={"textAlign": "center","font-weight":"bold"}),xs=12 ,sm=9, lg=4
            ),
            dbc.Col(
            [

                        dbc.Label("PERIODO ", html_for="Mi_selector_MES1"),
                        dcc.Dropdown(id='Mi_selector_MES1',
                                value='2020-12',
                                placeholder="Seleccione Mes ...",
                                options=[{'label': x, 'value': x} for x in sorted(df.MES_ANO.unique())],
                                ),

                           ]),
            dbc.Col(
            [

                        dbc.Label("VERSUS: ", html_for="Mi_selector_MES2"),
                        dcc.Dropdown(id='Mi_selector_MES2',
                                value='2020-11',
                                placeholder="Seleccione Mes ...",
                                options=[{'label': x, 'value': x} for x in sorted(df.MES_ANO.unique())],
                                ),

                           ])

            ],justify="center"
    ),

    dbc.Row(
        [
            dbc.Col(
                dcc.Graph(figure=fig)
            ),
            dbc.Col(),
            dbc.Col(),
            dbc.Col(),
            dbc.Col(),


        ]




    ),
    html.Iframe(src=app.get_asset_url('CV.pdf'),
                style={"height": "750px", "width": "50%"})
])

@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output('Mi_selector_can', 'options'),
    Output('Mi_selector_can', 'value'),
    Input('Mi_selector_gv', 'value'),
)
def set_cities_options(chosen_state):
    dff = df[df.GRUPO_VENDEDOR.isin(chosen_state)]
    counties_of_states = [{'label': c, 'value': c} for c in sorted(dff.CANAL.unique())]
    values_selected = [x['value'] for x in counties_of_states]
    return counties_of_states, values_selected


@app.callback(
    Output('Mi_selector_gv', 'options'),
    Output('Mi_selector_gv', 'value'),
    Input('Mi_selector_ofi', 'value'),
)
def set_cities_options2(chosen_state):
    dff = df[df.OFICINA.isin(chosen_state)]
    counties_of_states = [{'label': c, 'value': c} for c in sorted(dff.GRUPO_VENDEDOR.unique())]
    values_selected = [x['value'] for x in counties_of_states]
    return counties_of_states, values_selected