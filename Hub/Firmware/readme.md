### v0.6.54
9-22-2026

##### Features:
- The "Create cards for new devices" pop-out can now make a new dashboard by going to the bottom of the dashboard list.

##### Fixed:
- Fixed the Down button on awning and shade cards sending the same command as Up in some cicumstances, so the shade only ever moved one way.

---------------------------------

### v0.6.52
9-21-2026

##### Features:
- The Lighting card's two master groups are now called Zone 1 and Zone 2, and each can be renamed from the card's settings
- When scanning for devices you can now tick several in the All Detected Devices list and add them in one go, reviewing and renaming them in a table first
- A card can now be moved or copied to another dashboard from its gear menu, and a copy brings its settings with it
- The Lighting card's device lists now separate likely lights from other switched outputs, with the rest available at the bottom
- A tank in alarm now flashes its liquid red as well as its outline, on waste, grey and black tanks.

##### Fixed:
- Increased max tracked states
- In panel edit mode the Lighting card's automation clock no longer sits underneath the card-options gear
- Cards on a phone now keep the same shape they have on a laptop — tank bars, thermostats and square tiles are no longer stretched sideways.
- Lighting scene 2nd row labels clarified in edit mode
- Shades and awnings have been revised as devices and cards

----------------------------------

### v0.6.35
9-17-2026

##### Features:
- Router card now reports Tailscale status if enabled
- A new Weblink card can be setup to open any URL.  Useful for shortcuts to weather sites, cameras or other devices
- Tank cards can now warn and alarm at levels you choose — the card outlines amber at the warning and flashes red at the alarm.
- Notifications feature: Phone and SMS notifications can be tied to automations to alert on tank levels, temperatures, or any other device status. Enable in Settings>Integrations and setup by adding and editing an Automations card.
- Clock cards now come in 2×1, 4×1, 2×2 and 4×2, with the time centred and sized to fill the card in the same typeface as the dashboard header clock. There is no card outline or background. Press and hold a clock card to jump straight to the clock settings.
- TV/Kiosk mode: Show any dashboard panel full-screen on a TV, HDMI stick or wall tablet. Setup from from Settings → Displays, then tune the size, scaling, and safe-area sliders from your phone while watching the screen. 
- The Devices list marks anything that does not have a card yet with a yellow "Not on Dashboard".
- When creating cards for new devices, you can now choose which panel each switched output's card goes on.

##### Fixed:
- Climate card schedule no longer requires a long press
- After adding devices, "Create cards" now builds cards only for the devices you just added, instead of every device on the hub. The dashboard editor's button still covers everything.

---------------------------------

### v0.6.1
9-16-2026

##### Features:
- New Devices & Dashboard flow.  This version revises how devices are added to the system and how dashboard cards are automatically created.
- Add support file download to Settings>Status

---------------------------------

9-14-2026

##### Fixed:
- Return to Scan ID list after adding device

---------------------------------

### v0.5.108
9-13-2026

##### Fixed:
- Improved online update tool
- Fixed mobile rendering on Devices page
- Improved handling of margininal Wi-Fi
- Improved dashboard initial loading time
- After adding an RV-C device, return to the scan

---------------------------------

### v0.5.78
9-12-2026

##### Features:
- Added Victron SmartShunt Support
- Added device identification assistant
- Redesigned Devices pages

##### Fixed:
- System restore was missing some items

----------------------------------

### v0.5.37  
9-7-2026

##### Features:
- Starlink integration is enabled by default when adding a Starlink card. This will display a color-coded ping success rate on the card when turned on.
- Release notes are always available when viewing System>Online Updates
- Added Touch 8 display compatability

----------------------------------

### v0.5.30  
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

-------------------------

### v0.5.0
Initial release
