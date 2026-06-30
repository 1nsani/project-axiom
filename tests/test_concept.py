# tests/test_concept.py
import pytest
from src.models.concept import Concept

def test_concept_initialization():
    """Test that a Concept object stores all fields correctly upon initialization."""
    concept = Concept(
        objects=["Block 1", "Block 2"],
        quantities=["m=1kg"],
        interactions=["friction"],
        constraints=["horizontal motion"],
        goal=["find F_min"]
    )
    assert concept.objects == ["Block 1", "Block 2"]
    assert concept.quantities == ["m=1kg"]
    assert concept.interactions == ["friction"]
    assert concept.constraints == ["horizontal motion"]
    assert concept.goal == ["find F_min"]

def test_to_dict():
    """Test that to_dict returns the expected dictionary structure."""
    concept = Concept(
        objects=["Board"],
        quantities=["g=10"],
        interactions=["normal"],
        constraints=["frictionless"],
        goal=["p+q"]
    )
    expected_dict = {
        "objects": ["Board"],
        "quantities": ["g=10"],
        "interactions": ["normal"],
        "constraints": ["frictionless"],
        "goal": ["p+q"]
    }
    assert concept.to_dict() == expected_dict

def test_from_dict():
    """Test that from_dict correctly hydrates a Concept object from a dictionary."""
    data = {
        "objects": ["Floor"],
        "quantities": ["F"],
        "interactions": ["contact"],
        "constraints": ["no-slip"],
        "goal": ["F_max"]
    }
    concept = Concept.from_dict(data)
    assert isinstance(concept, Concept)
    assert concept.objects == ["Floor"]
    assert concept.quantities == ["F"]
    assert concept.interactions == ["contact"]
    assert concept.constraints == ["no-slip"]
    assert concept.goal == ["F_max"]        "interactions": ["friction"],
        "constraints": ["no-slip"],
        "goal": ["p+q"]
    }
    concept = Concept.from_dict(data)
    assert isinstance(concept, Concept)
    assert concept.objects == ["Board", "Block"]
    assert concept.goal == ["p+q"]
