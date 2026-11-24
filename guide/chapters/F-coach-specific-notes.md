# Coach-Specific Notes

::: lead
Every coach builder connects its equipment a little differently. This appendix explains behavior you may see on particular coaches, why it happens, and what to do about it.
:::

LaunchControl shows and controls what a coach puts on its control network. When something here does not match your coach, send a support file so it can be looked at; see [Troubleshooting](#troubleshooting).

## Controllers that change address after a power cycle

**What you see:** after the coach’s power was off, a scan lists a device you already added as **Moved here · updating**.

**Why:** some controllers come back with a different network address.

**What to do:** nothing. After about two minutes the Hub moves the saved device, its cards, lighting zones, shade groups, and automations to the new address.

- **Follow automatically:** lights and switched outputs, DC loads, window shades and awnings, door locks, roof fans, and thermostats.
- **Do not follow:** tanks, batteries, AC readings, and chargers. If one of these stops reading, add it again from a new scan and remove the old entry.

## Outputs that never report their state

**What you see:** a light or relay does not appear in the scan until it has been operated, and its row is marked **Control only**.

**Why:** some controllers accept commands for an output but never report whether it is on. LaunchControl then shows the last command it saw, from the dashboard or from the coach’s own switch panels.

**What to expect:** after a Hub restart the card shows no state until the output is next used. A switch that is wired directly to the equipment, or a key fob, cannot be seen.

## Door locks driven by two relays

**What you see:** the door lock does not appear as a lock in the scan. Two switched outputs do.

**Why:** the lock is two momentary relays, one to lock and one to unlock.

**What to do:** add both outputs in the same scan. LaunchControl pairs them into one **Door Lock** card and pulses the right relay for each action. If lock and unlock are reversed, use **Swap lock / unlock** in the card’s gear menu. Do not put a lock relay on a plain switch or light card, which would hold it energized.

## Awnings and shades that start and stop on a press

**What you see:** an awning or shade keeps moving after you let go, and the card shows nothing until it has moved once.

**Why:** window-shade controllers have no stop command and report nothing while at rest.

**What to do:** press a direction to start, and press the same direction again to stop. These cards are set to **Latching (one press)** automatically.

## Automatic water tank fill

**What you see:** the coach’s own panel turns the tank fill valve on after a short delay; a plain switch card may not start it.

**What to do:** operate the fill once from the coach’s own panel. The Hub learns how the coach switches that output and copies it. Then use a **Generic Switch** card on that output. This is a recent addition; tell support if the card does not start the fill on your coach.

## TV lifts

A TV lift has two outputs, up and down, and does not report its position. Choose **TV lift** in **What is it?** for its outputs; they are shown on a **TV Lift** card.

- The card shows a dash after a Hub restart until the lift is next used.
- On some coaches the lift runs only while it is powered. There a tap powers the chosen direction long enough to complete the travel; tap the other way to reverse.

## One wall button that switches several things

Some coaches have a button that switches several outputs together, such as a laundry button that runs a fan and opens a vent. A **Linked Switch** card does the same from the dashboard. If you mix the wall button and the card, the outputs can end up in different states; the card then reads **Mixed**, and a tap turns everything off.

## Switch-panel backlights

To add the backlights of the coach’s switch panels, press the on or dim side of the panel’s backlight button while the scan is open, then choose **Panel backlight** in **What is it?**. If you press only the off side, the scan offers a plain switched output instead.

## Winnebago coaches with WinnConnect

WinnConnect keeps its own record of some equipment and re-sends it, which limits what a second controller can do.

- **Lights.** The coach’s lighting zones appear in the scan as dimmers. Add them as dimmers; on, off, and brightness work, and color control is not available. After adding them, press each zone’s wall switch once so the Hub learns it. A zone whose switch has not been learned may need two presses at the wall after the Hub changed that light.
- **Inverter.** WinnConnect repeats its own inverter setting every few seconds while on shore power or generator, and so overrides a change made from LaunchControl. Use WinnConnect to switch the inverter.
- **Generator.** The generator is not on the RV-C network. The Hub senses when it is running, and the Shore Power card then reads **On generator**. The scan offers a **Generator (start / stop)** switch. A start or stop is refused while the running state is unknown and for 45 seconds after the previous request, and it is never available through LaunchControl Remote.
- **Tanks.** Fresh, gray, and black tank levels are not sent on the network the Hub reads on these coaches, so they cannot be shown from the coach itself. LPG is available. A Bluetooth tank monitor such as a Garnet SeeLevel is one way to add the others.
- **Roof fans and thermostats.** Their modules can change address after a power cycle. The Hub follows them automatically. If you see the same fan or thermostat twice from an earlier software version, delete the extra one.

## Wavetronix Fathom tank sensors

A Fathom may not show in a scan right away, because it answers only when asked; the Hub asks every 10 seconds. Set it up with one region and let the Hub correct an odd-shaped tank. See **Wavetronix Fathom sensors** in [Add or Change Equipment](#add-or-change-equipment).
