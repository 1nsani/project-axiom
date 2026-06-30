# tests/models/test_concept.py
import pytest
from src.models.concept import Concept

def test_create_concept():
    """Test successful initialization of a Concept object."""
    concept = Concept(
        objects=["Board", "Block"],
        quantities=["Mass"],
        interactions=["Friction"],
        constraints=["Static"],
        goal=["Find F"]
    )
    assert concept.objects == ["Board", "Block"]
    assert concept.quantities == ["Mass"]
    assert concept.interactions == ["Friction"]
    assert concept.constraints == ["Static"]
    assert concept.goal == ["Find F"]

def test_to_dict():
    """Test that to_dict returns a valid dictionary matching the object state."""
    concept = Concept(objects=["Board"], goal=["Find F"])
    expected = {
        "objects": ["Board"],
        "quantities": [],
        "interactions": [],
        "constraints": [],
        "goal": ["Find F"]
    }
    assert concept.to_dict() == expected

def test_from_dict():
    """Test that from_dict correctly hydrates a Concept object from valid data."""
    data = {
        "objects": ["Board", "Block"],
        "quantities": ["m"],
        "interactions": ["friction"],
        "constraints": ["no-slip"],
        "goal": ["p+q"]
    }
    concept = Concept.from_dict(data)
    assert isinstance(concept, Concept)
    assert concept.objects == ["Board", "Block"]
    assert concept.goal == ["p+q"]
