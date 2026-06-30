# tests/test_manim_generator.py
import pytest
from src.generator.manim_generator import ManimGenerator
from src.models.axiom import AxiomProgram, Instruction


@pytest.fixture
def sample_program():
    """Fixture to provide a minimal valid AxiomProgram for generation testing."""
    return AxiomProgram(
        instructions=[
            Instruction(action="Narrate", target="System", parameters={"text": "Hello World"}),
            Instruction(action="Create", target="Block 1", parameters={}),
            Instruction(action="EndScene", target="Scene 1", parameters={})
        ]
    )


def test_generator_returns_string(sample_program):
    """Test 1: Verify that ManimGenerator.generate returns a standard string instance."""
    generator = ManimGenerator()
    result = generator.generate(sample_program)
    assert isinstance(result, str)


def test_generator_output_contains_manim_import(sample_program):
    """Test 2: Verify that the generated source code contains the global manim framework import."""
    generator = ManimGenerator()
    result = generator.generate(sample_program)
    assert "from manim import *" in result


def test_generator_output_contains_scene_subclass(sample_program):
    """Test 3: Verify that the generated code defines exactly one standard Manim Scene subclass."""
    generator = ManimGenerator()
    result = generator.generate(sample_program)
    assert "class AxiomGeneratedScene(Scene):" in result


def test_generator_output_contains_construct_method(sample_program):
    """Test 4: Verify that the generated Scene subclass contains the mandatory construct execution loop."""
    generator = ManimGenerator()
    result = generator.generate(sample_program)
    assert "def construct(self):" in result
