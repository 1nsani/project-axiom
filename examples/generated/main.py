from manim import *


class AxiomGeneratedScene(Scene):
    def construct(self):
        # Track active on-screen objects by their target ID keys
        deployed_objects = {}
        
        # Narrate: We initialize the physical environment and introduce the core components of the system: Block 1, Block 2, Board, Floor.
        narrative_text = Text("We initialize the physical environment and introduce the core components of the system: Block 1, Block 2, Board, Floor.", font_size=24).to_edge(DOWN)
        self.play(Write(narrative_text))
        self.wait(2)
        self.play(FadeOut(narrative_text))
        if "Block 1" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Block 1", font_size=18).move_to(obj.get_center())
            deployed_objects["Block 1"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Block 1"]))
        if "Block 2" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Block 2", font_size=18).move_to(obj.get_center())
            deployed_objects["Block 2"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Block 2"]))
        if "Board" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Board", font_size=18).move_to(obj.get_center())
            deployed_objects["Board"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Board"]))
        if "Floor" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Floor", font_size=18).move_to(obj.get_center())
            deployed_objects["Floor"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Floor"]))
        # Boundary marker for: Scene 1: System Initialization
        self.wait(1)

        # Narrate: Analyzing the state vectors reveals the following active interactions and operational constraints: Board ↔ Block 1 : Friction, Board ↔ Block 2 : Friction, Floor ↔ Board : Normal, Force F → Board.
        narrative_text = Text("Analyzing the state vectors reveals the following active interactions and operational constraints: Board ↔ Block 1 : Friction, Board ↔ Block 2 : Friction, Floor ↔ Board : Normal, Force F → Board.", font_size=24).to_edge(DOWN)
        self.play(Write(narrative_text))
        self.wait(2)
        self.play(FadeOut(narrative_text))
        if "Block 1" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Block 1", font_size=18).move_to(obj.get_center())
            deployed_objects["Block 1"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Block 1"]))
        if "Block 2" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Block 2", font_size=18).move_to(obj.get_center())
            deployed_objects["Block 2"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Block 2"]))
        if "Board" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Board", font_size=18).move_to(obj.get_center())
            deployed_objects["Board"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Board"]))
        if "Floor" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Floor", font_size=18).move_to(obj.get_center())
            deployed_objects["Floor"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Floor"]))
        # Boundary marker for: Scene 2: Core Dynamics and Interactions
        self.wait(1)

        # Narrate: To solve the physics problem, we must resolve the mathematical boundaries for our primary objectives: Find F_min, Find F_max, Compute p + q.
        narrative_text = Text("To solve the physics problem, we must resolve the mathematical boundaries for our primary objectives: Find F_min, Find F_max, Compute p + q.", font_size=24).to_edge(DOWN)
        self.play(Write(narrative_text))
        self.wait(2)
        self.play(FadeOut(narrative_text))
        if "Block 1" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Block 1", font_size=18).move_to(obj.get_center())
            deployed_objects["Block 1"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Block 1"]))
        if "Block 2" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Block 2", font_size=18).move_to(obj.get_center())
            deployed_objects["Block 2"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Block 2"]))
        if "Board" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Board", font_size=18).move_to(obj.get_center())
            deployed_objects["Board"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Board"]))
        if "Floor" not in deployed_objects:
            obj = Square().set_color(BLUE)
            lbl = Text("Floor", font_size=18).move_to(obj.get_center())
            deployed_objects["Floor"] = VGroup(obj, lbl)
            self.play(Create(deployed_objects["Floor"]))
        # Boundary marker for: Scene 3: Target Boundary Calculation
        self.wait(1)
