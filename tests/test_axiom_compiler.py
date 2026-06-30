# tests/test_axiom_compiler.py
import pytest
from src.compiler.axiom_compiler import AxiomCompiler
from src.models.axiom import AxiomProgram
from src.models.storyboard import Scene, Storyboard


@pytest.fixture
def sample_storyboard():
    """Fixture to provide a structural Storyboard containing two discrete scenes."""
    scene1 = Scene(
        title="Scene One",
        objects=["Block 1"],
        narration="Introducing Block 1."
    )
    scene2 = Scene(
        title="Scene Two",
        objects=["Board"],
        narration="Introducing Board."
    )
    return Storyboard(scenes=[scene1, scene2])


def test_compiler_returns_axiom_program(sample_storyboard):
    """Test 1: Verify that AxiomCompiler.compile returns an AxiomProgram instance."""
    compiler = AxiomCompiler()
    program = compiler.compile(sample_storyboard)
    assert isinstance(program, AxiomProgram)


def test_compiler_generates_create_instructions(sample_storyboard):
    """Test 2: Verify that object parameters are correctly compiled into 'Create' actions."""
    compiler = AxiomCompiler()
    program = compiler.compile(sample_storyboard)
    
    create_instructions = [i for i in program.instructions if i.action == "Create"]
    assert len(create_instructions) == 2
    assert create_instructions[0].target == "Block 1"
    assert create_instructions[1].target == "Board"


def test_compiler_generates_narrate_instructions(sample_storyboard):
    """Test 3: Verify that scene narrations are correctly compiled into 'Narrate' actions."""
    compiler = AxiomCompiler()
    program = compiler.compile(sample_storyboard)
    
    narrate_instructions = [i for i in program.instructions if i.action == "Narrate"]
    assert len(narrate_instructions) == 2
    assert narrate_instructions[0].parameters["text"] == "Introducing Block 1."
    assert narrate_instructions[1].parameters["text"] == "Introducing Board."


def test_every_scene_ends_with_end_scene(sample_storyboard):
    """Test 4: Verify that each compiled scene sequence is terminated with an 'EndScene' action."""
    compiler = AxiomCompiler()
    program = compiler.compile(sample_storyboard)
    
    # Identify indices of EndScene actions
    end_scene_indices = [idx for idx, i in enumerate(program.instructions) if i.action == "EndScene"]
    
    assert len(end_scene_indices) == 2
    assert program.instructions[end_scene_indices[0]].target == "Scene One"
    assert program.instructions[end_scene_indices[1]].target == "Scene Two"
