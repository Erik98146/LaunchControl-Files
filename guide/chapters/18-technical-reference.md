<!-- part: Advanced -->
# Technical Reference

::: lead
Everything in this chapter is optional. Normal installation and use do not require this information.
:::

## Architecture in one paragraph

The Hub connects to the coach RV-C bus (CAN at the physical layer), decodes bus traffic into a live device model, and serves the dashboard locally over HTTP. Dashboard state changes are pushed over WebSockets. Touch 8 subscribes to the dashboard card model so it can mirror the configured panels and cards, while Mini asks the Hub for semantic roles such as “the battery.” Commands flow back through the Hub, which is the only LaunchControl device that transmits on RV-C.

## Hardware

| **Component** | **Details** |
| --- | --- |
| Hub | ESP32-S3 industrial control board with isolated CAN (RV-C) and RS-485 interfaces; simultaneous Wi-Fi access-point + station operation; dual firmware slots. |
| Touch 8 | ESP32-P4 dual-core RISC-V, 32 MB RAM; 8-inch 1024×600 IPS touch panel; Wi-Fi 6 through onboard co-processor; dual firmware slots. |
| Mini | ESP32-S3; 1.75-inch round 466×466 AMOLED touch display; dual firmware slots. |

## Versions

Each component reports its own vMAJOR.MINOR.BUILD version in Settings → Status and on the Update page. Hub, Touch 8, and Mini can version independently, while releases are verified as a compatible set.

## Network details

- **Friendly names —** launchcontrol.local (mDNS/Bonjour), launchcontrol-xxxx.local (per-device name), the DHCP hostname launchcontrol-xxxx, and http://launchcontrol on Windows.
- **Hub hotspot —** the Hub is 192.168.4.1 on its own hotspot. Touch 8 and Mini displays live on this private network.
- **Network separation —** the Hub does not route traffic between its hotspot and the RV/home router network.
- **Captive setup portal —** the automatic setup portal exists only on an unconfigured Hub. After commissioning, the hotspot behaves as a normal local network.

## Glossary

| **Term** | **Meaning** |
| --- | --- |
| RV-C | Industry-standard digital control network used in RVs; devices report state and accept commands on a shared two-wire bus. |
| DGN / instance | How RV-C identifies a message type and distinguishes multiple devices of the same kind. |
| GX device | Victron system monitor such as Cerbo GX; provides access to Victron installation data. |
| MQTT | Lightweight publish/subscribe protocol used by the Hub for Victron and custom integrations. |
| mDNS / Bonjour | Local-network name discovery that allows launchcontrol.local to work without a DNS server. |
| Binding | The link between a dashboard card and the device field(s) it displays or controls. |
| Panel | One dashboard tab: a named grid of cards. |
| Floor plan | A complete pre-built coach configuration. Loading a floor plan restores that configuration to the Hub. |

## Understanding Devices, Cards, and Dashboards

Four things work together to turn information from your RV’s equipment into an organized control panel.

**Device** — a piece of equipment or a function in the RV, such as a light, water pump, thermostat, tank sensor, inverter, or battery monitor. Devices are discovered through RV-C or added through integrations such as Victron, Bluetooth, or MQTT.

**Card** — the control or information display for a device. A Light Dimmer card controls a light, a Tank card shows a tank level, a Thermostat card displays and controls the climate system.

**Dashboard** — cards organized into one or more panels. Cards can be rearranged to match how you use your RV.

**Binding** — the link between a card and the device information it displays or controls. LaunchControl creates the normal bindings automatically when it creates a card; this chapter lists them.

## Expert mode

Expert mode is one switch for the whole product — at the top of the Devices page, in the scan, and at the bottom of the LaunchControl Remote card in Settings — remembered in the browser you set it in. Off, LaunchControl shows equipment by name; on, it also shows the protocol underneath: DGNs, instance numbers, source addresses, every field a device defines, raw bindings in the card editor, the relay override and the custom Shortcuts address. Nothing is removed by turning it off; it is only hidden.

