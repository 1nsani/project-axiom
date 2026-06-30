# examples/run_storyboard.py
import os
import sys

# Ensure project root is in path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.builder.storyboard_builder import StoryboardBuilder
from src.engine.concept_extractor import ConceptExtractor
from src.parser.markdown_parser import MarkdownParser

if __name__ == "__main__":
    parser = MarkdownParser()
    extractor = ConceptExtractor()
    builder = StoryboardBuilder()
    
    concept = extractor.extract(parser.parse("examples/problems/double_block.md"))
    storyboard = builder.build(concept)
    
    import json
    print(json.dumps(storyboard.to_dict(), indent=2))
