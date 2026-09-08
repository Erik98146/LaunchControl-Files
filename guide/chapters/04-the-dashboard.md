# The Dashboard

::: lead
The dashboard is a set of live cards organized into panels. Cards update in real time; cards that support control respond when tapped.
:::

![A finished dashboard](images/ch04-a-finished-dashboard.png)

## Panels

- **Panel tabs —** switch between groups such as Main, Power, and Climate. Each panel has its own name, icon, and layout.
- **Graph History —** each panel sets the history window used by graphs on that panel.
- **Panel editing —** panels can be added, renamed, reordered, duplicated, and deleted from edit mode.

## Edit mode: arrange the dashboard

1. **Enter edit mode from the dashboard.**
2. **Use + Add Card.** Choose a card type, name, size/layout, and device bindings.
3. **Drag cards to reposition them.** Cards snap into the dashboard grid.
4. **Use a card’s gear menu.** Edit, resize, or remove the card.
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

## Binding cards to devices

A card shows live data because it is bound to a device field. When you add or edit a card, LaunchControl provides a list of functions associated with the card. Select the device field that should be mapped (bound) to that function. Floor-plan cards normally arrive already bound.

::: note "What “binding” means"
A binding is simply the link between a dashboard card and the underlying device data. For example, a Tank card might be bound to the level field of the Fresh Water Tank device; a Light Dimmer card is bound to the control and status fields for one light.
:::

![Card bindings](images/ch04-card-bindings.png)

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
