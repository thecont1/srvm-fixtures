from dash import Dash, dcc, html
import plotly.express as px

app = Dash(__name__)

fig = px.line(
    x=[1, 2, 3, 4, 5],
    y=[2, 1, 4, 3, 6],
    title="srvm fixture x7 - dash",
    labels={"x": "sample", "y": "value"},
)

app.layout = html.Div(
    [
        html.H1("srvm fixture x7 - dash"),
        html.P("Served by srvm's Dash fixture on port 8050."),
        dcc.Graph(figure=fig),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
