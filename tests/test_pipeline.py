# tests/test_pipeline.py
import pytest
from src.engine.concept_extractor import ConceptExtractor
from src.models.concept import Concept
from src.parser.markdown_parser import MarkdownParser
from src.pipeline.pipeline import Pipeline


@pytest.fixture
def sample_md_file(tmp_path):
    """Fixture to create a temporary Markdown file for testing the pipeline."""
    content = """
    # Objects
    - Block 1
    - Board

    # Quantities
    - m = 1 kg

    # Interactions
    - Friction

    # Constraints
    - Horizontal

    # Goal
    - Find F
    """
    file_path = tmp_path / "pipeline_test.md"
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)


@pytest.fixture
def pipeline():
    """Fixture to initialize the pipeline with its required dependencies."""
    parser = MarkdownParser()
    extractor = ConceptExtractor()
    return Pipeline(parser=parser, extractor=extractor)


def test_pipeline_returns_concept(pipeline, sample_md_file):
    """Test 1: Verify the pipeline successfully returns a Concept instance."""
    result = pipeline.run(sample_md_file)
    assert isinstance(result, Concept)


def test_pipeline_preserves_objects(pipeline, sample_md_file):
    """Test 2: Verify that objects are correctly preserved through the pipeline execution."""
    result = pipeline.run(sample_md_file)
    assert result.objects == ["Block 1", "Board"]


def test_pipeline_preserves_goal(pipeline, sample_md_file):
    """Test 3: Verify that the goal is correctly preserved through the pipeline execution."""
    result = pipeline.run(sample_md_file)
    assert result.goal == ["Find F"]
