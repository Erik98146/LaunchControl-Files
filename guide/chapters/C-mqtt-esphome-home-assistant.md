# MQTT, ESPHome & Home Assistant

::: lead
For technical users: what the Hub publishes to MQTT, how to control it over MQTT, how to add your own MQTT and ESPHome devices, and how to connect Home Assistant. None of this is needed for normal use.
:::

## The broker

MQTT devices talk through a broker. Under **Settings → Integrations → MQTT**, turn on MQTT and choose one:

- **Connect to another broker —** an existing broker such as a Victron Cerbo GX or a Home Assistant server. Required for the Victron GX integration.
- **Use Hub's built-in broker —** the Hub is the broker. Other devices connect to the **Broker address** shown on the card.

| Built-in broker | |
| --- | --- |
| Port | 1883, plain MQTT (no TLS); for use on your own network only |
| Sign-in | None unless you set a username under **Sign-in for devices (optional)**; then every device must use that username and password |
| Capacity | Sized for 16 connected devices |
| Address to use | The Hub’s IP address. Shelly and ESPHome devices do not look up names such as `launchcontrol.local`, so reserve the Hub’s address in your router |

The Hub uses one broker at a time.

## What the Hub publishes

Under **Publish data to MQTT**, three switches choose what is sent. Each is independent and all are off until you turn them on.

- **RV-C data —** the fields marked **MQTT** on the Devices page.
- **Victron data —** readings from the Victron GX integration.
- **Bluetooth sensor data —** readings from the Bluetooth devices you added.

Every reading is published the same way:

| | |
| --- | --- |
| Topic | `<prefix>/<device>/<field>` |
| Payload | JSON with a value and a unit, for example `{"value":87,"unit":"%"}`. Text values are quoted: `{"value":"Bulk","unit":""}` |
| Names | The device and field names you see in LaunchControl, in lower case, with every run of other characters replaced by one underscore. “House Battery” becomes `house_battery` |
| Prefix | `launchcontrol_hub` unless you change **Topic prefix** under **Advanced settings** |
| Retained | Yes, so a client that connects later receives the latest value at once |
| Availability | `<prefix>/status` reads `online` while the Hub is connected and `offline` when it drops |

Examples:

    launchcontrol_hub/house_battery/state_of_charge   {"value":87,"unit":"%"}
    launchcontrol_hub/fridge_sensor/temperature       {"value":38.2,"unit":"°F"}
    launchcontrol_hub/status                          online

RV-C values are published when they change, and everything is sent again each time the Hub connects to the broker. Victron and Bluetooth values are sent within about two seconds of a change. Renaming a device or changing the prefix leaves the old retained topics on the broker; clear them with a tool such as MQTT Explorer.

## Control through MQTT

A published RV-C field that can be switched or set also listens on its own topic with `/set` added:

    launchcontrol_hub/water_pump/status/set     ON
    launchcontrol_hub/kitchen_light/brightness/set     40

