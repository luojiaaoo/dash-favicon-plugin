from dash import hooks
import feffery_utils_components as fuc


def setup_favicon_plugin(favicon: str) -> None:
    """
    设置dash应用的favicon.

    Parameters:
        favicon_filepath 设置favicon文件路径。
    """

    @hooks.layout()
    def update_layout(layout):
        """注入layout"""
        component_set_favicon = fuc.FefferySetFavicon(favicon=favicon)
        if isinstance(layout, list):
            return [component_set_favicon, *layout]
        return [component_set_favicon, layout]
