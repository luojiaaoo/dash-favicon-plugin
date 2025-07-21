# dash-favicon-plugin

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/CNFeffery/dash-offline-detect-plugin/blob/main/LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Set favicon plugin for Dash applications using Dash Hooks.

## Installation

```bash
pip install dash-favicon-plugin
```

## Usage

```python
from dash import Dash
# Import the favicon plugin
from dash_favicon_plugin import setup_favicon_plugin

# Enable the favicon plugin for the current app
setup_favicon_plugin(favicon=r"/assets/favicon.png")

app = dash.Dash(__name__)
# Rest of your app code...
```

## Example

Run the included example:

```bash
python example.py
```

<center><img src="./images/demo.gif" /></center>

## API Reference

### `setup_favicon_plugin()`

This function enables the favicon feature for your Dash application.

| Parameter | Type  | Default | Description                                                  |
| --------- | ----- | ------- | ------------------------------------------------------------ |
| `favicon` | `str` | `-`     | `pathname of favicon,  supporting svg, png, ico, gif formats.` |