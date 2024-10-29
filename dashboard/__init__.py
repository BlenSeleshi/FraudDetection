from dash import Dash
from .layout import get_layout
from .callbacks import register_callbacks

def create_dashboard(server, data):
    # Initialize Dash
    app = Dash(server=server, routes_pathname_prefix="/dashboard/")
    
    # Set the layout of the Dash app
    app.layout = get_layout()

    # Register callbacks, passing the data
    register_callbacks(app, data)
    
    return server
