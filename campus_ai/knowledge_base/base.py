"""Knowledge base interface."""

from abc import ABC, abstractmethod
from typing import List


class KnowledgeBase(ABC):
    """Abstract knowledge base for retrieving documents."""

    @abstractmethod
    def search(self, query: str) -> List[str]:
        """Return a list of documents matching the query."""
        raise NotImplementedError
