import dash
import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    title="Dash Me",
    external_stylesheets=[dbc.themes.DARKLY],
    external_scripts=[
    'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/MathJax.js?config=TeX-MML-AM_CHTML',
    ],
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.7",
        }
    ],
)
server = app.server
