# src/parser/markdown_parser.py
from __future__ import annotations


class MarkdownParser:
    """
    Parser responsible for converting structured Markdown text files
    into standard dictionaries for the Axiom pipeline.
    """

    def parse(self, path: str) -> dict[str, list[str]]:
        """
        Reads a markdown file and extracts bullet points under specific headings.
        
        Returns a dictionary with canonical keys and list of strings as values.
        """
        result: dict[str, list[str]] = {
            "objects": [],
            "quantities": [],
            "interactions": [],
            "constraints": [],
            "goal": []
        }

        valid_headers = {
            "# objects": "objects",
            "# quantities": "quantities",
            "# interactions": "interactions",
            "# constraints": "constraints",
            "# goal": "goal"
        }

        current_key = None

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cleaned = line.strip()

                # Ignore empty lines and comments
                if not cleaned or cleaned.startswith("
