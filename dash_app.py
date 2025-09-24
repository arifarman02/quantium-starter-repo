from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/sales.csv')
df = df.sort_values(by='date')

app = Dash(__name__)

colors = {
    'background': '#FACBAA',
    'text': '#FFFFFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Pink Morsel Sales',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'paddingTop': '20px',
            'fontSize': '2.5rem'
        }
    ),
    html.Div(children=[
        html.P(
            'Select a region:',
            style={'textAlign': 'center', 'color': colors['text']}
        ),
        dcc.RadioItems(
            ['north', 'south', 'east', 'west', 'all'],
            'all',
            id='radio-items-input',
            inline=True,
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),
        dcc.Graph(
            id='graph-output',
            style={'padding': '20px'}
        )
    ], style={'padding': 10, 'flex': 1, 'textAlign': 'center'}),
])

@callback(
    Output('graph-output', 'figure'),
    Input('radio-items-input', 'value')
)
def update_graph(region_value):
    if region_value == 'all':
        dff = df
    else:
        dff = df[df['region'] == region_value]
    
    fig = px.line(dff, x='date', y='sales', title=f'pink morsel sales in {region_value}')
    return fig

if __name__ == '__main__':
    app.run(debug=True)