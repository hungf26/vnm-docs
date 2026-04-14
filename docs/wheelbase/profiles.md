# Wheelbase Profiles

Wheelbase Profiles allow users to save, load, and manage different wheelbase configurations.

A profile stores **all current wheelbase settings**, including parameters from the Basic, Advanced, and Game Settings tabs. This allows users to quickly switch between different configurations depending on the sim racing game, vehicle type, or personal driving preference.

## Use Cases

Using profiles makes it easy to maintain separate setups for different racing scenarios:

- Different sim racing games
- Different car types (Formula, GT, Rally, etc.)
- Different steering wheels
- Different Force Feedback preferences

Profiles can also be shared between users or backed up for later use.

---

## Profile Management

The profile management controls are located in the **Profile section** of the wheelbase configuration page.

Available actions:

- Create new profiles
- Load existing profiles
- Save changes to the current profile
- Import profiles from external files
- Share profiles with other users

---

## Creating a New Profile

**Step 1** — Click **Add Profile**.

**Step 2** — Enter a name for the new profile.

**Step 3** — Adjust the wheelbase settings as desired.

**Step 4** — Click **Save** to store the profile.

The new profile will now appear in the profile list.

---

## Loading a Profile

**Step 1** — Open the **Profile list**.

**Step 2** — Select the desired profile.

**Step 3** — Click **Apply**.

The wheelbase will immediately load the settings stored in that profile.

---

## Saving Profile Changes

If you modify any wheelbase settings, the profile can be updated to store the new configuration.

**Step 1** — Adjust the desired parameters.

**Step 2** — Click **Save** to store the changes in the current profile.

If the changes should not be saved, click **Revert** to restore the previous settings.

---

## Importing Profiles

Profiles can be imported from external files.

**Step 1** — Click **Import**.

**Step 2** — Select the profile file.

**Step 3** — The profile will be added to the profile list.

This feature allows users to load profiles shared by other users or provided by VNM.

---

## Sharing Profiles

Profiles can be exported and shared with other users. Sharing is useful for:

- Exchanging Force Feedback setups with other sim racers
- Distributing recommended settings for specific games
- Backing up personal configurations

!!! tip "Recommended Practice"
    Create separate profiles for each sim racing game.

    Different games use different Force Feedback models, and separate profiles help maintain consistent steering behavior across titles.

---

## Automatically Change Profile

**Purpose**

Automatically switches the wheelbase profile based on the car you are using in-game.
This eliminates the need for manual profile changes and ensures optimal Force Feedback for each vehicle.

**Requirements**

- VNM Telemetry Plugin version >= 0.0.107
- Applies to wheelbase profiles only
- Not yet supported for Telemetry profiles

**How It Works**

- The plugin automatically detects the game + car when selected in-game
- Each car can be assigned to a dedicated profile
- When you return to that car → the profile is automatically loaded

!!! note
    If no profile is assigned to a car → the system will use the **current active profile**.

**Setup (for new car)**

**Step 1** — Open VNM SimCenter

**Step 2** — Navigate to **Automatically Change Profile**

**Step 3** — Enable the **Automatically Change Profile** feature

**Step 4** — Click **Refresh** to update the car list from the plugin

**Step 5** — Select game and car from the drop lists

**Step 6** — Configure Force Feedback settings as desired (Overall gain, user effects, etc.)

**Step 7** — Click **Save**

**What Happens Next**

- When you select the same car again → the saved profile will be automatically loaded
- When switching to another car → the corresponding profile will be loaded (if available)

**Troubleshooting**

| Issue | Solution |
|---|---|
| Car does not appear | Click **Refresh** |
| Profile does not load automatically | Ensure plugin is running; check plugin version (>= 0.0.107); make sure the feature is enabled |

**Best Practices**

- Create separate profiles for different car types (GT3, Formula, Drift)
- Avoid using a single profile for all cars
- Always click **Save** after making changes
- Use clear profile names (e.g., `ACC_GT3_Ferrari_296`)

---

## Hotkey Settings

**Purpose**

Quickly adjust wheelbase settings and switch profiles without switching to Windows.

**Access**

**Step 1** — Open VNM SimCenter

**Step 2** — Go to: **Settings → Wheelbase**

### Hotkey Step

Defines how much the value changes with each key press.

*Recommended:* `1 – 5` (depending on desired precision)

### Hotkey Sensitivity

Controls how fast values change when holding a key.

Higher value → slower change when holding the key.

### Notification Position

Defines where notifications appear on screen (Center, or other positions depending on version).

### Device Selection

Select which device receives the hotkey input. Example: `VNM GT Steering Wheel V1`

### Hotkey Mapping

#### Overall Gain (+/-)

Increase / decrease overall FFB strength.

Use case:
- Reduce force if it feels too heavy
- Increase force if feedback is too weak

#### DI Ratio (+/-)

Adjust DirectInput scaling ratio in TIC mode.

#### Overall Filter (+/-)

Adjust FFB smoothness.

- Higher → smoother, less noise
- Lower → more detail, may feel rough

#### Centerize

Return the wheel to center position (0°).

#### Profile Switching

Quickly switch between profiles. Example: `Ctrl + Num 0`

!!! tip
    Click **Save** in the bottom-right corner to apply all changes.

---

## General Settings

Controls how the wheelbase is displayed and how certain UI-related behaviors function. These settings do not directly affect Force Feedback.

| Setting | Purpose | Recommended |
|---|---|---|
| **Wheel max angle** | Maximum steering angle displayed in software | `1080°` for GT/road cars |
| **Wheel angle step** | How much steering angle changes per hotkey press | `90°` or `180°` |
| **Show current torque in %** | Displays FFB output as percentage instead of Nm | Enable for easy monitoring |
| **Enable circle animation** | Visual indicator for base temperature, torque, error status | User preference |
