# Card Reference

::: lead
Every dashboard card, in the order of the **Add a card…** list: its sizes, what it shows, what a tap and a press-and-hold do, and the settings worth knowing.
:::

## Common to every card

- **Add —** in panel edit mode, **Dashboard Cards → Add a card…**, or let LaunchControl create the card when you add equipment.
- **Gear menu —** in edit mode, each card’s gear offers **Edit**, **Move or copy…** when there is another panel, and **Delete**.
- **Edit —** every card has a **Card Name** and a **Layout**. Sizes are given in grid squares, width × height: an 8×1 card spans the dashboard and is one row tall.
- **Touch 8 —** every card appears on the Touch 8 unless its entry says otherwise.

## Power

### Battery + Power

- **Sizes:** 8×4 Standard, 4×2 Compact, 2×2 SoC + Power.
- **Shows:** state of charge, time remaining, net power, and **Charging battery** or **Using battery power**. The 8×4 size adds two graphs and a detail row.
- **Victron Battery Monitor** is the same card for a Victron battery monitor. It also names the source: charging from shore, solar, or engine.

### Inverter

- **Sizes:** 4×2 Standard, 2×2 Compact, 1×2 Narrow.
- **Shows:** the power supplied while inverting, **Charger Only** when only the charger is working, or **Off**.
- **Tap** switches the inverter. **Press and hold** starts an off-timer. The 4×2 size has a **Charger** menu to enable or disable charging.

### Shore Power

- **Size:** 8×1.
- **Shows:** power drawn, or **Connected**, **Disconnected**, or **On generator**; the current limit; a graph.
- **Tap** opens **Current limit** − and + in whole amps, and the charger’s Enabled / Disabled switch.

### Solar

- **Sizes:** 8×1, 4×1.
- **Shows:** solar power, yield, and a graph.
- **Tap** opens the seven-day yield chart when the charger is a Victron device.

### Alternator

- **Size:** 8×1.
- **Shows:** engine status, charging power, and a graph.
- **Tap** opens charging voltage, current, temperature, start battery, and engine detail.

### Battery Charger

- **Size:** 2×2, display only.
- **Shows:** the charge state — Off, Bulk, Absorption, Float, Storage, and so on — with optional volts and amps. A fault replaces the state, in red. The icon is green while charging, blue in float or storage, and gray when off.

### Power Diagram

- **Size:** 8×8.
- **Shows:** a picture of power flowing from shore, alternator, and solar to the battery, inverter, and loads. It reads your other power cards, so it has nothing to connect.
- **Controls:** shore limit − and +, the charger switch, tap the inverter to switch it, and tap the solar box for seven-day yield.

## Climate

### Climate

