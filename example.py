import dash
from dash import html

# Import the favicon plugin
from dash_favicon_plugin import setup_favicon_plugin

# Enable the favicon plugin for the current app
setup_favicon_plugin(favicon=r"/assets/favicon.png")

app = dash.Dash(__name__)

app.layout = html.Div("Test App.", style={"padding": 50})

if __name__ == "__main__":
    app.run()