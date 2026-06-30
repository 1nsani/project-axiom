# src/compiler/axiom_compiler.py
from __future__ import annotations

from src.models.axiom import AxiomProgram, Instruction
from src.models.storyboard import Storyboard, Scene


class AxiomCompiler:
    """
    Compiler responsible for translating a high-level, human-readable Storyboard
    into a low-level, machine-executable AxiomProgram intermediate representation.
    """

    def compile(self, storyboard: Storyboard) -> AxiomProgram:
        """
        Compiles a complete Storyboard sequence into a sequential AxiomProgram.
        
        Transforms high-level narrative structure and asset definitions into a series
        of atomic, programmatic execution instructions.
        """
        compiled_instructions: list[Instruction] = []

        for scene in storyboard.scenes:
            # 1. Compile narration instruction if present
            if scene.narration:
                compiled_instructions.append(
                    Instruction(
                        action="Narrate",
                        target="System",
                        parameters={"text": scene.narration}
                    )
                )

            # 2. Compile entity creation instructions deterministically
            for obj in scene.objects:
                compiled_instructions.append(
                    Instruction(
                        action="Create",
                        target=obj,
                        parameters={}
                    )
                )

            # 3. Finalize scene context tracking boundaries
            scene_id = scene.title if scene.title else "Scene"
            compiled_instructions.append(
                Instruction(
                    action="EndScene",
                    target=scene_id,
                    parameters={}
                )
            )

        return AxiomProgram(instructions=compiled_instructions)
