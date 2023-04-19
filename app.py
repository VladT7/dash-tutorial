from dash import Dash
from dash import dcc
from dash import html
import pandas as pd

data = pd.read_csv("dash-tutorial/avocado.csv")
data = data.query("type == 'organic' and region == 'Albany'")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")

data.sort_values(by="Date", inplace=True)

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Avocado Prices"),
        html.P(
            children="An interactive graph showing the average price of avocados in Albany, NY between 2015 and 2018."
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    }
                ],
                "layout": {"title": "Average Price of Avocados in Albany, NY"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    }
                ],
                "layout": {"title": "Avocados sold"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
