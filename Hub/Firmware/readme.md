#### v0.5.30  
9-6-2026

##### Features:
- An odd-shaped tank reads a sensor percentage that does not track the water actually in it. Add a per-tank Geometry Lookup option: the user calibrates by filling the tank in steps, recording how much water went in against what the sensor reports, and the hub then uses that table to compute the real percentage full and the water remaining in gallons or liters (per the hub-wide units setting). Table export/import as CSV.  Accessed via editing the tank device.
- New Slide card for slide-out rooms, available in the 4×1 and 2×2 sizes. It moves only while a direction button is held.
- The hub clock moved to the top of the System tab, and the Status page now shows whether the clock is set.
- RV-C Logging now lets you send a test frame while a capture is running, so the command and the device's reply are recorded together.

##### Fixed:
- A second tank monitor (or any other RV-C device) that reports the same tank number as an existing device was missing from the Add Devices scan. Each device is now listed separately, gets its own live readings, and a second one is given a distinguishing default name.
- RV-C Tools now shows a separate row for each device when two devices report the same instance number, labelled with the device's bus address.
- Inverter and charger AC status devices (1FFCA) now appear in device discovery without Expert mode.
- Inverter card bindings
- Shore power card bindings
- RV-C Tools and Devices now decode the full AC status pages (voltage, current, frequency, faults, peak values, input capacity) for inverter, charger, generator, ATS and generic AC sources.
- RV-C Tools now labels values a device reports as "not available" or "error" instead of showing a raw number.
- Inverter, charger and AC-source devices now show their AC readings, charger state details and configuration limits by default when added.
- Shore power input current limit can now be set from the Shore Power card, the Power Diagram, the Devices page and MQTT on RV-C inverter/chargers that support CHARGER_CONFIGURATION_COMMAND_2.
- The hub clock source (and timezone) could switch back to RV-C after a reboot if a Settings page was left open on another device. Clock settings now stay as saved.

#### v0.5.0
Initial release
