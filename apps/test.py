import dash
import dash_bootstrap_components as dbc
import pathlib
import dash_core_components as dcc
import pandas as pd
import dash_html_components as html

from app import app


layout = html.Div([
    html.Br(),
    html.Div(id='static',children='$$y = \\begin{cases} 0 & x < 0 \\\\ x & x \ge 0 \\end{cases}$$'),
    html.Div(id='static',children='$$f(x) = \\frac{1}{2}(1+ \\theta x) ; -1<x<1, \\theta \in <-1,1>$$'),
    html.Div(id='static',children='$$F(x) = \\begin{array}{cc} \\{ &  \\begin{array}{cc} 0 & x\\leq -1 \\\ \\frac{1}{2} (\\theta \\frac{x^2}{2} + x - \\frac{\\theta}{2} + 1) & -1\\leq x\\leq 1 \\\   1 & 1\\leq x    \\end{array}\\end{array}$$'),
    html.Div(id='static',children='$$F(x) = \\begin{cases} 0 &  x\leq -1  \\\\ \\frac{1}{2} (\\theta \\frac{x^2}{2} + x - \\frac{\\theta}{2} + 1) & -1\leq x\leq 1  \\\\ 1 &  1\leq x \\end{cases}$$'),
    dbc.Row(
        [
            dbc.Col(
                html.Iframe(src=app.get_asset_url('CV_CamiloPoma.pdf'),
                style={"height": "750px", "width": "50%"})
            )
        ],
        justify="center"
    ),
    dcc.Markdown('''

        Inline code snippet: `False`

        Block code snippet:
        ```ruby
        import dash

        external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

        app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
        for i in range(8):
            print(i)


        ```

            >
            > Block quotes are used to highlight text.
            >

        That is so funny! :joy:

        '''),

    html.Code(children=
                '''def funcion(a):
                    return a+1
                ''', className="python"),

    # html.Code[chil),


])
