"""In-memory knowledge base for demonstration."""

from typing import List

from .base import KnowledgeBase


class InMemoryKnowledgeBase(KnowledgeBase):
    def __init__(self, documents: List[str] | None = None) -> None:
        self.documents = documents or []

    def add_document(self, doc: str) -> None:
        self.documents.append(doc)

    def search(self, query: str) -> List[str]:
        query_lower = query.lower()
        return [doc for doc in self.documents if query_lower in doc.lower()]
