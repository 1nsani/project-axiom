# Axiom Programs

## What is an AxiomProgram?

An **AxiomProgram** (`AxiomProgram` dataclass) is a compiled, sequential array of atomic rendering and vector execution directives. It represents the final low-level intermediate representation (IR) of the engine pipeline before physical animation rendering.

## What is an Instruction?

An **Instruction** (`Instruction` dataclass) is a discrete, strongly-typed machine operation within an `AxiomProgram`. Each instruction maps an active engine command directly to a localized target and execution state matrix:

* **Action:** The core operational command (e.g., `Create`, `Move`, `Transform`, `Narrate`).
* **Target:** The exact entity ID or subsystem being manipulated.
* **Parameters:** A configuration dictionary specifying velocities, scales, text values, or layout bounds.

## Why Axiom Language Exists Between Storyboard and Manim

The Axiom Intermediate Language isolates abstract structural concepts from the programmatic overhead of direct visual framework implementations.

```
Storyboard ──[Compiler]──> AxiomProgram ──[Interpreter]──> Manim Render Engine

```

This structural separation fulfills three architectural mandates:

1. **Framework De-coupling:** It protects the core business logic from framework-specific APIs (like Manim's complex update loops, scene graphing, and vector transformations).
2. **Deterministic Execution:** Translating abstract, human-readable scene narration and actions into a rigid list of state instructions removes ambiguities prior to generation.
3. **Multi-Target Compilation:** The `AxiomProgram` acts as an engine-agnostic assembly block. The same program can be interpreted to drive Manim for high-fidelity videos, three.js for real-time web instances, or matplotlib for quick visual validations.
