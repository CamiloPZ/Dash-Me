import dash
import dash_bootstrap_components as dbc
import pathlib
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = px.data.iris()
fig1 = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'], template="plotly_dark")



fig2 = go.Figure(data=go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(size=[40, 60, 80, 100],
                color=[0, 1, 2, 3])
))

fig2.update_layout(

     template="plotly_dark"
)

layout = html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col(children=[dbc.Card([
            dbc.CardHeader("Plotly Express"),
            dbc.CardBody(children=[
                dcc.Graph(id="fig1",figure=fig1),
            ])])]),
        dbc.Col(children=[dbc.Card([
            dbc.CardHeader("Graph Objects"),
            dbc.CardBody(children=[
                dcc.Graph(id="fig2",figure=fig2),
            ])])])
    ]),
    dcc.Markdown(
        '''
        # Hi there!
        '''
    )
])
