Project Axiom

«A compiler for transforming physics problems into educational animations.»

Axiom is an open-source research project that aims to automate the creation of high-quality educational physics animations.

Instead of directly asking an AI model to generate animation code, Axiom decomposes the problem into multiple deterministic stages. Each stage has a single responsibility, making the system modular, testable, and extensible.

---

Vision

The long-term vision of Axiom is to build a complete compiler that converts a written physics problem into a polished educational animation comparable to professional explanatory videos.

Rather than treating animation generation as a single AI task, Axiom treats it as a software engineering problem.

---

Core Philosophy

Every stage must work manually before it becomes automatic.

Human understanding comes first.

AI is introduced only after the pipeline has been validated.

This philosophy ensures that every component can be tested independently and replaced without affecting the rest of the system.

---

High-Level Pipeline

Physics Problem (Markdown)
            │
            ▼
Markdown Parser
            │
            ▼
Concept Extraction
            │
            ▼
Concept Model
            │
            ▼
Storyboard Builder
            │
            ▼
Storyboard
            │
            ▼
Axiom Compiler
            │
            ▼
Axiom Language (Intermediate Representation)
            │
            ▼
Manim Generator
            │
            ▼
Generated Python Code
            │
            ▼
Render Engine
            │
            ▼
Educational Animation (.mp4)

---

Pipeline Stages

1. Markdown Parser

Reads a structured Markdown document and converts it into structured data.

Output:

- Objects
- Quantities
- Interactions
- Constraints
- Goal

---

2. Concept Extraction

Transforms structured problem information into a Concept object.

The Concept contains only semantic information.

No animation logic is introduced at this stage.

---

3. Storyboard Builder

Converts a Concept into a sequence of educational scenes.

Each scene answers one educational question.

A storyboard describes:

- learning goal
- objects
- actions
- narration

It does not describe camera movement or animation implementation.

---

4. Axiom Compiler

Transforms the Storyboard into an Intermediate Representation called Axiom Language.

This is the compiler stage.

Every scene becomes a sequence of primitive instructions.

Example:

Create(Block)

Label(Block)

Highlight(Contact)

Narrate(...)

EndScene

---

5. Manim Generator

Converts the Intermediate Representation into executable Manim Community Python code.

This backend knows nothing about physics.

It only translates instructions.

---

6. Render Engine

Executes Manim and produces the final animation.

Output:

video.mp4

---

Why an Intermediate Representation?

Axiom intentionally separates educational logic from rendering logic.

Storyboard
        │
        ▼
Axiom Language
        │
        ▼
Manim

Because of this architecture, the rendering backend can later be replaced.

Possible future backends include:

- Blender
- Three.js
- SVG
- WebGL

without changing the Storyboard.

---

Current Project Status

Current MVP includes:

- Markdown-based problem representation
- Concept data model
- Storyboard model
- Axiom Language design
- Compiler architecture
- Manim backend architecture
- Unit testing infrastructure

The project is currently focused on building a deterministic end-to-end pipeline before introducing AI.

---

Future Roadmap

- LLM-assisted Concept Extraction
- Automatic Storyboard Generation
- Intelligent Axiom Compiler
- Multi-backend Rendering
- Voice Narration
- Camera Planning
- Visual Style System
- Interactive Web Interface

---

Design Principles

- One responsibility per component
- Deterministic before intelligent
- Data model before business logic
- Unit tests before automation
- Intermediate Representation before rendering
- AI replaces validated modules, never undefined processes

---

Technology Stack

- Python
- Manim Community
- Markdown
- JSON
- Pytest
- Google Colab
- GitHub
- Obsidian

---

Project Structure

axiom/
│
├── src/
├── tests/
├── examples/
├── docs/
├── vault/
└── README.md

---

License

This project is under active development.
The architecture may evolve as the compiler matures.
