# Advanced Settings

The Advanced tab contains detailed configuration options for the wheelbase.

These parameters control internal signal processing, compatibility behavior, and steering limit characteristics. In most cases, the default values are optimized and do not require adjustment.

!!! info
    Most users can operate the wheelbase normally using only the settings available in the **Basic tab**.

    The settings in the Advanced tab are primarily intended for **experienced users** who want to fine-tune force feedback behavior or adjust compatibility for specific sim racing games.

---

## Crash Effect Reduction

**Purpose**

Limits extremely strong force spikes generated during crashes or abrupt physics events.

**Explanation**

Some sim racing games may generate very large force spikes during collisions. These spikes can result in sudden high torque output from the wheelbase.

Crash Effect Reduction helps limit these spikes to improve user safety and reduce excessive steering shocks.

**Recommended Usage**

- Enable this option if the wheel produces very strong impacts during crashes.
- Disabling allows the wheelbase to reproduce the full force feedback signal from the game.

---

## DI Ratio

**Purpose**

Controls the contribution of the DirectInput force feedback signal when combining multiple force sources.

**Explanation**

In certain modes such as **TIC (Telemetry + DirectInput Combine)**, the wheelbase may receive force feedback from multiple sources.

- **Higher values** → prioritize the DirectInput force feedback signal from the game
- **Lower values** → increase the influence of internally generated telemetry forces

**Typical Range:** `30 – 70`

---

## Damper Filter

**Purpose**

Controls the response speed of the damping effect.

**Explanation**

- **Lower values** → faster, more responsive damping
- **Higher values** → smoother, more stable damping response

**Recommended Range:** `0 – 300`

---

## Inertia Filter

**Purpose**

Controls the response speed of the simulated rotational inertia.

**Explanation**

- **Lower values** → inertia reacts more quickly
- **Higher values** → smoother inertia, may slightly reduce steering responsiveness

**Recommended Range:** `0 – 300`

---

## Friction Filter

**Purpose**

Controls the response speed of the friction effect.

**Explanation**

- **Lower values** → faster response to steering input
- **Higher values** → smoother friction, reduces rapid changes in steering resistance

**Recommended Range:** `0 – 300`

---

## Bumpstop Range

**Purpose**

Defines the steering angle at which the maximum bumpstop force is reached.

**Explanation**

The bumpstop effect simulates the mechanical steering limit of a real vehicle.

When the steering angle reaches the configured **Steering Range**, the bumpstop force begins to increase. As the wheel continues to rotate beyond this point, the bumpstop force gradually increases until it reaches maximum strength at the Bumpstop Range.

This progressive force prevents the wheel from rotating beyond the configured steering limits while maintaining a natural steering feel.

**Recommended Setting**

The Bumpstop Range should typically be set slightly beyond the configured Steering Range (approximately **+5° to +15°**).

---

## Lock Strength

**Purpose**

Controls the maximum strength of the bumpstop force.

**Explanation**

Lock Strength defines the maximum force applied when the steering angle reaches the Bumpstop Range.

- **Higher values** → stronger steering stop, more noticeable limit
- **Lower values** → softer steering stop

**Recommended Range:** `5000 – 10000`

---

## FFB Mode

The FFB Mode setting defines how the wheelbase receives and processes force feedback signals from sim racing games.

=== "DirectInput"

    DirectInput is the standard force feedback interface used by most Windows sim racing games.

    The wheelbase receives force feedback signals directly from the game through the DirectInput API.

    **Recommended for general use** — best compatibility with most sim racing titles.

=== "Telemetry"

    The wheelbase generates force feedback using vehicle telemetry data received from supported games.

    Requires the **VNM Telemetry plugin** to be enabled and supported by the selected game.

    **Supported games:**

    - Assetto Corsa
    - Assetto Corsa Competizione
    - Assetto Corsa EVO
    - Assetto Corsa Rally (ACR)
    - iRacing
    - rFactor 2
    - Le Mans Ultimate
    - RaceRoom Racing Experience

=== "iRacing 360"

    Designed for full steering range support in iRacing with a **360 Hz force feedback update rate**.

    Provides faster and smoother force feedback response compared to standard DirectInput operation.

    !!! note
        This mode may not function in current versions of iRacing.

=== "TIC (Telemetry + DirectInput Combine)"

    Combines Telemetry-based force feedback with DirectInput force feedback signals.

    This hybrid approach can provide more detailed steering feedback while maintaining compatibility with the game's native force feedback system.

    Use **DI Ratio** to control the balance between telemetry and DirectInput forces.