## Card bindings

A binding connects an element on a dashboard card to information or controls provided by a device. For example a Tank card’s level display is bound to the level field of a tank device; a Light Dimmer card to the status and brightness of a lighting device; a Thermostat card to temperature, setpoint, mode and fan fields; a Battery + Power card may combine information from a battery, a shunt and other power devices.

To inspect a card’s bindings: enter dashboard edit mode, open the card’s edit menu, and review the device selected as the card’s data source. **Advanced** shows every slot. Change a binding only when the suggested source is incorrect or the card needs information from another device. Structured cards use named function slots so the card knows which field represents mode, setpoint, fan, status, and similar functions.

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

Bindings may point to an RV-C instance/field, a Victron MQTT value, a Bluetooth sensor reading, a Shelly/MQTT device field or a OneControl device.

## Understanding RV-C Devices, DGNs, and Instances

RV-C is the communication network used by many RV systems to share status information and commands between devices. The specifications can be found on the [RVIA web site](https://www.rvia.org/system/files/media/file/RV-C%20Specification%20Full%20Layer%202-20-26_Final_v2.pdf). Rather than each device having its own dedicated connection to LaunchControl, devices communicate over a shared two-wire RV-C bus.

At a basic level, LaunchControl identifies RV-C information using two important pieces: a **DGN** and an **instance**.

**DGN** — Data Group Number

A DGN (Data Group Number) identifies the type of RV-C message being sent. You can think of it as describing the function or category of information.

Examples include data groups for:

- Lighting dimmers
- Tank levels
- Thermostats
- Water pumps
- Battery information
- Generator status

A DGN does not necessarily represent one physical device. The same DGN can be used by many devices of the same type.

The **instance** identifies which device or function the message belongs to when several use the same DGN.

For example, an RV may have several dimmable lights:

| DGN | Instance | Example Device |
| --- | --- | --- |
| Lighting Dimmer | 22 | Kitchen Overhead |
| Lighting Dimmer | 24 | Bedroom Light |
| Lighting Dimmer | 32 | Main Ceiling |
| Lighting Dimmer | 35 | Bench Light |

All four lights use the same lighting-dimmer message type, but each has a different instance number so the system can tell them apart.

Suppose the Main Ceiling light is represented by the lighting-dimmer DGN with Instance 32.

When that light reports its current brightness, LaunchControl sees a lighting status message for Instance 32 and updates the corresponding device.

When you move the brightness slider on a LaunchControl dashboard, the Hub sends the appropriate lighting command for Instance 32. Other dimmers using the same DGN ignore the command because it is not addressed to their instance.

This is why a single RV-C device type may appear several times when LaunchControl scans the bus.

**Status and Command DGNs**

Some RV-C functions use separate DGNs for status and commands. A lighting dimmer, for example, may report its current state using a lighting status DGN while accepting on/off or brightness changes through a related command DGN.

LaunchControl handles these relationships for you. In normal use, you simply add the discovered device, give it a meaningful name such as Main Ceiling, and LaunchControl creates and binds its dashboard card.

**Device Fields**

Within a device, LaunchControl exposes individual pieces of information as fields. Such as a dimming level of a light, or the mode of the thermostat.

Dashboard cards are then bound to these fields. For example, a Climate card might bind its mode control to the mode field of a thermostat device.

![LaunchControl interface screenshot](images/ch14-launchcontrol-interface-screenshot.png "")

A device’s **Advanced** settings expose its individual fields and allow changing the field name and unit rounding as well as the calculated offset and multiplier (which are set by default to the RV-C specification); Expert mode lists every field the device defines.

You normally do not need to know the underlying DGN or instance numbers. LaunchControl discovers and manages them automatically, but understanding the relationship can be helpful when identifying devices or troubleshooting an RV-C installation.
