# The Dashboard

::: lead
The dashboard is a set of live cards organized into panels. Cards update in real time; cards that support control respond when tapped.
:::

![A finished dashboard](images/ch04-a-finished-dashboard.png)

## Panels

- **Panel tabs —** switch between groups such as Main, Power, and Climate. Each panel has its own name, icon (or two), and layout. As many tabs as fit are shown across the top; the rest are always one tap away under the **All panels** icon (the grid icon at the end of the tabs).
- **Sub-panels —** each panel can hold up to three sub-panels. Tap a tab's name to open it, or tap the small arrow beside it to choose one of its sub-panels. While a sub-panel is open, its tab reads "Panel › Sub-panel".
- **All panels —** shows every panel and sub-panel in your order, with the one showing marked. Tap any of them to go there. With more than eight panels a search box appears. **Manage panels** at the bottom opens the panel manager.
- **Graph History —** each panel sets the history window used by graphs on that panel.
- **Managing panels —** open **Manage panels** (from All panels, or from edit mode). Each panel has a **⋯** menu: **Edit** (name, icons and parent, with a preview), **Add sub-panel**, **Move…** (put it under another panel or back on top), **Duplicate**, **Move up / down** and **Delete**. Drag a panel by its handle to reorder it; the new order is saved when you press **Done**. Other changes save as soon as you make them, with **Undo** for a few seconds. Deleting a panel tells you first what happens to its cards and sub-panels.
- **Coming back —** reloading the page returns to the panel you were on; opening the dashboard fresh starts on the first panel.
- **Every screen follows —** a change to cards or panels made on one phone or laptop shows up on every other open dashboard, including TVs, within a couple of seconds. A dashboard that is in the middle of editing waits until the editor closes.

## Create and arrange the dashboard
Version 0.6 can automatically create dashboard cards when devices are added. This is the fastest way to build a new dashboard because the card type, device source, and normal bindings are configured together.

### Arrange the cards

1. **Open the Dashboard and enter panel edit mode**
2. **Drag cards into desired positions** The grab handle is in the top left of the card. Cards snap into the dashboard grid.
3. **Open card settings to edit, duplicate or remove.** 
5. **Exit edit mode.** The layout is stored on the Hub and is used by phones, browsers, and Touch 8 displays.

::: note "Responsive layout"
The dashboard grid adapts to screen size, so the same configuration can be used on desktop, phone, and Touch 8 displays.
:::

## Card gallery

| **Card** | **What it shows / does** |
| --- | --- |
| Thermostat | Room temperature, setpoint, mode, and fan. Available in several layouts. |
| Lighting | Inside/Outside master switches plus four scene buttons. |
| Light Dimmer | One light with on/off and brightness control. |
| Tank | Fresh, gray, or black tank level. |
| Battery + Power | Battery state of charge, power flow, and history graph. Three sizes: 8×4 Standard, 4×2 Compact (no graphs or detail row; time remaining shown as e.g. "4d 18h"), and 2×2 SoC + Power (just the two numbers). |
| Solar | Solar charging power with history graph. |
| Shore Power | Shore connection status and power. |
| Inverter | Inverter state with on/off control. |
| Alternator | Engine/DC-DC charging status with graph. |
| Water Pump | Simple on/off control. |
| Awning / Shades | Extend/retract or up/down controls, with optional position. |
| Hydronic | Diesel/electric hydronic furnace control. |
| Power Diagram | Live power flow between shore, solar, alternator, battery, inverter, and loads. |
| Sleep Timer | Turns selected devices off at a set time each night. |
| Automation / Macro | Shows one automation's status (tap to arm) or runs one macro. Set them up under Settings → Automations. |
| Clock / Generic | Clock and general-purpose sensor value cards. |
| Starlink / Travel Router | Internet equipment status and controls. |
| Weather | Current conditions and a five-day forecast; tap for the next hours. Four sizes, from a full 8×4 card to a one-row strip. Set up under Settings → Integrations → Weather. |
| Slide | Room slide controls |

Victron-specific cards appear after the Victron integration is configured. Victron cards can also be auto-created and will include all bindings.

The card editor shows a preview of the card at its real size, with sample values, for every layout you pick.

## Header icons

