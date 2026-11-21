<!-- part: Using LaunchControl -->
# Controls

::: lead
Use dashboard cards for everyday lighting, climate, tanks, and timers. The sections below explain gestures and what each control does.
:::

A tap, a press-and-hold, and a timer action can do different things on different card types. Follow the instructions for the card you are using.

## Lighting Scenes

The Lighting Scenes card controls groups of lights from one place:

- **Two zone masters —** an On and an Off button for each of two groups of lights, such as inside and outside.
- **Four scenes —** one-tap lighting presets such as Evening or Movie. Each scene remembers the level of every light in it.

Each Lighting Scenes card keeps its own lights, zones and scenes, so you can add more than one: for example a full card on the main panel and a row of scene buttons by the bedroom.

![The 8×2 Standard layout](images/ch05-lighting-master-controls.png "The 8×2 Standard layout: a zone master either side of the four scenes")

### Layouts

The card comes in four layouts. Pick one when you add the card, and change it at any time from the card's **Edit** dialog.

| **Layout** | **What it shows** | **Use it for** |
| --- | --- | --- |
| 8×2 Standard | Both zone masters, the four scenes, and the automation badge | The main lighting card |
| 8×1 Scenes | The four scene buttons in one row | Scenes in a single-row slot, with no masters |
| 2×4 Scenes | The four scene buttons stacked | A narrow scene keypad |
| 4×2 Masters | On and Off for each zone, as four large buttons | Zone switching without scenes |

The Touch 8 shows the same layouts. On the 8×2 Standard layout only, **Touch Panel Alternate** turns the card on a Touch display into four large buttons.

### Set up the card

1. **Add the card.** Open panel edit mode, then **Dashboard Cards → Add a card… → Lights & switches → Lighting Scenes**. The Lighting Scenes dialog opens.
2. **Name it and pick a layout.** Tap a layout button to see a preview of the card at its real size. The name is shown on the card and is how Siri and Shortcuts find it.
3. **Set up the zones.** For Zone 1 and Zone 2, give the zone a name (up to 11 characters, for example Inside), then tick the lights it switches.
4. **Choose the scene lights.** Under **Scenes**, tick every light that any scene should control. The four scenes share this one list.
5. **Name the scene buttons.** Give each button a name, and optionally an icon or a second line of text.
6. **Save.** The card appears on the panel. If the layout you picked does not fit where the card was, it moves to the first free space.

To change any of this later, open the card's gear menu and choose **Edit**. Name, layout, zones and scenes are all in that one dialog.

::: note "Sections that fold away"
A layout with no master buttons folds the **Zones** section, and the Masters layout folds **Scenes**. Open a folded section to change it: its settings are kept, and zones and scenes still work by voice, from macros and from remotes even when the card does not show their buttons.
:::

Each zone and the scene list hold up to **32 lights**. The dialog warns when a list is full.

### Use the zone masters

- **On —** tap to switch the zone's lights on.
- **Off —** tap to switch them all off.
- **Full brightness —** press and hold **On** to bring every light in the zone to 100%.
- **Memory —** a setting for each zone in the Edit dialog. With Memory on, **On** returns dimmable lights to the level they had before they were switched off. With it off, **On** always switches them on at full.

The buttons also show what the lights are doing: **On** is lit while any light in the zone is on, and **Off** is lit when all of them are off. This stays correct when lights are switched at a wall switch.

### Save and use scenes

1. **Set the lights.** Use the dimmer cards, the masters or the wall switches to get the lights the way you want them.
2. **Press and hold a scene button.** On the dashboard, confirm **Save**. On a Touch display the scene is saved as soon as you hold the button.
3. **Tap the button to recall it.** Every light in the scene list goes to the level it had when you saved, including lights that were off.

How scenes behave:

- **Changing a scene —** set the lights again and press and hold the same button.
- **A scene that has never been saved —** tapping it does nothing.
- **Which scene is active —** the last scene recalled stays highlighted until you recall another or press a master.
- **Lights outside the scene list —** a scene does not touch them.

Scenes can also be run without the card: from a macro or automation (see [Automations & Macros](#automations-macros)), from a Shelly BLU button remote, and by name with Siri and Shortcuts.

### Lighting automation

On the 8×2 Standard layout, the clock badge in the top right corner opens Lighting Automation. It can switch lights on and off by time of day, or use a solar panel as a light sensor to switch them at dusk and dawn. The badge is yellow while automation is on.

## Lighting Dimmers

The Light Dimmer card provides controls for an individual light. Dimmers for small cards can be accessed by pressing and holding the card. Lights remember their last value when turned back on. This setting can be changed in the device setup for each light.

## Climate

The Thermostat card is available as a wide card, a large dial, or a compact tile. The dial shows current room temperature and the selected setpoint. Tap the compact tile to open the full mode, fan, and setpoint controls. 

### Schedules

A thermostat can follow four daily periods: Awake, Away, Return, and Sleep. Each period has its own time, mode, and setpoint. The clock control switches between following the schedule and manual hold.

::: note "Clock required"
Schedules only run when the Hub has valid time. The Hub keeps its clock automatically — internet time when it has it, otherwise the coach network, a GPS or the browser that is open. If a schedule will not enable, see Settings → System → Date & time.
:::

## Tanks

Fluid tanks with heaters that have been bound to a card may be toggled by pressing and holding the card. 

For an irregularly shaped tank, **Geometry Lookup** maps sensor readings to measured contents. Calibrate once under **Devices → edit the tank**; see **Tank Geometry Calibration (Optional)** in [Add or Change Equipment](#add-or-change-equipment). The Hub then shows corrected percentage and estimated volume in your selected units.

## Awnings & Shades

Awning and Shades cards have two direction buttons. Depending on the device, a button is either hold-to-move (the motor runs while you hold it) or press-to-command (window-shade controllers start on a press and stop on the next press). The card settings say which.

**Move several shades at once —** when you add or edit a Shades card yourself, the card editor lists every other shade on the Hub under **Also move these shades**. Tick the ones that should follow. One press then moves the card's own shade and every ticked shade, from the dashboard or a Touch display. Cards created automatically are one shade each; edit a card to group them.

## Graphs

Solar, Shore Power, Alternator, Generator, Battery and Net Power cards have graphs that can be configured for time and scale markers from the panel edit mode.

## Device Off-timers

Many on/off cards can start a device with a countdown timer to automatically turn off the device when the time expires. Press and hold a device to start the timer. Tap the device again to cancel the timer (device remains on).

## Sleep Timer

The Sleep Timer card turns selected devices off at the same time every night. Choose the devices, set the time, and arm the timer.

::: note "Timer uses"
Device timers are useful for short duration use, when you don’t want to forget to turn off a water pump or inverter, for example. The sleep timer is especially useful when you are off-grid and don’t want to accidentally run power hungry devices all night.
:::
