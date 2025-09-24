import dash
from dash import html

def test_present_header(dash_duo):
    app = dash.Dash(__name__)
    app.layout = html.H1('Pink Morsel Sales')
    dash_duo.start_server(app)
    header_element = dash_duo.find_element('h1')
    assert header_element.text == 'Pink Morsel Sales'