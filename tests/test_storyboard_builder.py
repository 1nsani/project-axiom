# tests/test_storyboard_builder.py
import pytest
from src.builder.storyboard_builder import StoryboardBuilder
from src.models.concept import Concept
from src.models.storyboard import Storyboard


@pytest.fixture
def sample_concept():
    """Fixture to provide a populated Concept object for builder testing."""
    return Concept(
        objects=["Block 1", "Board"],
        quantities=["m=1kg"],
        interactions=["Friction"],
        constraints=["Horizontal"],
        goal=["Find F"]
    )


def test_builder_returns_storyboard(sample_concept):
    """Test 1: Verify that StoryboardBuilder.build returns a Storyboard instance."""
    builder = StoryboardBuilder()
    result = builder.build(sample_concept)
    assert isinstance(result, Storyboard)


def test_storyboard_contains_three_scenes(sample_concept):
    """Test 2: Verify that the generated storyboard contains exactly three scenes."""
    builder = StoryboardBuilder()
    result = builder.build(sample_concept)
    assert len(result.scenes) == 3


def test_scene_titles_are_correct(sample_concept):
    """Test 3: Verify that all scene titles match the deterministic layout design."""
    builder = StoryboardBuilder()
    result = builder.build(sample_concept)
    
    assert result.scenes[0].title == "Scene 1: System Initialization"
    assert result.scenes[1].title == "Scene 2: Core Dynamics and Interactions"
    assert result.scenes[2].title == "Scene 3: Target Boundary Calculation"


def test_scene_narrations_are_not_empty(sample_concept):
    """Test 4: Verify that none of the generated scenes contain empty narration text."""
    builder = StoryboardBuilder()
    result = builder.build(sample_concept)
    
    for scene in result.scenes:
        assert scene.narration != ""
        assert len(scene.narration.strip()) > 0
