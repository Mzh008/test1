"""Web search plugin."""

from typing import Any

from .base import Plugin


class WebSearchPlugin(Plugin):
    name = "websearch"
    description = "Search the web for information."

    def run(self, query: str, **_: Any) -> str:
        # Placeholder implementation
        return f"Searching the web for: {query}"
