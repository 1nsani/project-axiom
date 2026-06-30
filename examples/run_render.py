# examples/run_render.py
import os
import sys

# Ensure project root is in path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.render.render_engine import RenderEngine

if __name__ == "__main__":
    source_file = "examples/generated/main.py"
    output_directory = "output"
    
    # Instantiate the execution abstraction and trigger the compilation loop
    engine = RenderEngine()
    engine.render(source=source_file, output_dir=output_directory)
