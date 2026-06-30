# src/models/axiom.py
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class Instruction:
    """
    Data model representing a discrete structural render or vector action 
    within the compiled Axiom execution sequence.
    """
    action: str = ""
    target: str = ""
    parameters: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Returns a standard dictionary representation of the Instruction instance."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Instruction:
        """Creates an Instruction instance from a dictionary representation."""
        return cls(
            action=data.get("action", ""),
            target=data.get("target", ""),
            parameters=data.get("parameters", {})
        )


@dataclass
class AxiomProgram:
    """
    Data model representing a compiled array of sequential Instructions 
    ready to be fed into the final geometric layout and animation rendering engine.
    """
    instructions: list[Instruction] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Returns a standard dictionary representation of the AxiomProgram instance."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AxiomProgram:
        """Creates an AxiomProgram instance from a structured dictionary data input."""
        raw_instructions = data.get("instructions", [])
        return cls(
            instructions=[Instruction.from_dict(inst) for inst in raw_instructions]
        )
