from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('./data/sales.csv')
df = df.sort_values(by='date')

app = Dash(__name__)

fig = px.line(df, x='date', y='sales', title='pink morsel sales')

app.layout = html.Div(children=[
    html.H1(children='pink morsel sales'),
    dcc.Graph(
        id='line-chart',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run(debug=True)