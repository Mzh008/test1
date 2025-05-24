"""Retrieval-Augmented Generation plugin."""

from typing import Any

from .base import Plugin
from ..knowledge_base.base import KnowledgeBase


class RAGPlugin(Plugin):
    name = "rag"
    description = "Retrieve information from a knowledge base and generate an answer."

    def __init__(self, knowledge_base: KnowledgeBase | None = None) -> None:
        self.knowledge_base = knowledge_base

    def run(self, query: str, **_: Any) -> str:
        if not self.knowledge_base:
            return "No knowledge base configured."
        docs = self.knowledge_base.search(query)
        # In a real implementation, you'd pass `docs` to an LLM.
        return "\n".join(docs)
