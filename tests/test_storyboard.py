# tests/test_storyboard.py
import pytest
from src.models.storyboard import Scene, Storyboard


def test_create_scene():
    """Test 1: Verify successful initialization of a Scene object with correct fields."""
    scene = Scene(
        title="Scene 1",
        goal="Introduce objects",
        objects=["Block 1", "Board"],
        actions=["Create(Board)", "Create(Block1)"],
        narration="We introduce the system."
    )
    assert scene.title == "Scene 1"
    assert scene.goal == "Introduce objects"
    assert scene.objects == ["Block 1", "Board"]
    assert scene.actions == ["Create(Board)", "Create(Block1)"]
    assert scene.narration == "We introduce the system."


def test_create_storyboard():
    """Test 2: Verify successful initialization of a Storyboard holding multiple scenes."""
    scene1 = Scene(title="Scene 1")
    scene2 = Scene(title="Scene 2")
    storyboard = Storyboard(scenes=[scene1, scene2])
    
    assert len(storyboard.scenes) == 2
    assert storyboard.scenes[0].title == "Scene 1"
    assert storyboard.scenes[1].title == "Scene 2"


def test_storyboard_to_dict():
    """Test 3: Verify Storyboard.to_dict serialization schema and integrity."""
    scene = Scene(
        title="Scene 1",
        goal="Goal 1",
        objects=["Floor"],
        actions=["Create(Floor)"],
        narration="Floor init."
    )
    storyboard = Storyboard(scenes=[scene])
    
    expected_dict = {
        "scenes": [
            {
                "title": "Scene 1",
                "goal": "Goal 1",
                "objects": ["Floor"],
                "actions": ["Create(Floor)"],
                "narration": "Floor init."
            }
        ]
    }
    assert storyboard.to_dict() == expected_dict


def test_storyboard_from_dict():
    """Test 4: Verify Storyboard.from_dict deserialization builds identical object graph."""
    data = {
        "scenes": [
            {
                "title": "Scene 1",
                "goal": "Goal 1",
                "objects": ["Board"],
                "actions": ["Create(Board)"],
                "narration": "Board init."
            }
        ]
    }
    storyboard = Storyboard.from_dict(data)
    
    assert isinstance(storyboard, Storyboard)
    assert len(storyboard.scenes) == 1
    assert isinstance(storyboard.scenes[0], Scene)
    assert storyboard.scenes[0].title == "Scene 1"
    assert storyboard.scenes[0].objects == ["Board"]
