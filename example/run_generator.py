# examples/run_generator.py
import os
import sys

# Ensure project root is in path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.builder.storyboard_builder import StoryboardBuilder
from src.compiler.axiom_compiler import AxiomCompiler
from src.engine.concept_extractor import ConceptExtractor
from src.generator.manim_generator import ManimGenerator
from src.parser.markdown_parser import MarkdownParser

if __name__ == "__main__":
    parser = MarkdownParser()
    extractor = ConceptExtractor()
    builder = StoryboardBuilder()
    compiler = AxiomCompiler()
    generator = ManimGenerator()
    
    concept = extractor.extract(parser.parse("examples/problems/double_block.md"))
    storyboard = builder.build(concept)
    program = compiler.compile(storyboard)
    manim_code = generator.generate(program)
    
    print(manim_code)
