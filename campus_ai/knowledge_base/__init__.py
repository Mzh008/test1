"""Knowledge base implementations."""

from .base import KnowledgeBase
from .in_memory import InMemoryKnowledgeBase

__all__ = ["KnowledgeBase", "InMemoryKnowledgeBase"]
