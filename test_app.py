import dash
from dash import html, dcc

def test_present_header(dash_duo):
    app = dash.Dash(__name__)
    app.layout = html.H1('Pink Morsel Sales')
    dash_duo.start_server(app)
    header_element = dash_duo.find_element('h1')
    assert header_element.text == 'Pink Morsel Sales'

def test_visualisation(dash_duo):
    app = dash.Dash(__name__)
    app.layout = dcc.Graph(id='graph-output', style={'padding': '20px'})
    dash_duo.start_server(app)
    graph_element = dash_duo.find_element('#graph-output')
    assert graph_element is not None

def test_region_picker(dash_duo):
    colors = {
    'background': '#FACBAA',
    'text': '#FFFFFF'
    }
    app = dash.Dash(__name__)
    app.layout = dcc.RadioItems(
            ['north', 'south', 'east', 'west', 'all'],
            'all',
            id='radio-items-input',
            inline=True,
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        )
    dash_duo.start_server(app)
    radio_items_element = dash_duo.find_element('#radio-items-input')
    assert radio_items_element is not None