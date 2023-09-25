import pandas_datareader.data as web
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import datetime

# App layout
app = dash.Dash()
app.title = "Stock Prices Visualization"
app.layout = html.Div(children=[
    html.H1("Stock Prices Visualization Dashboard"),
    html.H4("Enter the stock name here "),
    dcc.Input(id="input", value="", type="text"),
    html.Div(id="output-graph")
])


# App interaction with user
@app.callback(
    Output(component_id="output-graph", component_property='children'),
    [Input(component_id="input", component_property="value")]
)
def update_value(input_data):
    start = datetime.datetime(2023, 9, 1)
    end = datetime.datetime.now()

    data_source = "yahoo"

    # fetch data from yahoo finance api
    url = 'https://query1.finance.yahoo.com/v7/finance/download/{}?period1={}&period2={}&interval=1d&events=history'

    df = web.DataReader(input_data, data_source, start, end, api_key=url)

    # return the graph
    return dcc.Graph(id="demo", figure={'data':
                                        [{'x': df.index, 'y': df.Close,
                                            'type': 'line', 'name': input_data}, ],
                                        'layout': {'title': input_data}})


if __name__ == "__main__":
    app.run_server(debug=True)
