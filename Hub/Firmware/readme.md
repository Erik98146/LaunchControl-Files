### v0.8.xx
10-9-2026

##### Features:
- Remote UI has improved login, layouts, and a new brief RV status page
- New Color Light card for Shelly Plus RGBW PM light controllers: pick a color on a wheel, set RGB and white brightness separately or together with a master dimmer, and save it all in Lighting scenes.
- Shade card pop-outs close after touching a button.
- New experimental AI integration: Control your RV using conversational voice control. Query status and control devices. Spot trends. It can answer questions from the Users Guide. Requires LaunchControl Remote.

#### Fixes:
- Door locks driven by two relays now show the right state when operated from other controllers, such as a Spyder panel
- Lights and DC loads that never report their own status (e.g. some ValidMfg coaches) can now be added as “control only” devices; their state follows the commands LaunchControl sees. Relay door locks on such coaches use the coach’s own pulse.
- Installing an update no longer appears frozen at 100% while the Hub restarts; the page shows the restart and a timer. 
- A web interface update that stalls or uses the wrong file no longer leaves the Hub without its pages; the current interface stays in place.
- Shore power no longer shows "Disconnected" before any reading arrives.
- Lighting card's scene icons no longer overlap in its settings.
- Added compatibility with older client devices

---------------------------------------

### v0.8.15
10-6-2026

##### Features:
- Remote Access now uses an on/off switch, matching the other integrations.
- Shelly Gen2/Gen3/Gen4 relays connected to the Hub's MQTT broker are found automatically under Devices → Add devices, and get a dashboard switch card in one tap. The input can also drive automations.
- Phones can have their own dashboard card order by re-arranging on the phone.
- New Fan card: on/off for exhaust fans, and Open / Close for vent motors, with a fan icon on the dashboard and the Touch display.
- Devices page: Bulk create cards for the devices you select.
- Panel Edit now opens scrolled to your cards.

#### Fixed:
- Door Lock cards with a single relay now hold the lock, matching the coach's panel.
- A lock whose position is unknown now asks whether to lock or unlock rather than toggle.
- On phones, dashboard cards now keep their order instead of rearranging to fill gaps.
- Restarts caused by updates or errors no longer count toward the power-cycle PIN reset.
- After a firmware update, the Hub now reports exactly what happened: updated, still waiting to restart, or rolled back.
- Improvements to debug file and crash dump file for debugging.
- Added missing weather card previews

-------------------------------

### v0.8.2
10-5-2026

##### Features:
- LaunchControl Remote: Remote access over the cloud. Open your coach's dashboard from anywhere, in any browser, with no app, no router settings and no port forwarding. Turn it on under Settings → Integrations → Remote Access and the same dashboard is available remotely. Every new hub includes 90 days free; after that $6.99 a month or $69 a year, managed from the portal. Includes sharing with other people. LaunchControl support can be let in for 24 hours with a PIN you hold, and for safety awnings and slides cannot be moved remotely.
- LaunchControl Remote Status page: battery, tank and temperature readings, recent alerts, and a 30-day map of where your coach has been, if Cerbo-GPS equipped.
- New dashboard layout and management: Dashboards can now have sub-panels. Easier dashboard navigation: addition of an All panels drawer, separate sub-panel chevrons, and a simpler panel manager with editing, moving, reordering and undo. Up to 5 sub-panels per main panel.
- Improved weather cards: 
    - Added an 8x1 weather card with optional no background.
    - Improved weather forecasting by switching to the European ECMWF model.
    - Improved weather card layouts and fonts.
    - Smaller variants have a 5-day forecast pop-out option.
    - A weather panel is now available in the header.
- Shortcuts & API improvements: With guided voice and one-tap shortcut setup, a searchable device picker, safe command testing, and controls for the API access key.
- Settings menus have been revised with a less busy interface.

#### Fixes:
- Added missing weather card previews
- Cards now keep working when a coach gives its RV-C controllers new bus addresses after a power cycle: lights, switches, loads, shades and door locks show their real state again, and "did not take effect" no longer appears for commands that worked.

------------------------------------------

### v0.7.40
10-1-2026

