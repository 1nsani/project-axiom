# src/engine/concept_extractor.py
from __future__ import annotations
from src.models.concept import Concept

class ConceptExtractor:
    """
    Extractor responsible for mapping raw input dictionary data 
    into a structured Concept model.
    """
    
    def extract(self, data: dict) -> Concept:
        """
        Transforms a raw dictionary into a Concept object instance.
        """
        return Concept.from_dict(data)
