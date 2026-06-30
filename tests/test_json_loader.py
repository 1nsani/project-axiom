# tests/test_json_loader.py
import pytest
from src.io.json_loader import JSONLoader


def test_json_loader_returns_dict():
    """Verify that JSONLoader successfully parses the file and returns a dictionary."""
    loader = JSONLoader()
    result = loader.load("examples/input/double_block_input.json")
    assert isinstance(result, dict)


def test_json_loader_has_required_keys():
    """Verify that the parsed dictionary contains all canonical concept keys."""
    loader = JSONLoader()
    result = loader.load("examples/input/double_block_input.json")
    required_keys = {"objects", "quantities", "interactions", "constraints", "goal"}
    assert required_keys.issubset(result.keys())
