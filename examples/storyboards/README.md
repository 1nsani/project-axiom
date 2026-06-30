# Storyboards

## What is a Storyboard?

A **Storyboard** is a structural blueprint (`Storyboard` dataclass) that models a complete instructional sequence. It converts extracted physical parameters into a sequential, deterministic pipeline designed for automated asset compilation.

## What is a Scene?

A **Scene** (`Scene` dataclass) represents a atomic state or visual frame within the sequence. It encapsulates a localized state by declaring:

* **Context:** `title` and structural `goal`.
* **State Matrix:** The active physics `objects` present.
* **Dynamics:** Discrete engine `actions` and mathematical operations.
* **Narration:** The contextual script justifying the frame's transformations.

## Why Storyboards Exist Before Animation

Storyboards act as an abstraction layer separating core physics extraction from downstream rendering logic.

```
Concept ──> Storyboard ──> Animation Render Engine

```

Developing a declarative storyboard *before* driving geometry engines ensures:

1. **State Validation:** Physical boundaries and kinematic constraints are calculated and verified prior to running costly vector/matrix transforms.
2. **Engine Agnostic Execution:** The sequence remains a pure data layer, allowing interchangeable render engines to interpret the actions array identically.
3. **Deterministic Layouts:** Explicit object-action mapping prevents interpolation errors during state transitions.