- **Sizes:** 4×2 Classic, 4×4 Dial, 2×2 Compact.
- **Shows:** the room temperature and **Heating to**, **Cooling to**, **Fan only**, or **System Off**.
- **Controls:** arrows change the temperature one degree at a time. The control panel has Mode (A/C, Heat, Off) and Fan (Hi, Lo, Auto), and separate heat and cool temperatures when the thermostat has both. Open it with the cog on Classic, a tap on the upper half of the Dial, or a tap on Compact.
- **Schedule:** tap the clock icon; see [Controls](#controls).
- **Setting — AC only:** removes the heat controls from this card, the Touch 8, and the Mini, for a zone with no furnace.

### Hydronic

- **Sizes:** 4×4 Full, 4×2 Compact.
- **Shows:** burner and electric element indicators with water, tank, and target temperatures.
- **Controls:** Off, Diesel, Electric, or Both, and the target temperature, on the Full size.
- **Touch 8:** status only.

### Roof Fan

- **Size:** 2×2.
- **Shows:** Off, Low, Medium, or High; dome open or closed; an optional temperature.
- **Tap** opens the speed and dome controls. Choosing a speed opens the dome; closing the dome stops the fan.
- **Touch 8:** readings only. Not available by voice or in automations yet.

## Water

### Tank

- **Tank types:** Water, Waste, Gray, Black, LPG, Fuel.
- **Sizes:** 4×4, 2×4, 2×2, 2×1, 1×2.
- **Shows:** level, and the amount remaining once a tank size or calibration is set.
- **Press and hold** switches the tank heater, when one is connected to the card.
- **Setting — Level alarm:** **Warning at** and **Alarm at**. Waste tanks start at 80 and 90 percent and alarm as they fill; water, LPG, and fuel start at 20 and 10 percent and alarm as they empty. The card outlines amber, then blinks red. No message is sent.

### Water Pump

- **Sizes:** 2×2, 1×2 Narrow. **Tap** switches the pump. **Press and hold** starts an off-timer.

### Tank Heat

- **Size:** 2×2. **Tap** switches the heater. A Tank card on the same heater shows the same state.

## Security

### Door Lock

- **Size:** 2×2.
- **Shows:** **Locked**, **Unlocked**, or a dash when the lock has not reported.
- **Tap** locks or unlocks. With the state unknown, the dashboard asks **Lock or unlock?**
- **Settings:** a color for locked and for unlocked — red, green, white, or gray. **Swap lock / unlock** in the gear menu corrects a lock that works backwards.

## Lights & switches

### Light Dimmer

- **Sizes:** 8×1, 4×1, 2×2 Compact.
- **Wide sizes:** tap the bulb for on or off, drag the slider or type a percentage, press and hold the bulb for 100%.
- **Compact:** tap for on or off; press and hold for the slider.

### Color Light

- **Size:** 2×2. The bulb takes the light’s color.
- **Tap** switches the light. **Press and hold** opens the color wheel, color chips, and the **Color**, **White**, and **Master** sliders. See [Shelly Setup](#shelly-setup).

### Lighting Scenes

Two zone masters and four scenes; everyday use is described in [Controls](#controls). Each Lighting Scenes card keeps its own lights, zones, and scenes, so you can add more than one: a full card on the main panel and a row of scene buttons by the bedroom.

| **Layout** | **What it shows** | **Use it for** |
| --- | --- | --- |
| 8×2 Standard | Both zone masters, the four scenes, and the automation badge | The main lighting card |
| 8×1 Scenes | The four scene buttons in one row | Scenes in a single-row slot, with no masters |
| 2×4 Scenes | The four scene buttons stacked | A narrow scene keypad |
| 4×2 Masters | On and Off for each zone, as four large buttons | Zone switching without scenes |

On the 8×2 Standard layout only, **Touch Panel Alternate** turns the card on a Touch 8 into four large buttons.

To set the card up:

1. **Add the card.** Open panel edit mode, then **Dashboard Cards → Add a card… → Lights & switches → Lighting Scenes**.
2. **Name it and pick a layout.** The name is shown on the card and is how Siri and Shortcuts find it.
3. **Set up the zones.** For Zone 1 and Zone 2, give the zone a name of up to 11 characters, such as Inside, then tick the lights it switches.
4. **Choose the scene lights.** Under **Scenes**, tick every light that any scene should control. The four scenes share this one list.
5. **Name the scene buttons.** Give each button a name, and optionally an icon or a second line of text.
6. **Save.** If the layout you picked does not fit where the card was, it moves to the first free space.

Things to know:

- **Memory** is a setting for each zone. With it on, **On** returns dimmable lights to the level they had before they were switched off. With it off, **On** always switches them on at full.
- Each zone and the scene list hold up to **32 lights**. Color lights and panel backlights can be scene lights.
- A layout with no master buttons folds the **Zones** section away, and the Masters layout folds **Scenes**. The settings are kept, and zones and scenes still work by voice, from macros, and from remotes even when the card does not show their buttons.
- A scene does not touch lights outside its list.

### Generic Switch, Fan, and Tank Heat

- **Size:** 2×2. **Tap** switches one output on or off.
- A Generic Switch connected to a Shelly relay also shows its wired switch as **Input on** or **Input off**.
- A Fan card connected to a vent with open and close motors opens a small Open / Close control instead.

### Linked Switch

- **Size:** 2×2. Switches up to three outputs, and optionally a vent motor, together.
- **Shows:** On, Off, or **Mixed** when the outputs disagree.
- **Tap** turns everything off when on or mixed, and on when off.

### Panel Backlight

- **Size:** 2×2. **Tap** steps through Off, On, and Dim. It can be added to a lighting scene.

### Sleep Timer

- **Size:** 4×2. Turns the inverter, water pump, and Starlink off at a set time each night; only the ones that have a card are offered.
- **Tap** the top of the card to arm or disarm it, and the time to change it.

## Motors

### Awning, Shades, and Slide

- **Sizes:** 4×1 or 2×2.
- **Tap** opens two direction buttons: extend and retract, up and down, or out and in.
- **Awning and Shades** come in two kinds: **Momentary (hold to move)** runs the motor while you hold the button; **Latching (one press)** starts on one press and stops on the next. Window-shade controllers are always latching. **Slides** are always hold to move.
- **Swap direction** in the gear menu corrects a card that runs backwards.
- **Also move these shades** on a Shades card adds up to 12 other shades that move with it.
- **Through Remote:** Awning and Slide cards read **Unavailable remotely**. Shades still work.

### TV Lift

- **Size:** 2×2. **Tap** sends the lift up or down. After a Hub restart the card shows a dash until the lift is next used, because the lift does not report its position.

## Internet

### Starlink

- **Sizes:** 2×2, 4×4 Detailed, 2×1 No Icon, 1×2 Narrow.
- **Tap** switches dish power when the card is connected to its power circuit. **Press and hold** starts an off-timer.
- **Setting — Connect to Starlink dish:** shows **Online**, **Searching…**, **Offline**, or **Dish off** with ping success. The Detailed size adds download, upload, latency, obstruction, uptime, and GPS.

### Travel Router

- **Sizes:** 2×2, 2×1 No Icon, 1×2 Narrow.
- **Shows:** Wi-Fi, Ethernet, or No internet; or a setup message such as Check password.
- **Tap** opens the connection, Wi-Fi networks to join, the speed test, and network quality.
- **Setting — Network quality alarm:** the card blinks red when quality stays below your number for more than 10 seconds.

## Utility

### Clock

- **Sizes:** 2×1, 4×1, 2×2, 4×2. Time and date. **Press and hold** opens the clock settings.

### Generic - Single and Generic - Dual

- **Sizes:** Single 2×1 or 8×1 Graph; Dual 4×1.
- **Shows:** any one or two readings, captioned with the card’s name. Name a Dual card “Fresh / Gray” to label each value.
- **Setting — Value alarm:** above or below, with **Warning at** and **Alarm at** in the units the card shows. The card outlines amber, then blinks red. No message is sent.

### Automation and Macro

- **Sizes:** 2×2, 1×2 Narrow.
- **Automation** shows Normal, Triggered, Disabled, or Latched. **Tap** turns the rule on or off, or resets it when latched.
- **Macro** shows when it last ran. **Tap** runs it.

### Web Link

- **Sizes:** 2×1, 4×1. **Tap** opens the web address you set under **Address**; **Open in new page** keeps the dashboard open behind it.
- **Touch 8:** not shown.

### Weather

- **Sizes:** 8×4 Full, 4×2 Compact, 4×1 Bar, 8×1 Strip.
- **Tap** opens the next 24 hours; the smaller sizes can switch to the five-day forecast.
- **Setting — No background:** on the Strip size, for a clean header row.
- The location is set once for the whole Hub under Settings → Integrations → Weather.

## Victron

These appear in the list once Victron equipment is configured.

| Card | Sizes | What it does |
| --- | --- | --- |
| Victron MultiPlus | 4×2, 2×2, 1×2 | Shows On, Charger Only, Inverter Only, or Off with power. Tap switches between On and Charger Only; press and hold starts an off-timer. |
| Victron Battery Monitor | 8×4, 4×2, 2×2 | The Battery + Power card for a Victron battery monitor. |
| Victron Shore Power | 8×1 | The Shore Power card for a Victron system. |
| Victron MPPT | 8×1, 4×1 | Solar power and yield. Tap for the last seven days. |
| Victron GPS | 2×1 | Speed and altitude. |
| Victron Temp - Single / Dual | 2×1, 8×1 Graph / 4×1 | One or two temperature sensors, captioned with the sensor names. |
