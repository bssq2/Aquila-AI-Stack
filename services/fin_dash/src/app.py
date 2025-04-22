from dash import Dash
from layout import make_layout

app = Dash(__name__)
app.layout = make_layout()