# Connecting Additional Equipment

::: lead
Connect only the equipment you actually have. Each section is independent; you can add these features at any time.
:::

## Choose the equipment you are adding

Use only the sections that match your installation. Built-in RV equipment may be your only source; integrations are optional. [Supported Equipment](#supported-equipment) lists everything LaunchControl works with.

| Equipment | Where to begin |
| --- | --- |
| Built-in lights, pumps, tanks, or climate | [Add or Change Equipment](#add-or-change-equipment) |
| Victron equipment with a GX device | **Settings → Integrations → Victron GX** |
| Shelly relays, inputs, or RGBW lights | [Shelly Setup](#shelly-setup); choose the broker before configuring devices |
| Bluetooth sensors, tank monitors, or a button remote | **Settings → Integrations → Bluetooth** |
| GL.iNet router or Weather | The matching card under **Settings → Integrations** |
| Starlink | A Starlink card on the dashboard; see the Starlink section below |
| Other MQTT equipment, including ESPHome | **Devices → Add devices → Configure MQTT device** |

## Victron equipment

If your coach has a Victron GX device such as a Cerbo GX, LaunchControl can read and control supported Victron equipment including MultiPlus inverter/chargers, battery monitors, solar chargers, GPS, and temperature sensors. Use the GX integration when you have a supported GX device. Other MQTT equipment can share its broker.

1. **Enable MQTT on the Cerbo GX.** On the GX device: Settings → Services → **MQTT on LAN (plaintext)** on.  The hub will need to see the Cerbo over the network. See Wi-Fi setup guide at [launchcontrol.tech FAQ](https://launchcontrol.tech/pages/support-faq)
2. **Find the Cerbo.** On the Hub, open **Settings → Integrations → Victron GX** and press **Set up**. Press **Find Cerbo GX**; the Hub looks for the GX device on your network and offers it. Press **Use this Cerbo**. LaunchControl connects MQTT to it, finds its Portal ID, and turns Victron on, in one go.
3. **Add the equipment.** Press **Add Victron devices** on the Victron GX card, or open Devices and run a Victron scan. Add the discovered equipment; LaunchControl creates matching dashboard cards.

You’re done when the Victron readings appear on your dashboard.

![Devices added after a Victron scan](images/ch03-devices-added-after-a-victron-scan.png)

::: technical
If the Cerbo is not found, press **Enter the address manually**: under **Settings → Integrations → MQTT** choose **Connect to another broker**, enter the Cerbo’s IP address as the **Server address** (port 1883) and press **Save changes**, then on the Victron GX card press **Find Victron GX** to fill in the Portal ID and **Save changes**.

The Hub always needs to know where to find the Cerbo GX. The Cerbo can be reached directly over its own access point, or through your RV router. With an RV router, give the Cerbo a fixed IP address. See the Wi-Fi setup guide on the [launchcontrol.tech FAQ](https://launchcontrol.tech/pages/support-faq) for additional detail.

The Hub is an MQTT client. Victron values arrive through the GX device’s MQTT topic tree; writable fields such as inverter mode, input current limit, and setpoints are written back through MQTT. With a Cerbo, its broker is the natural place to connect Shelly, ESPHome, and other MQTT devices; without one, the Hub can run its own broker (see the advanced MQTT section).
:::

## Shelly devices

Shelly relays, inputs, and color lights (Gen2, Gen3, and Gen4 models) connect to the Hub over MQTT and are found automatically; there are no topics to type. Point each Shelly at the broker, then choose **Devices → Add devices → Scan for Shelly devices**. A relay becomes a switch card, an input shows On or Off, and a Plus RGBW PM becomes a **Color Light** card. A Shelly button can run a macro.

Step-by-step settings, color lights, button presses, the Shelly BLU remote, and troubleshooting are in [Appendix A: Shelly Setup](#shelly-setup).

## Bluetooth sensors and monitors

The Hub listens directly to supported Bluetooth devices. There is no pairing: each device broadcasts its readings and the Hub reads the ones you add.

1. **Turn Bluetooth on.** Open **Settings → Integrations → Bluetooth**, choose **On**, and press **Save and restart**. The dashboard and displays pause for about 30 seconds and reconnect by themselves.
2. **Scan.** Press **Add Bluetooth devices** on the card, or on the Devices page choose **Add devices → Scan for Bluetooth devices**. Each device in range is listed with its kind and signal strength.
3. **Press Add** beside the ones you want, name them, and accept the offer to create a card.

If a device does not appear, **Add Bluetooth manually** lets you choose its type and enter its Bluetooth address yourself.

| Device | What you enter | Card created |
| --- | --- | --- |
| Victron solar charger (SmartSolar) | Encryption key | Victron solar card |
| Victron battery monitor (SmartShunt, BMV) | Encryption key | Battery monitor card |
| Victron AC charger, Orion Smart, Orion XS | Encryption key | Battery Charger |
| Victron SmartLithium battery | Encryption key | Voltage and temperature |
| Victron Smart BatteryProtect | Encryption key | Output state and voltage |
| Thornwave PowerMon battery monitor | Nothing | Battery monitor card |
| Garnet SeeLevel tank monitor | Nothing | One Tank card for each tank it reports |
| Mopeka propane tank sensor | Mounting, contents, and tank size | Tank |
| RuuviTag | Nothing | Temperature |
| Ruuvi Air | Nothing | CO2 and temperature |
| SwitchBot Meter, Meter Plus, Outdoor Meter, Meter Pro, Meter Pro CO2 | Nothing | Temperature and humidity (CO2 on the Pro CO2) |
| Shelly BLU H&T and other BTHome temperature sensors | Encryption key, only if the sensor is encrypted | Temperature and humidity |
| Shelly BLU Door/Window, Motion, and BTHome leak sensors | Encryption key, only if the sensor is encrypted | Open/closed, motion, or leak state |
| Shelly BLU button remote | A name, then what each press does | None; see [Shelly Setup](#shelly-setup) |

::: technical "Sensor encryption, wake-up behavior and limits"
- **Victron encryption key.** In the VictronConnect app, connect to the device, open the gear menu, then the ⋮ menu → **Product info**. Turn on **Instant readout via Bluetooth**, press **SHOW**, and copy the key. A Victron device broadcasts only while Instant readout is on. If you have a Cerbo GX, use the Victron GX integration instead; it provides more data and control.
- **Shelly BLU encryption key.** In the Shelly app, open the device’s settings → **Encryption**.
- **Finding a device.** Press the SYNC button on a Mopeka sensor, press any button on a Shelly BLU remote, or open the door or wave at a door or motion sensor while the scan runs.
- **Door, motion, and leak sensors report only when something happens.** After the Hub restarts, their card shows no state until the sensor next sends.
- **Limits.** Up to 8 Victron devices, 16 sensors, 8 propane tank sensors, 4 SeeLevel monitors, 4 PowerMon monitors, and 4 button remotes.

:::

Bluetooth sensors work like any other device: on cards and the Touch 8, as automation triggers, and in backups. You’re done when each sensor has reported its expected reading. Some event-driven sensors need to be activated first.

## Leak sensors and water valves

A leak sensor can close a water valve and send an alert by itself. Three things take part:

- **Bluetooth leak sensors** that use BTHome are added like any Bluetooth sensor (above).
- **Shelly Flood** sensors and **Shelly-powered water valves** connect over Wi-Fi and are added by hand as MQTT devices. The exact settings are in [MQTT, ESPHome & Home Assistant](#mqtt-esphome-home-assistant).
- **The automation** that joins them is described under **A leak shut-off** in [Automations & Macros](#automations-macros).

## Starlink

Starlink is set up on its dashboard card, not under Settings.

1. **Add a Starlink card.** In the scan, choose **Starlink power switch** in **What is it?** for the circuit that powers the dish; or in panel edit mode use **Add a card…** and pick Starlink.
2. **Turn on Connect to Starlink dish** in the card’s **Edit** dialog. The Hub then reads speed, latency, and obstruction from the dish itself. The Hub must be on a network that can reach the dish, and it connects to one dish.

The small card shows ping success with **Online**, **Offline**, **Searching…**, or **Dish off**. Ping success is the best single indicator of a reliable connection. The **4×4 Detailed** layout adds latency, obstruction, download and upload speed, uptime, and GPS satellites. When the card is bound to the dish’s power circuit, tapping it switches the dish on or off.

## GL.iNet travel router

With a supported GL.iNet router such as the Beryl or Slate family, the Travel Router card shows the active uplink, signal strength, and internet reachability. Tap the card to scan for and join campground or home Wi-Fi without opening the router’s administration page.

To set it up, open **Settings → Integrations → GL.iNet travel router**, turn the integration on, and press **Find router**. Enter the **Router admin password** — the one you use to sign in to the router's admin page — and press **Save changes**. The card checks the password and shows **Connected** with the router model, then offers **Add router card**. If the router is not the one the Hub connects through, press **Enter manually** and type its address under **Advanced settings**.

On routers running GL.iNet firmware 4.11 or later, the card’s detail view adds:

- **Speed Test —** press **Run speed test** for download, upload, and ping. Each test moves real data, roughly 100 MB or more on a fast link. **Schedule** can repeat it every few hours or daily at a set time; scheduled tests run only on an Ethernet or Wi-Fi uplink, never on cellular.
- **Network Quality —** overall, responsiveness, and reliability scores, with latency, jitter, DNS lookup time, and packet loss.
- **Network quality alarm —** in the card’s **Edit** dialog. The card blinks red when overall quality stays below the number you set for more than 10 seconds.

## Weather

The Weather card shows current conditions and a five-day forecast, with the next hours on a tap; the same weather can also sit in a panel's header. Open **Settings → Integrations → Weather**, turn weather on, and pick a **Weather location**:

- **Use GPS —** follows the coach, using a Victron GX device that has GPS. If GPS stops reporting, the Hub keeps the last position until it restarts, then a location you chose earlier.
- **Choose a location —** type a city or ZIP code, press **Search**, and pick the right place from the results. The card shows what you selected and what is saved, so you can tell them apart.

Press **Save changes**; the card then shows **Forecast ready** and offers **Add weather card**. **Refresh now** fetches a new forecast at once. The forecast refreshes every 30 minutes, and again once the coach has moved 20 miles. Forecast data by Open-Meteo.com; no account or key is needed.

## Other MQTT devices

This is an advanced option; you can skip it if your equipment has its own integration.

Compatible devices that publish to your MQTT broker — an ESPHome sensor, a home-built controller — can be added by hand.

1. **Connect the broker first** under **Settings → Integrations → MQTT**.
2. **Open Devices → Add devices → Configure MQTT device** and give the device a name.
3. **Add a field for each reading.** Enter a **Label** and the **MQTT Topic** to read. A field is read-only unless you also give it a **Command topic**, which the Hub publishes to when you switch or set it.
4. **Press Save,** then use **Add to dashboard** in the device’s ⋮ menu.

The Hub holds up to 48 such devices with six fields each. Topic options, worked examples, and Home Assistant are covered in [MQTT, ESPHome & Home Assistant](#mqtt-esphome-home-assistant).

## The Hub's own MQTT broker

Advanced setup: skip this section unless you are connecting equipment over MQTT.

Under **Settings → Integrations → MQTT** the **Broker** choice has two options:

- **Connect to another broker —** the Hub connects to a broker somewhere else: a Cerbo GX, a Home Assistant broker, or any other. This is the Victron setup above.
- **Use Hub's built-in broker —** the Hub runs the broker itself. Use this on a coach that has no Cerbo. The card shows the **Broker address** your devices should use (the Hub's IP address on port 1883) and how many **clients** are connected. Set a username and password on a private network; with a blank username, any device that can reach the broker can connect.

Shelly, ESPHome, and other MQTT devices are pointed at that address in their own settings. The Hub uses one broker at a time: with the built-in broker selected, the Victron GX integration is unavailable, because it reads the Cerbo's broker — the Victron GX card then says **Victron isn’t connected**.

**Publish data to MQTT** has three independent options — **RV-C data**, **Victron data**, and **Bluetooth sensor data** — and turning one on never starts the others. Changes take effect when you press **Save changes**; the card shows **Unsaved changes** until you do. Topics, payloads, and Home Assistant examples are in [MQTT, ESPHome & Home Assistant](#mqtt-esphome-home-assistant).

