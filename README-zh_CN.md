# dash-favicon-plugin

[![GitHub](https://shields.io/badge/license-MIT-informational)](https://github.com/luojiaaoo/dash-favicon-plugin/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/dash-favicon-plugin.svg?color=dark-green)](https://pypi.org/project/dash-favicon-plugin/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

[English](./README.md) | 简体中文

使用Dash Hooks为Dash应用设置网站图标的插件。

## 安装

```bash
pip install dash-favicon-plugin
```

## 使用方法

```python
from dash import Dash
# 导入网站图标插件
from dash_favicon_plugin import setup_favicon_plugin

# 为当前应用启用网站图标插件
setup_favicon_plugin(favicon=r"/assets/favicon.png")

app = dash.Dash(__name__)
# 你的其他应用代码...
```

## 示例

运行包含的示例：

```bash
python example.py
```


## API参考

### `setup_favicon_plugin()`

此函数为你的Dash应用启用网站图标功能。

| 参数      | 类型   | 默认值 | 描述                                                  |
| --------- | ------ | ------ | ---------------------------------------------------- |
| `favicon` | `str`  | `-`    | `网站图标的路径名，支持svg、png、ico、gif等格式。` |