- The device and field parts are the same names the field is published under; the two above are examples.
- The payload is `ON` or `OFF` (or `true` / `false`), or a number.
- Send it **not retained**. The Hub ignores retained commands, so a stored message can never switch something by itself after a restart.
- There is no reply topic. Watch the field’s own topic for the new value.
- Only RV-C fields accept `/set`. Use the control address for everything else; see **The control address** in [Technical Reference](#technical-reference).

::: warning "Anyone on the broker can send commands"
Every client connected to the broker can switch published fields. On the built-in broker, set a username and password if devices you do not control share your network.
:::

## Add your own MQTT device

1. **Open Devices → Add devices → Configure MQTT device.** The broker must be connected first.
2. **Enter a Device Name.**
3. **For each reading, press Add Field** and fill in:

| Field | What to enter |
| --- | --- |
| **Label** | The name of the reading, such as Temperature |
| **MQTT Topic** | The topic to read |
| **Unit override** | Optional. Leave blank to use the unit in the payload |
| **Command topic** | Optional. Where the Hub publishes when you switch or set the field. Blank keeps the field read-only |
| **Rounding** | Decimal places, 0 to 6 |

4. **Press Save,** then **Add to dashboard** in the device’s ⋮ menu, or choose the device as the data source of a Generic or Generic Switch card.

The Hub reads a payload that is a plain number or word, or JSON in the form `{"value":…,"unit":"…"}`. Commands are sent as `ON`, `OFF`, or a number, never retained. Up to 48 devices with six fields each can be added.

A suffix after `#` on a topic handles devices that publish differently:

| Suffix | On | What it does |
| --- | --- | --- |
| `#name` | MQTT Topic | Reads one value out of a JSON payload: `…/status/switch:0#output`. One level of nesting is allowed: `#temperature.tC`. True and false read as ON and OFF |
| `#lower` | Command topic | Sends `on` and `off` in lower case |
| `#rgbw:0` | Command topic ending in `/rpc` | Drives a Shelly RGBW light |
| `#valve` | Command topic ending in `/rpc` | Drives a Shelly-powered water valve: on opens it, off closes it |

## ESPHome

ESPHome devices are not found automatically yet. Add each one as an MQTT device.

Point the ESPHome device at your broker in its configuration:

    mqtt:
      broker: 192.168.8.8

By default ESPHome publishes each component under the device’s name, so the topics to enter in LaunchControl look like this for a device named `garage`:

| ESPHome component | MQTT Topic | Command topic |
| --- | --- | --- |
| A sensor named “Bay Temperature” | `garage/sensor/bay_temperature/state` | — |
| A switch named “Compressor” | `garage/switch/compressor/state` | `garage/switch/compressor/command` |

ESPHome switches publish and accept `ON` and `OFF`, which is what the Hub sends, so no suffix is needed. Use a tool such as MQTT Explorer to confirm the exact topics your device publishes.

## Leak sensors and water valves

A Shelly Flood sensor and a Shelly-powered water valve are added as MQTT devices by hand. Point each at the broker first, as in [Shelly Setup](#shelly-setup).

| Device | Field | Setting |
| --- | --- | --- |
| Shelly Flood | **MQTT Topic** | `<device id>/status/flood:0#alarm` — reads ON when wet and OFF when dry |
| Shelly-powered water valve | **Command topic** | `<device id>/rpc#valve` — on opens the valve, off closes it |

- On the Flood, turn on status notifications over MQTT in its own settings; they are off by default. The Flood runs on a battery and sleeps, so LaunchControl shows its state the next time it reports.
- `<device id>` is the Shelly’s default MQTT prefix, shown on its own MQTT settings page.
- The valve setting follows Shelly’s published interface for its smart water valve. Test that the valve closes and opens from its card before you rely on it, and use the automation in [Automations & Macros](#automations-macros) to close it when a sensor gets wet.

## Home Assistant

Home Assistant and LaunchControl can share a broker in either direction: point the Hub at Home Assistant’s broker with **Connect to another broker**, or point Home Assistant’s MQTT integration at the Hub’s built-in broker. The Hub does not announce its devices to Home Assistant automatically, so describe the ones you want in Home Assistant’s configuration.

A reading, from the Hub’s published data:

    mqtt:
      sensor:
        - name: "Coach battery"
          state_topic: "launchcontrol_hub/house_battery/state_of_charge"
          value_template: "{{ value_json.value }}"
          unit_of_measurement: "%"
          availability_topic: "launchcontrol_hub/status"

A control, through the Hub’s control address. This works for every named card, zone, scene, and macro, not only RV-C devices:

    rest_command:
      coach_water_pump_on:
        url: "http://192.168.8.8/api/control?device=Water%20Pump&action=on&key=YOUR_API_ACCESS_KEY"
      coach_bedroom_temp:
        url: "http://192.168.8.8/api/control?device=Bedroom&temp={{ temp }}&key=YOUR_API_ACCESS_KEY"

Replace the address with your Hub’s, the names with your own card names, and the key with the one under **Settings → Integrations → Shortcuts & API → API access key**. The **API & custom integrations** tab on that card builds these addresses for you. The key can be sent as an `Authorization: Bearer` header instead of in the address. Awnings, shades, slides, and levelers are refused.

Node-RED and other tools connect the same two ways: MQTT for readings, the control address for commands.
