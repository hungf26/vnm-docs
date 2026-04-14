# Firmware Update

## Purpose

Firmware Update allows you to update the internal software of the wheelbase to:

- Improve performance and stability
- Fix bugs
- Add new features

Update the firmware whenever a new version is released by the manufacturer.

## Important Notes

!!! danger "Do Not Power Off During Update"
    Powering off during a firmware update may corrupt the firmware.

!!! warning "Version Requirement"
    Update via UI is only available for **firmware version 1.0.2.6 or later**.

    For lower versions:

    - Hold the reset button for a few seconds
    - Use VNM Flash tool to perform the upgrade

After updating:

- You may need to **Reconnect** the device
- Verify your profiles and settings

If the update fails:

- Try again
- Or use Reconnect (`Ctrl + F6`)

---

## How to Access Firmware Update

**Step 1** — Open VNM SimCenter

**Step 2** — From the top menu, select:
```
Device → Update Firmware
```

The Firmware Update panel will be displayed and detect `[DFU] VNM Direct Driver`.

---

## Firmware Update Panel

### Components

| Component | Description |
|---|---|
| **Device (DFU Mode)** | Select the device in DFU mode (e.g., `[DFU] VNM Direct Driver`) |
| **Firmware Version** | Select the version to install (latest is pre-selected) |
| **Refresh** | Rescan connected DFU devices |
| **File Selection (…)** | Manually select a firmware file (e.g., for beta firmware) |
| **Full Erase** | Erase all existing firmware before flashing (use when firmware is corrupted or update fails multiple times) |
| **Flash** | Start the firmware update process |
| **Abort** | Cancel the update process |
| **Log Window** | Displays update progress and any errors |

---

## Firmware Update Procedure (DFU Mode)

**Step 1** — Put the wheelbase into DFU mode (automatic via UI or using reset button if required)

**Step 2** — Open the Firmware Update window

**Step 3** — Select:
- DFU device
- Firmware version

**Step 4 (Optional)** — Enable **Full Erase** if needed

**Step 5** — Click **Flash**

**Step 6** — Wait until the process completes (check Log window for status)

---

## Troubleshooting

| Problem | Solution |
|---|---|
| Device not detected after update | Reconnect the device; Unplug and reconnect USB; Restart SimCenter |
| Update stuck or not completing | Wait a few more minutes; if still stuck → restart software and try again |
| No DFU device appears | Press **Refresh**; Reconnect USB; Enter DFU mode again |

!!! warning
    Do not disconnect during flashing. After a successful update, the device will reboot and reconnect may be required.
