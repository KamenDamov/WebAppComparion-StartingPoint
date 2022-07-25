from dash import Dash, dcc, html

app = Dash(__name__)

app.layout = html.Div([
    dcc.Textarea(
        id='textarea-example',
        value='Input text here',
        style={'width': '25%', 'height': 100},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
])


if __name__ == '__main__':
    app.run_server(debug=True)