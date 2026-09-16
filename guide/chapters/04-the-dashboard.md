# The Dashboard

::: lead
The dashboard is a set of live cards organized into panels. Cards update in real time; cards that support control respond when tapped.
:::

![A finished dashboard](images/ch04-a-finished-dashboard.png)

## Panels

- **Panel tabs —** switch between groups such as Main, Power, and Climate. Each panel has its own name, icon, and layout.
- **Graph History —** each panel sets the history window used by graphs on that panel.
- **Panel editing —** panels can be added, renamed, reordered, duplicated, and deleted from edit mode.

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
| Battery + Power | Battery state of charge, power flow, and history graph. |
| Solar | Solar charging power with history graph. |
| Shore Power | Shore connection status and power. |
| Inverter | Inverter state with on/off control. |
| Alternator | Engine/DC-DC charging status with graph. |
| Water Pump | Simple on/off control. |
| Awning / Shades | Extend/retract or up/down controls, with optional position. |
| Hydronic | Diesel/electric hydronic furnace control. |
| Power Diagram | Live power flow between shore, solar, alternator, battery, inverter, and loads. |
| Sleep Timer | Turns selected devices off at a set time each night. |
| Automation / Macro | Rules and one-tap action groups. |
| Clock / Generic | Clock and general-purpose sensor value cards. |
| Starlink / Travel Router | Internet equipment status and controls. |
| Slide | Room slide controls |

Victron-specific cards appear after the Victron integration is configured. Victron cards can also be auto-created and will include all bindings.

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
