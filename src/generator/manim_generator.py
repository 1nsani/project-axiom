# src/generator/manim_generator.py
from __future__ import annotations

from src.models.axiom import AxiomProgram


class ManimGenerator:
    """
    Generator responsible for compiling an AxiomProgram intermediate representation
    into an executable Manim Python script string.
    """

    def generate(self, program: AxiomProgram) -> str:
        """
        Translates the intermediate AxiomProgram instructions into a standard,
        executable Manim Python script string.
        """
        lines = [
            "from manim import *",
            "",
            "",
            "class AxiomGeneratedScene(Scene):",
            "    def construct(self):",
            "        # Track active on-screen objects by their target ID keys",
            "        deployed_objects = {}",
        ]

        for inst in program.instructions:
            action = inst.action
            target = inst.target
            params = inst.parameters

            if action == "Narrate":
                text = params.get("text", "").replace('"', '\\"')
                lines.append(f'        # Narrate: {text}')
                # Create a temporary centered text display for the narration script
                lines.append(f'        narrative_text = Text("{text}", font_size=24).to_edge(DOWN)')
                lines.append("        self.play(Write(narrative_text))")
                lines.append("        self.wait(2)")
                lines.append("        self.play(FadeOut(narrative_text))")

            elif action == "Create":
                # Only construct the visual asset if it has not already been added to the graph
                lines.append(f'        if "{target}" not in deployed_objects:')
                lines.append(f'            obj = Square().set_color(BLUE)')
                lines.append(f'            lbl = Text("{target}", font_size=18).move_to(obj.get_center())')
                lines.append(f'            deployed_objects["{target}"] = VGroup(obj, lbl)')
                lines.append(f'            self.play(Create(deployed_objects["{target}"]))')

            elif action == "EndScene":
                lines.append(f'        # Boundary marker for: {target}')
                lines.append("        self.wait(1)")
                lines.append("")

        # Fallback empty structural implementation if the program lacks any execution steps
        if len(program.instructions) == 0:
            lines.append("        pass")

        return "\n".join(lines)
