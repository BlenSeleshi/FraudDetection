from dash import html, dcc

def get_layout():
    return html.Div([
        html.H1("Fraud Detection Dashboard"),
        html.Div([
            html.Div(id="total-transactions", className="summary-box"),
            html.Div(id="total-fraud-cases", className="summary-box"),
            html.Div(id="fraud-percentage", className="summary-box")
        ], className="summary-container"),
        
        dcc.Graph(id="fraud-trend-chart"),
        dcc.Graph(id="geo-fraud-chart"),
        dcc.Graph(id="device-browser-fraud-chart"),
        
        # Add Interval component for auto-refresh
        dcc.Interval(
            id="interval-component",
            interval=60*1000,  # Update every minute
            n_intervals=0
        )
    ])
