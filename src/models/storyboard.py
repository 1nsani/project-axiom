# src/models/storyboard.py
from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any


@dataclass
class Scene:
    """
    Data model representing a single instructional scene within a storyboard.
    """
    title: str = ""
    goal: str = ""
    objects: list[str] = field(default_factory=list)
    actions: list[str] = field(default_factory=list)
    narration: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Returns a standard dictionary representation of the Scene instance."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Scene:
        """Creates a Scene instance from a dictionary."""
        return cls(
            title=data.get("title", ""),
            goal=data.get("goal", ""),
            objects=data.get("objects", []),
            actions=data.get("actions", []),
            narration=data.get("narration", "")
        )


@dataclass
class Storyboard:
    """
    Data model representing a complete sequential collection of Scenes.
    """
    scenes: list[Scene] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Returns a standard dictionary representation of the Storyboard instance."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Storyboard:
        """Creates a Storyboard instance from a dictionary data structure."""
        raw_scenes = data.get("scenes", [])
        return cls(
            scenes=[Scene.from_dict(scene_data) for scene_data in raw_scenes]
        )
