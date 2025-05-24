"""GPA calculator plugin."""

from typing import Any, Iterable, Tuple

from .base import Plugin


class GPACalculatorPlugin(Plugin):
    name = "gpa"
    description = "Calculate weighted GPA for a set of courses."

    def run(self, grades: Iterable[Tuple[float, float]], **_: Any) -> float:
        """Compute GPA from `(grade, weight)` pairs."""
        total_weight = 0.0
        total_score = 0.0
        for grade, weight in grades:
            total_weight += weight
            total_score += grade * weight
        if total_weight == 0:
            return 0.0
        return total_score / total_weight
