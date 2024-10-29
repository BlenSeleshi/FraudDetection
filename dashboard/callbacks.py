from dash import Input, Output
import plotly.express as px

def register_callbacks(app, data):
    @app.callback(
        Output("fraud-trend-chart", "figure"),
        Input("interval-component", "n_intervals")
    )
    def update_fraud_trend_chart(n):
        # Generate fraud trend line chart
        fraud_trend = data.groupby(data['purchase_time'].dt.date)['class'].sum().reset_index()
        fig = px.line(fraud_trend, x="purchase_time", y="class", title="Fraud Cases Over Time")
        return fig

    @app.callback(
        Output("geo-fraud-chart", "figure"),
        Input("interval-component", "n_intervals")
    )
    def update_geo_fraud_chart(n):
        # Create a map-based chart for geographic fraud analysis
        geo_data = data.groupby("country")["class"].sum().reset_index()
        fig = px.choropleth(geo_data, locations="country", color="class", title="Fraud by Country")
        return fig

    @app.callback(
        Output("device-browser-fraud-chart", "figure"),
        Input("interval-component", "n_intervals")
    )
    def update_device_browser_chart(n):
        # Create a bar chart for device and browser-based fraud
        device_data = data.groupby(["device_id", "browser"])["class"].sum().reset_index()
        fig = px.bar(device_data, x="device_id", y="class", color="browser", title="Fraud by Device and Browser")
        return fig
