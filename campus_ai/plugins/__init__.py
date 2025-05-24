"""Plugin implementations."""

from .rag import RAGPlugin
from .gpa import GPACalculatorPlugin
from .research import ResearchPlugin
from .websearch import WebSearchPlugin

__all__ = [
    "RAGPlugin",
    "GPACalculatorPlugin",
    "ResearchPlugin",
    "WebSearchPlugin",
]
