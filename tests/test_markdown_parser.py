# tests/test_markdown_parser.py
import pytest
from src.parser.markdown_parser import MarkdownParser


@pytest.fixture
def valid_md_file(tmp_path):
    """Fixture to create a temporary valid Markdown file for testing."""
    md_content = """
    # Objects
    - Block 1
    - Board

    # Quantities
    - m = 1 kg
    - F

    # Interactions
    - Board ↔ Block 1 : Friction

    # Constraints
    - Horizontal motion

    # Goal
    - Find F_min
    """
    file_path = tmp_path / "test_concept.md"
    file_path.write_text(md_content, encoding="utf-8")
    return str(file_path)


def test_parse_valid_markdown(valid_md_file):
    """Test 1: Verify parsing a valid Markdown file executes without errors."""
    parser = MarkdownParser()
    result = parser.parse(valid_md_file)
    assert result is not None


def test_dictionary_structure_and_keys(valid_md_file):
    """Test 3: Verify the returned object is a dictionary with the exact required keys."""
    parser = MarkdownParser()
    result = parser.parse(valid_md_file)
    
    assert isinstance(result, dict)
    expected_keys = {"objects", "quantities", "interactions", "constraints", "goal"}
    assert set(result.keys()) == expected_keys


def test_extraction_of_all_sections(valid_md_file):
    """Test 2: Verify all five sections are extracted correctly with valid data."""
    parser = MarkdownParser()
    result = parser.parse(valid_md_file)
    
    assert result["objects"] == ["Block 1", "Board"]
    assert result["quantities"] == ["m = 1 kg", "F"]
    assert result["interactions"] == ["Board ↔ Block 1 : Friction"]
    assert result["constraints"] == ["Horizontal motion"]
    assert result["goal"] == ["Find F_min"]
