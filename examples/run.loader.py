# examples/run_loader.py
import os
import sys

# Ensure project root is in path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.io.json_loader import JSONLoader

if __name__ == "__main__":
    loader = JSONLoader()
    data = loader.load("examples/input/double_block_input.json")
    print(data)
