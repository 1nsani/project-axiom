# src/builder/storyboard_builder.py
from __future__ import annotations

from src.models.concept import Concept
from src.models.storyboard import Scene, Storyboard


class StoryboardBuilder:
    """
    Builder responsible for deterministically transforming a physics Concept model
    into a structured, sequential three-scene Storyboard for the Axiom pipeline.
    """

    def build(self, concept: Concept) -> Storyboard:
        """
        Builds a complete three-scene Storyboard from the provided Concept instance.
        """
        # Format comma-separated representations for clean strings
        objects_str = ", ".join(concept.objects) if concept.objects else "system entities"
        interactions_str = ", ".join(concept.interactions) if concept.interactions else "system forces"
        goals_str = ", ".join(concept.goal) if concept.goal else "required solutions"

        # Scene 1: System Initialization
        scene_1 = Scene(
            title="Scene 1: System Initialization",
            goal="Introduce and visualize the baseline configuration of physical objects.",
            objects=concept.objects.copy(),
            actions=[f"Create({obj})" for obj in concept.objects],
            narration=f"We initialize the physical environment and introduce the core components of the system: {objects_str}."
        )

        # Scene 2: Critical Interactions
        scene_2 = Scene(
            title="Scene 2: Core Dynamics and Interactions",
            goal="Isolate and evaluate the acting force vectors and coupling interactions.",
            objects=concept.objects.copy(),
            actions=[f"ApplyInteraction({inter})" for inter in concept.interactions],
            narration=f"Analyzing the state vectors reveals the following active interactions and operational constraints: {interactions_str}."
        )

        # Scene 3: Problem Target Mapping
        scene_3 = Scene(
            title="Scene 3: Target Boundary Calculation",
            goal="Define and highlight the definitive target variables required to resolve the problem.",
            objects=concept.objects.copy(),
            actions=[f"HighlightGoal({target})" for target in concept.goal],
            narration=f"To solve the physics problem, we must resolve the mathematical boundaries for our primary objectives: {goals_str}."
        )

        return Storyboard(scenes=[scene_1, scene_2, scene_3])
