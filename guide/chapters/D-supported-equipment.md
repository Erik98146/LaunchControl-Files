# Supported Equipment

::: lead
What LaunchControl can monitor and control, grouped by how the equipment connects to the Hub. “Monitor” means its readings appear on the dashboard; “Control” means the dashboard can operate it.
:::

If your equipment is not listed, it may still work: any RV-C reading can be shown on a Generic card, and any device that publishes to MQTT can be added by hand. See [Add or Change Equipment](#add-or-change-equipment).

## Built into the coach (RV-C)

Found by **Devices → Add devices**. What a particular coach offers depends on what its manufacturer connected to the RV-C network; see [Coach-Specific Notes](#coach-specific-notes).

| Category | Device or equipment | Monitor | Control | What you get |
| --- | --- | --- | --- | --- |
| Lighting | Lights, on/off and dimmable | Yes | Yes | On, off, brightness, zone masters and four-scene presets |
| Lighting | ITC VersiControl RGB(W) lighting zones | Yes | Yes | On, off and brightness per zone |
| Lighting | Switch panel backlights | Yes | Yes | Off, dim or on; can be part of a lighting scene |
| Climate | Thermostats, air conditioners, heat pumps and furnaces | Yes | Yes | Room temperature, mode, fan, setpoint and a four-period daily schedule |
| Climate | Roof fans and powered vents | Yes | Yes | On, off, speed and dome open or closed |
| Climate | Hydronic heating: Elwell Timberline 1.5 | Yes | Yes | Water and tank temperature, burner and electric element status, mode and setpoint |
| Power | House batteries and battery monitors | Yes | — | Voltage, current, state of charge, temperature and time remaining |
| Power | Chassis battery | Yes | — | Voltage |
| Power | Inverter/chargers | Yes | Yes | Inverter on or off, charger state, AC power, off-timer |
| Power | Shore power | Yes | Yes | Connected state and power draw; shore current limit |
| Power | Battery chargers and DC-DC chargers | Yes | — | Charge state, voltage and current |
| Power | Solar charge controllers | Yes | — | Solar power, daily and lifetime yield, history graph |
| Power | Alternator regulators (Wakespeed WS500 class) | Yes | — | Charging voltage, current and temperature, engine running |
| Power | Generators | Yes | — | Running status and starting battery voltage |
| Water | Fresh, gray, black, LP and fuel tanks | Yes | — | Level, volume remaining, warning and alarm thresholds |
| Water | Wavetronix Fathom tank sensors | Yes | — | Level, with tank-shape correction in the Hub |
| Water | Water pumps | Yes | Yes | On, off and off-timer |
| Water | Tank heaters | Yes | Yes | On and off |
| Coach | Awnings | — | Yes | Extend and retract (not available through Remote) |
| Coach | Window shades | — | Yes | Up and down; one card can move a group of shades |
| Coach | Slide-outs | — | Yes | Extend and retract (not available through Remote) |
| Coach | Door locks | Yes | Yes | Lock, unlock and lock state |
| Coach | TV lifts | Yes | Yes | Up and down |
| Coach | Fans, vents and other switched 12 V loads | Yes | Yes | On and off; several outputs can be linked to one switch |
| Coach | Any other RV-C reading | Yes | — | Shown on a generic value card, with optional alarms |

## Victron, through a GX device

Needs a Cerbo GX or other GX device on the same network as the Hub.

| Category | Device or equipment | Monitor | Control | What you get |
| --- | --- | --- | --- | --- |
| Power | Victron MultiPlus inverter/chargers | Yes | Yes | Mode (on, charger only, inverter only, off), input current limit, AC power |
| Power | Victron battery monitors (SmartShunt, BMV) | Yes | — | Voltage, current, state of charge and time remaining |
| Power | Victron solar chargers (MPPT) | Yes | — | Solar power, yield and a seven-day history |
| Sensors | Victron temperature sensors | Yes | — | Temperature |
| Location | Victron GPS | Yes | — | Position, speed and elevation; follows the coach for weather and Remote |

## Bluetooth

Needs Bluetooth turned on under Settings → Integrations. No GX device or gateway is required.

| Category | Device or equipment | Monitor | Control | What you get |
| --- | --- | --- | --- | --- |
| Power | Victron SmartSolar chargers (MPPT) | Yes | — | Solar power, battery voltage, charge state and yield today |
| Power | Victron SmartShunt and BMV battery monitors | Yes | — | Voltage, current, state of charge and time remaining |
| Power | Victron AC chargers | Yes | — | Charge state, voltage and current |
| Power | Victron Orion Smart and Orion XS DC-DC chargers | Yes | — | Charge state, input and output voltage, off reason |
| Power | Victron SmartLithium batteries | Yes | — | Battery voltage, lowest and highest cell, balancer state |
| Power | Victron Smart BatteryProtect | Yes | — | Output state, voltages, alarm and warning |
| Power | Thornwave PowerMon battery monitors | Yes | — | Voltage, current, power, state of charge and temperature |
| Water | Garnet SeeLevel tank monitors (709-BT, 709-BTP3, 709-BTP7, 708-RBT Soul) | Yes | — | Every tank the monitor reports, each as its own tank card |
| Water | Mopeka tank sensors, including the Lippert LP sensor | Yes | — | Propane or tank level, temperature and sensor battery |
| Sensors | RuuviTag temperature sensors | Yes | — | Temperature, humidity, pressure and battery |
| Sensors | Ruuvi Air air-quality monitor | Yes | — | CO2, PM2.5, VOC, NOx, temperature and humidity |
| Sensors | SwitchBot meters (Meter, Meter Plus, Outdoor Meter, Meter Pro, Meter Pro CO2) | Yes | — | Temperature, humidity, battery, and CO2 on the Pro CO2 |
| Sensors | Shelly BLU H&T, Door/Window and Motion sensors | Yes | — | Temperature, humidity, open or closed, motion, light level |
| Sensors | Other BTHome v2 sensors, such as Xiaomi with pvvx firmware and leak sensors | Yes | — | Temperature, humidity, water leak, battery |
| Remotes | Shelly BLU button remotes | Yes | — | Each press runs a macro, recalls a scene or switches a device |

## Shelly and other Wi-Fi equipment

Connects over Wi-Fi through an MQTT broker; see [Shelly Setup](#shelly-setup) and [MQTT, ESPHome & Home Assistant](#mqtt-esphome-home-assistant).

| Category | Device or equipment | Monitor | Control | What you get |
| --- | --- | --- | --- | --- |
| Switching | Shelly relays, Gen2, Gen3 and Gen4 (Plus, Pro and Gen4 lines) | Yes | Yes | On, off and wired switch state; found automatically |
| Switching | Shelly inputs, such as the Plus i4 | Yes | — | On or off state; button presses can run macros |
| Lighting | Shelly Plus RGBW PM color lights | Yes | Yes | On, off, color wheel, color and white brightness, scenes |
| Water | Shelly Flood leak sensors | Yes | — | Leak alarm, usable as an automation trigger |
| Water | Shelly-powered smart water valves | — | Yes | Open and close, for an automatic leak shut-off |
| Other | ESPHome and other MQTT devices | Yes | Yes | Any published value as a reading; command topics for control |

## Internet and network

Reached over the network the Hub is joined to.

| Category | Device or equipment | Monitor | Control | What you get |
| --- | --- | --- | --- | --- |
| Internet | Starlink | Yes | Yes | Online state and ping success; dish power when wired to a switched circuit |
| Internet | GL.iNet travel routers (Beryl and Slate families) | Yes | Yes | Uplink, signal, internet check, speed test; join campground Wi-Fi |

## Lippert OneControl coaches

Coaches that use Lippert OneControl in place of RV-C are supported through the Hub’s **Connection protocol** setting; see the note in [Add or Change Equipment](#add-or-change-equipment).