##### Features:
- 3rd party interface API: Voice Control. Shortcuts, & Siri -  say "Hey Siri, Coach" then "kitchen lights on", "bedroom to 72", or build one-tap shortcuts from Settings → Integrations. Works on Apple Watch and over a VPN; no extra hardware.  Any device that can open a web address can interface.
- Added a MQTT broker to the hub.  This allows integration to a multitude of devices without requiring an external broker.
- Battery + Power cards now come in a 4×2 compact size and a 2×2 small.
- A Shades card can now move several shades at once. Edit the card and tick the other shades it should move; one press moves them all, from the dashboard or a Touch display.
- Syncronize changes across devices: Editing a dashboard will now auto-update all other connected displays.
- Alerts you have already read now show in gray. A History button keeps every alert since start-up even after Delete all.
- Macro improvements: Macros can now set a thermostat to Fan Only and include timed waits between steps.

------------------------------------------

### v0.7.26
9-29-2026

##### Features:
- Revise state tracking to free significant RAM for furture development.
- The hub now supports TLS for secure connections to the internet. This will allow for future addition of new features.
- New Weather card: Three sizes with a 5‑day forecast and an hourly view on tap. Location comes from the coach GPS automatically, or set a place once in Settings.
- New Linked Switch card: one tap controls several outputs together, such as a laundry mode that powers the washer/dryer, turns off air conditioners and opens the dryer vent. The card turns red if the outputs ever get out of step.
- Door locks wired as two relays now set up as a single Door Lock card when you add them and create cards.  Setup with improved discovery and automatic card creation.
- Generic value cards now show your card name as the label. On a two-value card, name it like "Fresh / Gray" to label each value.
- Generic value cards can now warn and alarm when a value goes above or below levels you set, on the dashboard and the Touch display.
- The old "Generic" card is now named "Generic Switch" to make clear it's an on/off control.
- The Travel Router card can now alert you to poor conditions: turn on the network quality alarm, set a threshold (85 by default), and the card blinks red on the dashboard and Touch display when quality stays below it.  Requires a GL.iNet Beryl AX (MT3000) Travel router with 4.11 (beta) firmware and network quality enabled.

--------------------------------------

### v0.6.92
9-27-2026

##### Features:
- GL.iNet travel router speed test and network quality: View network quality, run a speed test from the router card on the dashboard or Touch 8, schedule automatic tests, and see recent results (requires GL.iNet firmware 4.11 beta or newer).
- Added support for Mopeka Pro series propane tank, water and fuel sensors as Bluetooth devices and shown on a Tank card with level alarms.
- Climate cards have a new "AC only" setting that hides heat and fuel controls, for thermostat zones which only run the air conditioner.

#### Fixed:
- Thermostat cards for the same climate zone now share one schedule, so the zone shows the same schedule and clock status on every dashboard.
- On the Touch 8, press and hold a lighting scene to save the current light levels to it, just like on the dashboard. Scenes saved anywhere now update immediately on every open dashboard.

-------------------------------------------------

### v0.6.78
9-24-2026

##### Features:
- New Door Lock card — tap to lock or unlock, with a green padlock when locked. Works with RV-C door locks and with coaches whose lock is a pair of relay outputs. Lock and unlock colors may be set in card settings.
- Bulk device add now has an Identify button on each row — tap it to switch a light or DC load on and see which one it is, tap again to switch it back.
- The hub checks once a day for a newer firmware release and adds an alert when one is available.
- Automations and alerts have been re-worked into a dedicated settings section:
    - Automations are now managed entirely under Settings → Automations, with their own sensor picker. A dashboard card is optional and simply points at an automation for status. 
    - Macros are now managed entirely under Settings → Automations. 
    - Push Alerts and SMS Alerts settings moved under Settings → Automations.
    - Alerts can show on-screen behind the top-right icon and under Settings → Status → Alerts.  Press to view details and clear. Critical system alerts are in red an cannot be cleared.

-----------------------------------------------

### v0.6.57
9-22-2026

##### Features:
- Awning, shade and slide cards have a "Swap direction" option, for when the coach's motor is wired so that Extend and Retract come out the wrong way round. Found on the card gear menu and may be applied individually or globally.

------------------------------------------------

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
