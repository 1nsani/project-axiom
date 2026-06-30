# examples/run_pipeline.py
import os
import sys

# Ensure project root is in path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.engine.concept_extractor import ConceptExtractor
from src.parser.markdown_parser import MarkdownParser
from src.pipeline.pipeline import Pipeline

if __name__ == "__main__":
    parser = MarkdownParser()
    extractor = ConceptExtractor()
    pipeline = Pipeline(parser=parser, extractor=extractor)
    
    concept = pipeline.run("examples/problems/double_block.md")
    print(concept)
