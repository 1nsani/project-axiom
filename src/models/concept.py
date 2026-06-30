# src/models/concept.py
from __future__ import annotations

from dataclasses import dataclass, field

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
