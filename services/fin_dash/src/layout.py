import dash_core_components as dcc
import dash_html_components as html

def make_layout():
    return html.Div([
        html.H1("Finance Dashboard"),
        dcc.Graph(id="dummy-graph")
    ])