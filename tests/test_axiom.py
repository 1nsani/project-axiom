# tests/test_axiom.py
import pytest
from src.models.axiom import Instruction, AxiomProgram


def test_create_instruction():
    """Test 1: Verify successful initialization of an Instruction object with correct fields."""
    instruction = Instruction(
        action="Create",
        target="Block 1",
        parameters={"position": [0, 1], "mass": 1.0}
    )
    assert instruction.action == "Create"
    assert instruction.target == "Block 1"
    assert instruction.parameters == {"position": [0, 1], "mass": 1.0}


def test_create_axiom_program():
    """Test 2: Verify successful initialization of an AxiomProgram holding multiple instructions."""
    inst1 = Instruction(action="Create", target="Board")
    inst2 = Instruction(action="ApplyForce", target="Board")
    program = AxiomProgram(instructions=[inst1, inst2])
    
    assert len(program.instructions) == 2
    assert program.instructions[0].action == "Create"
    assert program.instructions[1].action == "ApplyForce"


def test_axiom_program_to_dict():
    """Test 3: Verify AxiomProgram.to_dict serialization schema and integrity."""
    instruction = Instruction(
        action="Highlight",
        target="Goal",
        parameters={"color": "red"}
    )
    program = AxiomProgram(instructions=[instruction])
    
    expected_dict = {
        "instructions": [
            {
                "action": "Highlight",
                "target": "Goal",
                "parameters": {"color": "red"}
            }
        ]
    }
    assert program.to_dict() == expected_dict


def test_axiom_program_from_dict():
    """Test 4: Verify AxiomProgram.from_dict deserialization builds identical object graph."""
    data = {
        "instructions": [
            {
                "action": "Move",
                "target": "Block 2",
                "parameters": {"velocity": 5.0}
            }
        ]
    }
    program = AxiomProgram.from_dict(data)
    
    assert isinstance(program, AxiomProgram)
    assert len(program.instructions) == 1
    assert isinstance(program.instructions[0], Instruction)
    assert program.instructions[0].action == "Move"
    assert program.instructions[0].target == "Block 2"
    assert program.instructions[0].parameters == {"velocity": 5.0}
