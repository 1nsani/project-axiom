# src/io/json_loader.py
from __future__ import annotations

import json


class JSONLoader:
    """
    Loader responsible for reading and parsing JSON files from disk
    using the standard library.
    """

    def load(self, path: str) -> dict:
        """
        Reads a JSON file from the given path and returns its contents as a dictionary.

        Raises standard Python exceptions (FileNotFoundError, json.JSONDecodeError)
        if the file does not exist or contains invalid JSON.
        """
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
