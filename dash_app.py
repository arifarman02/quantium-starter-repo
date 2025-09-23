from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/sales.csv')
df = df.sort_values(by='date')

app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='pink morsel sales'),
    dcc.RadioItems(['north', 'south', 'east', 'west', 'all'], 'all', id='radio-items-input'),
    dcc.Graph(id='graph-output')
], style={'padding': 10, 'flex': 1})

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