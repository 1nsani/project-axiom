# src/pipeline/pipeline.py
from __future__ import annotations

from src.engine.concept_extractor import ConceptExtractor
from src.models.concept import Concept
from src.parser.markdown_parser import MarkdownParser


class Pipeline:
    """
    Orchestrator class that executes the Axiom compilation pipeline by
    parsing a markdown asset and extracting its structured core physics concepts.
    """

    def __init__(
        self, parser: MarkdownParser, extractor: ConceptExtractor
    ) -> None:
        """
        Initializes the pipeline using dependency injection.
        """
        self._parser = parser
        self._extractor = extractor

    def run(self, path: str) -> Concept:
        """
        Executes the full parsing and extraction pipeline for a given markdown file.
        """
        raw_data = self._parser.parse(path)
        return self._extractor.extract(raw_data)
