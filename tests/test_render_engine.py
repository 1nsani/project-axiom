# tests/test_render_engine.py
import pytest
from unittest.mock import patch, MagicMock
from src.render.render_engine import RenderEngine


def test_render_engine_instantiation():
    """Test 1: Verify that a RenderEngine instance can be successfully instantiated."""
    engine = RenderEngine()
    assert isinstance(engine, RenderEngine)


def test_render_accepts_two_string_arguments():
    """Test 2: Verify method signature and successful invocation with valid string paths using mocking."""
    engine = RenderEngine()
    
    with patch("os.path.exists", return_value=True), \
         patch("os.makedirs") as mock_makedirs, \
         patch("subprocess.run") as mock_run:
        
        # Test signature acceptance and execution path routing
        engine.render("dummy_source.py", "dummy_output_dir")
        
        mock_makedirs.assert_called_once_with("dummy_output_dir", exist_ok=True)
        mock_run.assert_called_once()


def test_invalid_source_path_raises_exception():
    """Test 3: Verify that an invalid or non-existent source path correctly triggers a FileNotFoundError."""
    engine = RenderEngine()
    
    with patch("os.path.exists", return_value=False):
        with pytest.raises(FileNotFoundError) as exc_info:
            engine.render("non_existent_file.py", "output_dir")
        
        assert "Provided source file not found" in str(exc_info.value)
