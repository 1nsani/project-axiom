# src/models/concept.py
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any

@dataclass
class Concept:
    """
    Data model representing the deconstructed physical components, 
    interactions, and objectives of a physics problem for the Axiom pipeline.
    """
    objects: list[str] = field(default_factory=list)
    quantities: list[str] = field(default_factory=list)
    interactions: list[str] = field(default_factory=list)
    constraints: list[str] = field(default_factory=list)
    goal: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a dictionary representation of the Concept instance.
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Concept:
        """
        Creates a Concept instance from a dictionary, ensuring all fields are populated.
        """
        return cls(
            objects=data.get("objects", []),
            quantities=data.get("quantities", []),
            interactions=data.get("interactions", []),
            constraints=data.get("constraints", []),
            goal=data.get("goal", [])
        )
