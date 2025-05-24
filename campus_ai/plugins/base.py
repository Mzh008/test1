"""Base classes for plugins."""

from abc import ABC, abstractmethod
from typing import Any


class Plugin(ABC):
    """Abstract plugin interface."""

    name: str = "plugin"
    description: str = ""

    @abstractmethod
    def run(self, **kwargs: Any) -> Any:
        """Execute the plugin with provided parameters."""
        raise NotImplementedError
