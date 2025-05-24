"""Main agent and plugin management."""

from importlib import import_module
from typing import Dict, Any, List

from .plugins.base import Plugin


class CampusAgent:
    """Simple agent that dispatches tools provided as plugins."""

    def __init__(self, plugin_paths: List[str] | None = None) -> None:
        self.plugins: Dict[str, Plugin] = {}
        if plugin_paths:
            for path in plugin_paths:
                self.load_plugin(path)

    def load_plugin(self, dotted_path: str) -> None:
        """Load a plugin from a dotted module path."""
        module_path, cls_name = dotted_path.rsplit(".", 1)
        module = import_module(module_path)
        cls = getattr(module, cls_name)
        if not issubclass(cls, Plugin):
            raise TypeError(f"{cls_name} is not a Plugin")
        plugin: Plugin = cls()
        self.plugins[plugin.name] = plugin

    def available_tools(self) -> List[str]:
        return list(self.plugins.keys())

    def run_tool(self, name: str, **kwargs: Any) -> Any:
        if name not in self.plugins:
            raise KeyError(f"Plugin {name} not loaded")
        plugin = self.plugins[name]
        return plugin.run(**kwargs)
