# Troubleshooting

## Wheelbase Disconnection

If your wheelbase occasionally disconnects from the PC during use, this is usually related to **USB signal instability**, **electrical noise (EMI)**, or **system power quality**.

---

## Quick Check

Before following all steps, identify your situation:

| Symptom | Likely Cause |
|---|---|
| Disconnect only under strong force (kerbs, impacts) | Electrical noise (EMI) |
| Random disconnect (even when idle) | USB or power issue |
| Disconnect even in DFU mode | USB cable or hardware issue |
| Works normally on another PC | PC USB environment issue |

---

## Testing — Case 1: Disconnect Under Force (Driving)

**Test:** Reduce torque to **50%** and check if the issue disappears.

- **If yes** → indicates a load-dependent issue

  Gradually increase torque (+10% each step) and observe:
  - Force spikes causing temporary power-off, then recovery → **power supply protection or instability**
  - Disconnect without full power loss → **EMI or grounding issue**

- **If no** → may indicate general USB stability or hardware issue

---

## Testing — Case 2: Random Disconnect

=== "Test 1: EMC Stop"

    - Disable motor output
    - Check if disconnect still occurs

    **If stable** → strongly suggests EMI or load-related interference

=== "Test 2: DFU Mode"

    - Enter DFU mode
    - Check if disconnect occurs

    **If yes** → USB cable / hardware issue

=== "Test 3: Different PC"

    Test on another PC or laptop.

    **If works normally** → likely PC USB environment issue

---

## Step-by-Step Solutions

### Step 1: Use a Direct Motherboard USB Connection

Connect the wheelbase directly to a **rear USB port on the motherboard**.

Avoid:

- USB hubs
- Extension cables
- Monitor or keyboard USB ports

### Step 2: Keep USB Cable Away from Power Cables

Ensure the USB cable is not routed alongside:

- Wheelbase power adapter cable
- Other high-power cables

Keep at least **20–30 cm** distance if possible.

### Step 3: Ground the Rig to the PC Case

If using a metal rig, connect it to the PC case using a grounding wire:

```
Rig / Wheelbase  →  grounding wire  →  PC Case
```

This helps reduce electrical noise and improves stability.

### Step 4: Ensure Proper Grounding of the PC

For best results, the PC should be connected to a properly grounded power outlet (3-pin with earth).

In advanced setups, a dedicated grounding connection can be used to connect the rig or PC case to a verified earth ground.

!!! warning
    Only perform this if you are familiar with proper electrical grounding and safety.

### Step 5: Try a Different USB Port

- Use another rear USB port
- Avoid front panel ports
- Try moving the wheelbase to a different USB port group (different controller if possible)

### Step 6: Try a Shorter USB Cable

Use a cable **shorter than 1.5 m**. Shorter cables are less sensitive to interference.

### Step 7: Add Ferrite Clamps

Attach ferrite clamps to the USB cable, preferably near the device side (wheelbase).

If multiple USB devices are connected (pedals, shifters, button boxes, etc.), consider adding ferrite clamps to those cables as well.

Electrical noise can travel through USB connections between devices and the PC. Using ferrite clamps on multiple devices can help reduce overall system noise.

### Step 8: Check Power Stability

- Avoid overloaded power strips
- Avoid sharing power with high-power devices
- If using a surge protector, try connecting the PC directly to a wall outlet as a test

### Step 9: Use a USB Isolator

In high electrical noise environments, a **USB isolator with isolated power** may help improve stability. This is not required in most setups.

---

## If the Issue Still Occurs

Please provide the following information when contacting VNM support:

**A. Basic Information**

- Are you using a USB hub?
- Are you using the original USB cable?
- Is the rig grounded to the PC case?
- Your PC specifications (CPU and motherboard)
- List of connected sim racing devices (wheelbase, pedals, shifter, motion system, etc.)

**B. When Does the Issue Occur?**

- Under force (during driving)
- Randomly (including idle or light use)
- Immediately after plugging in

**C. Additional Details**

- Does the device fully power off, or only disconnect from USB?
- Any other relevant observations
