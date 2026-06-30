# src/render/render_engine.py
from __future__ import annotations

import os
import subprocess
import sys


class RenderEngine:
    """
    RenderEngine executes the Manim Community animation framework via a sub-process
    to generate the final video output media from compiled Python source scripts.
    """

    def render(self, source: str, output_dir: str) -> None:
        """
        Executes Manim command line compilation on the provided source script.

        Args:
            source: Path to the executable Python script containing the Manim scene.
            output_dir: Path to the target folder where rendered assets will be saved.

        Raises:
            FileNotFoundError: If the source file does not exist.
            subprocess.CalledProcessError: If the Manim compilation sub-process fails.
        """
        if not os.path.exists(source):
            raise FileNotFoundError(f"Provided source file not found: {source}")

        # Ensure the structural target output directory tree exists
        os.makedirs(output_dir, exist_ok=True)

        # Build command array to invoke the local environment's Manim executable.
        # -q/--quality m: Medium quality (720p 30fps) optimal for rapid testing cycles.
        # --media_dir: Directly intercepts and redirects the compilation outputs.
        command = [
            sys.executable,
            "-m",
            "manim",
            source,
            "AxiomGeneratedScene",
            "-qm",
            "--media_dir",
            os.path.abspath(output_dir),
        ]

        # Execute compilation without suppressing standard descriptors to preserve track traces.
        subprocess.run(command, check=True)
