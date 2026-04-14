# Game Settings

## DirectInput Force Feedback Effects

The parameters in the Game Settings tab correspond to the different Force Feedback effect types defined by the **Microsoft DirectInput Force Feedback API**.

When a sim racing game sends Force Feedback signals to the wheelbase, those signals are represented using standardized effect types.

VNM SimCenter allows users to adjust the **gain (strength)** of each effect type — making it possible to fine-tune how strongly the wheelbase reproduces specific DirectInput force effects.

!!! tip "Recommended"
    In most cases, keep all values at **100%** to ensure accurate reproduction of the Force Feedback signal from the game.

---

## Effect Types

### Constant Force

Represents a steady force that does not change over time.

Commonly used to represent:

- Cornering forces from tire grip
- Self-aligning torque of the steering system
- Sustained steering resistance

**For most modern sim racing games, Constant Force is the primary component of the Force Feedback signal.**

### Ramp Force

Represents a force that gradually increases or decreases over time.

May be used to simulate smooth transitions in steering force (e.g., when load progressively increases entering a corner).

Less commonly used than constant forces in modern physics-based simulators.

### Condition Effects

Simulate mechanical characteristics of a steering system. Forces are generated dynamically based on wheel movement.

| Effect | Description |
|---|---|
| **Spring** | Applies a centering force pulling the wheel toward neutral position |
| **Damper** | Generates resistance proportional to steering speed |
| **Friction** | Applies constant resistance regardless of steering speed |
| **Inertia** | Simulates rotational mass of the steering system |

### Periodic Effects

Generate oscillating forces based on mathematical waveforms. Commonly used to simulate vibration.

| Waveform | Behavior |
|---|---|
| **Sine Wave** | Smooth, continuous oscillating force |
| **Triangle Wave** | Force changes linearly between two values |
| **Square Wave** | Abruptly alternates between two force levels |
| **Sawtooth Up** | Gradually increases then suddenly drops |
| **Sawtooth Down** | Gradually decreases then suddenly rises |

---

## Recommended Usage

In most cases, users should keep all DirectInput effect gain values at **100%**.

Adjust these values only if you want to modify how strongly the wheelbase responds to a specific type of DirectInput force effect.

---

## Games and Effects Reference

| Game | Game Effects | User Effects |
|---|---|---|
| AC / ACC / iRacing / F1 2020 | Constant gain, Damper gain | All |
| AMS2 | Constant gain | All |
| Dirt 4 / Rally 2.0 | Constant gain, Friction gain | All |
| Project Cars 2 | Constant gain, Sine gain | All |
| Raceroom | Sine gain | All |
| rFactor 2 | Sine gain, Damper gain | All |
| WRC Generation | Ramp gain, Square gain, Sine gain, Spring gain, Damper gain | All |
| WRC 10 | Constant gain, Sine gain, Spring gain, Damper gain | All |

!!! note
    This table will be updated as more games are tested.