The icons at the top right of the dashboard, from left to right:

- **Warning triangle —** appears when something needs attention; a number on it is the count of unread alerts. Tap it to see them.
- **Connection dot —** green while the dashboard is receiving live data, amber while it reconnects.
- **Cloud —** LaunchControl Remote. On a dashboard opened through Remote it shows that page's own link: green while connected, amber while reconnecting. On the coach's own network it appears while someone is viewing the Hub through Remote.
- **Menu —** Settings, Devices and the other pages.

When a panel header shows the weather and space is tight, the place name is left out so the temperature, wind and rain always fit.

## Card Bindings
A binding connects an element on a dashboard card to information or controls provided by a device.

For example:
- A Tank card’s level display is bound to the level field of a tank device.
- A Light Dimmer card is bound to the status and brightness controls of a lighting device.
- A Thermostat card is bound to temperature, setpoint, operating mode, and fan fields.
- A Battery + Power card may combine information from a battery, shunt, and other power devices.

### Automatic bindings
When LaunchControl creates a card from the device-setup workflow, it automatically supplies the normal bindings for that card. Most users will not need to configure bindings manually.

Test each newly created card from the dashboard. If its values appear correctly and its controls operate the intended equipment, no additional binding configuration is necessary.

### Review or change bindings
To inspect a card's bindings:

1. Enter dashboard edit mode.
2. Open the card’s edit menu.
3. Review the device selected as the card’s data source.
4. Change advanced bindings only when the suggested source is incorrect or the card needs information from another device.

Cards that combine several functions may expose multiple named bindings. A Thermostat card, for example, can have separate bindings for room temperature, setpoint, operating mode, fan mode, and fan speed.

A missing or incorrect binding may cause a card to display a dash, omit a control, or operate the wrong device. Return to the card editor and confirm both the device source and the individual field assignments.

:::

![Card bindings](images/card-settings01.png)

The following table illustrates typical bindings for cards that refer to multiple source devices.

::: bindings
### Inverter
| Card element | DGN name | DGN | Field |
| Watts | Inverter Out Power | 1FFD5 | Real Power |
| Enable | Inverter | 1FFD4 | Enable |
| Charger | Charger Enable | 1FFC7 | Enable |

### Shore Power
| Card element | DGN name | DGN | Field |
| Watts | Charger Input Power | 1FFC8 | Real Power |
| Current Limit | Charger Current Limit | 1FFC9 | Capacity |
Note: Charger enable ties to 1FFC7.

### Battery + Power
| Card element | DGN name | DGN | Field |
| State of Charge | Battery | 1FFFC | State of Charge |
| Voltage | Battery | 1FFFD | Voltage |
| Temperature | Battery | 1FFFC | Temperature |
| Net Power | Battery | 1FFFD | Power |
| Remaining Time | Battery | 1FFFC | Time Remaining |
| Current | Battery | 1FFFD | Current |
| Consumption DC | — | — | — |
| Consumption AC | Inverter Out Power | 1FFD5 | Real Power |

### Climate
| Card element | DGN name | DGN | Field |
| Room Temp | Thermostat | 1FF9C | Temperature |
| Setpoint | Thermostat | 1FFE2 | Setpoint Cool/Heat |
| Mode | Thermostat | 1FFE2 | Mode |
| Fan Mode | Thermostat | 1FFE2 | Fan Mode |
| Fan Speed | Thermostat | 1FFE2 | Fan Speed |
:::

::: technical
Bindings may point to an RV-C instance/field, a Victron MQTT value, or a Bluetooth sensor reading. Structured cards use named function slots so the card knows which field represents mode, setpoint, fan, status, and similar functions. See section 14 for additional information.
:::

## Graphs

Solar, Battery + Power, Alternator, temperature, and similar cards can draw a small history graph. The Hub stores the history, so it remains available after the browser is closed and appears consistently on every display. The panel Graph History setting selects how much graph history should be shown.

## Look and feel

- **Themes —** choose the dashboard appearance in display settings; Touch 7 follows the dashboard theme.
- **Units —** the Hub-wide Imperial/Metric setting covers temperatures, pressures, and speeds. Individual Victron devices can override units when needed.
- **Background regions —** optional tinted regions can visually group related cards on a panel.
