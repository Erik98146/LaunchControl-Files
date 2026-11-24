# Add or Change Equipment

::: lead
The Devices page is where LaunchControl manages the equipment it knows about. Adding equipment is one screen: find it, name it, say what it is, and its dashboard cards are made at the same time. This is also where you test a device, change its name, or set up an integration such as Victron, Shelly, or Bluetooth sensors. Add only the integrations your coach actually uses.
:::

## Choose the equipment you are adding

Use only the sections that match your installation. Built-in RV equipment may be your only source; integrations are optional. [Supported Equipment](#supported-equipment) lists everything LaunchControl works with.

| Equipment | Where to begin |
| --- | --- |
| Built-in lights, pumps, tanks, or climate | **Devices → Add devices**; follow the scan below |
| Lippert OneControl equipment | Check **Settings → System → Connection protocol**; see the note below |
| Victron equipment with a GX device | **Settings → Integrations → Victron GX** |
| Shelly relays, inputs, or RGBW lights | [Shelly Setup](#shelly-setup); choose the broker before configuring devices |
| Bluetooth sensors, tank monitors, or a button remote | **Settings → Integrations → Bluetooth** |
| GL.iNet router or Weather | The matching card under **Settings → Integrations** |
| Starlink | A Starlink card on the dashboard; see [Starlink](#starlink) |
| Other MQTT equipment, including ESPHome | **Devices → Add devices → Configure MQTT device** |

::: note "OneControl installations"
For a Lippert OneControl installation, choose the matching **Connection protocol** under **Settings → System** before scanning. Changing protocol removes source-specific configuration and restarts the Hub; review the effects and back up an existing setup first. See [Settings Reference](#settings-reference).
:::

## RV-C devices

RV-C devices are the coach’s built-in lights, pumps, tanks, thermostats, awnings, slides, generators, batteries, inverters, and similar equipment. The Devices page lists everything currently configured on the Hub, grouped by its source: RV-C devices, Victron devices, and so on.

### Find equipment

1. **Open Devices.**
2. **Press Add devices.** If other sources are set up, choose **Scan RV**.
3. **Wait a few seconds.** The list fills with what the Hub hears on the RV’s control network, with a live reading on each row, in sections: **Devices you just operated**, **Needs identification**, **Ready to add**, and **Already configured**. Each row names the device type and its instance number, which is what the RV’s own paperwork uses.

Equipment that reports all the time — thermostats, tank sensors, batteries, inverters, solar — appears under Ready to add, already ticked. Lights, pumps, awnings, and other switched circuits wait under Needs identification until they are operated.

On a coach with a long list, narrow it down:

- **Search found equipment** finds a row by name.
- **Show** limits the list to one kind of equipment, such as Tank, Thermostat, or Switched output. It appears once the scan has found two or more kinds. Rows you already ticked stay ticked while they are filtered out of view.
- **Sort** orders the list by name or by the order things were found.

The **⋯ More** button holds the session details and a manual refresh. Leaving with devices ticked but not added asks first.

### Identify lights, pumps, and other switched devices

The easiest way to tell which row is which is to operate the device in the RV.

1. **Turn it on, then off,** from the RV’s own switch or panel.
2. **Watch the list.** The device that just changed moves to the top under **Devices you just operated**, ticked and highlighted in green. Work with one device at a time so it stays clear which row is which.

The other direction works too: press a row’s **ID** button to switch that output on from the Hub and see which light comes on. Press **ID** again to switch it back off. ID is offered only for lights and switched circuits; awnings, slides, and shades show a dash, because they should never be operated without someone watching them.

::: warning "Door locks"
If a switched circuit drives a door lock, pressing ID on it will operate the lock.
:::

### Add the devices

Everything happens on the one screen:

1. **Tick the devices to add.** Ready-to-add and just-operated devices start ticked; untick any you do not want. **Select all** and **none** under Ready to add tick or clear that section.
2. **Name each device** in its row — Bench Light, Kitchen Ceiling, Water Pump.
3. **Say what each switched circuit is** in its **What is it?** box. A dimmer or relay output can drive a light, a water pump, a fan, an awning, shades, a door lock, a TV lift, or a Starlink dish, and only you know which. LaunchControl shows a guess under the box but never picks for you. Choose **No card** to add the device without a dashboard card; untick the row to leave the device out. Batteries, tanks, thermostats, and the like show the card they will get.
4. **Choose where the cards go** — only when you have more than one panel, or in Expert mode. **Put the cards on**, in the bar under the list, picks the panel or makes a new one; otherwise the cards go on your dashboard.
5. **Press Add Equipment & Create Dashboard.** The bar says what one press will do — how many devices and how many cards. If a selected switched circuit has no type, you cannot continue; the red note takes you to the first unfinished row. **No card** counts as an answer and is not asked again. The devices are added one at a time and their cards are created straight after. From the setup guide, it returns you to the guide.

![Add Device – Found RV-C devices page](images/devices01.png)

::: note "The card limit"
The Hub holds up to 72 dashboard cards. The bar counts what it is about to create and the button stays off while the selection would go past that; untick a row or choose No card. It also says when more than 16 cards would keep a history graph on the Hub.
:::

### Hide equipment you will never add

Most coaches report outputs that are not connected to anything. To stop one from being offered in every scan, press **Hide** on its row. It moves to a collapsed **Hidden** section at the bottom of the list; press **Show** there and then **Unhide** to bring it back. A device you have already added cannot be hidden.

### Scanning again

A second scan folds the devices you already added under **Already configured**, with their count; press **Show** to list them anyway. When there is nothing new, the list says **Nothing new found yet** and suggests operating a light or switch.

Some coaches give their controllers new network addresses after a power cycle. A device that moved shows as **Moved here · updating** instead of as something new; the Hub updates its saved address, its cards, and its lighting zones by itself within a couple of minutes, and notes it in the alert list. Nothing to do.

### Expert mode

To keep the list readable, protocol-level detail is hidden: message numbers (DGNs), instance numbers, source addresses, and the rarely used device types. **Expert mode** — the switch at the top of the Devices page, and the same switch in the scan — shows all of it, on every page of LaunchControl, in this browser. If you cannot find a device, turn Expert mode on; some device types are listed only there. See the [Technical Reference](#technical-reference) for what the numbers mean.

### Change a device

Select a device in the list to test it, rename it, or edit its fields — which readings are shown, their units and rounding, a tank’s size, a dimmer’s memory behavior. A device’s ⋮ menu offers **Add to dashboard** for a device that has no card yet, and **Remove**. Removing a device clears its card bindings and deletes a card left with nothing bound.

## Tank size and calibration

A tank sensor reports a percentage. Two optional settings turn that into an amount. Open **Devices**, select the tank, and edit it.

### Tank size

Enter how much the tank holds when full under **Tank size** and press **Save**. The Tank card then shows how much is in the tank as well as the percentage, in gallons or liters according to the Hub’s units setting. This is all a rectangular tank needs.

### Geometry Lookup for an odd-shaped tank

A sensor measures the liquid level, which does not match the contents of an irregular tank. **Geometry Lookup** corrects it with a table you build once by adding known amounts of water.

1. **Level the RV and empty the tank.**
2. **Tick Geometry Lookup, then press Start.** The first entry, 0 added, is recorded for you.
3. **Add water in known amounts.** After each amount, type it under **Water added since last entry** and press **Save Entry**. A water flow meter helps. Amounts of 1–2 gallons give a good table; up to 32 entries are kept. **Undo Last** removes a mistake.
4. **Press Finish when the tank is full.** This also sets the tank size, so there is no need to enter it separately.

The correction applies immediately on the dashboard and the displays. **Export CSV** saves the table for backup or for another coach with the same tank; **Import CSV** loads one instead of entering the points by hand. **Recalibrate** starts over and **Remove Table** returns to the plain sensor reading.

### Wavetronix Fathom sensors

A Fathom sensor arrives set up as fresh tank 1 on a tank 39.3 inches deep, so it needs to be told what it is really mounted on. Press **Fathom sensor setup…** in the tank’s editor, or **Set up** on its row in the scan.

1. **Choose the tank** the sensor is on: fresh, gray, or black, 1 to 3.
2. **Enter the tank’s depth** as a single region, in inches from the bottom.
3. **Press Program sensor.** With the tank empty, **Tank is empty** lets the sensor size itself.

Changing which tank the sensor reports makes it come back as a new device: add it from the scan, then remove the old entry.

::: note "One correction at a time"
For an odd-shaped tank, leave the Fathom with one region and use Geometry Lookup in the Hub. LaunchControl does not allow both a multi-region table in the sensor and Geometry Lookup, because two corrections stacked on each other give wrong readings.
:::

## Victron equipment

If your coach has a Victron GX device such as a Cerbo GX, LaunchControl can read and control supported Victron equipment including MultiPlus inverter/chargers, battery monitors, solar chargers, GPS, and temperature sensors. Use the GX integration when you have a supported GX device. Other MQTT equipment can share its broker.

1. **Enable MQTT on the Cerbo GX.** On the GX device: Settings → Services → **MQTT on LAN (plaintext)** on.
2. **Find the Cerbo.** On the Hub, open **Settings → Integrations → Victron GX** and press **Set up**. Press **Find Cerbo GX**; the Hub looks for the GX device on your network and offers it. Press **Use this Cerbo**. LaunchControl connects MQTT to it, finds its Portal ID, and turns Victron on, in one go.
3. **Add the equipment.** Press **Add Victron devices** on the Victron GX card, or open Devices and run a Victron scan. Add the discovered equipment; LaunchControl creates matching dashboard cards.

![Devices added after a Victron scan](images/ch03-devices-added-after-a-victron-scan.png)

If the Cerbo is not found, press **Enter the address manually**: under **Settings → Integrations → MQTT** choose **Connect to another broker**, enter the Cerbo’s IP address as the **Server address** (port 1883) and press **Save changes**, then on the Victron GX card press **Find Victron GX** to fill in the Portal ID and **Save changes**.

The Hub always needs to know where to find the Cerbo GX. The Cerbo can be reached directly over its own access point, or through your RV router. With an RV router, give the Cerbo a fixed IP address. See the Wi-Fi setup guide on the [launchcontrol.tech FAQ](https://launchcontrol.tech/pages/support-faq) for additional detail.

::: technical
The Hub is an MQTT client. Victron values arrive through the GX device’s MQTT topic tree; writable fields such as inverter mode, input current limit, and setpoints are written back through MQTT. With a Cerbo, its broker is the natural place to connect Shelly, ESPHome, and other MQTT devices; without one, the Hub can run its own broker (below).
:::

## The Hub's own MQTT broker

Under **Settings → Integrations → MQTT** the **Broker** choice has two options:

- **Connect to another broker —** the Hub connects to a broker somewhere else: a Cerbo GX, a Home Assistant broker, or any other. This is the Victron setup above.
- **Use Hub's built-in broker —** the Hub runs the broker itself. Use this on a coach that has no Cerbo. The card shows the **Broker address** your devices should use (the Hub's IP address on port 1883) and how many **clients** are connected. The username and password are optional: leave the username blank and any device on the RV network can connect; enter one and devices must sign in with it and the password.

Shelly, ESPHome, and other MQTT devices are pointed at that address in their own settings. The Hub uses one broker at a time: with the built-in broker selected, the Victron GX integration is unavailable, because it reads the Cerbo's broker — the Victron GX card then says **Victron isn’t connected**.

**Publish data to MQTT** has three independent options — **RV-C data**, **Victron data**, and **Bluetooth sensor data** — and turning one on never starts the others. Changes take effect when you press **Save changes**; the card shows **Unsaved changes** until you do. Topics, payloads, and Home Assistant examples are in [MQTT, ESPHome & Home Assistant](#mqtt-esphome-home-assistant).

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
| Mopeka or Lippert propane tank sensor | Mounting, contents, and tank size | Tank |
| RuuviTag | Nothing | Temperature |
| Ruuvi Air | Nothing | CO2 and temperature |
| SwitchBot Meter, Meter Plus, Outdoor Meter, Meter Pro, Meter Pro CO2 | Nothing | Temperature and humidity (CO2 on the Pro CO2) |
| Shelly BLU H&T and other BTHome temperature sensors | Encryption key, only if the sensor is encrypted | Temperature and humidity |
| Shelly BLU Door/Window, Motion, and BTHome leak sensors | Encryption key, only if the sensor is encrypted | Open/closed, motion, or leak state |
| Shelly BLU button remote | A name, then what each press does | None; see [Shelly Setup](#shelly-setup) |

Things to know:

- **Victron encryption key.** In the VictronConnect app, connect to the device, open the gear menu, then the ⋮ menu → **Product info**. Turn on **Instant readout via Bluetooth**, press **SHOW**, and copy the key. A Victron device broadcasts only while Instant readout is on. If you have a Cerbo GX, use the Victron GX integration instead; it provides more data and control.
- **Shelly BLU encryption key.** In the Shelly app, open the device’s settings → **Encryption**.
- **Finding a device.** Press the SYNC button on a Mopeka or Lippert sensor, press any button on a Shelly BLU remote, or open the door or wave at a door or motion sensor while the scan runs.
- **Door, motion, and leak sensors report only when something happens.** After the Hub restarts, their card shows no state until the sensor next sends.
- **Limits.** Up to 8 Victron devices, 16 sensors, 8 propane tank sensors, 4 SeeLevel monitors, 4 PowerMon monitors, and 4 button remotes.

Bluetooth sensors work like any other device: on cards and the Touch 8, as automation triggers, and in backups.

::: note "Why a restart?"
Bluetooth is off by default. Turning it on or off changes how Hub memory is allocated, so the change takes effect after a restart. Saving does the restart for you.
:::

::: note "Newer devices"
Support for SwitchBot meters, BTHome sensors, Ruuvi Air, and the Victron charger, SmartLithium, and BatteryProtect types is recent. If a reading looks wrong, send a support file so it can be checked against your device.
:::

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

Anything that publishes to your MQTT broker — an ESPHome sensor, a home-built controller — can be added by hand.

1. **Connect the broker first** under **Settings → Integrations → MQTT**.
2. **Open Devices → Add devices → Configure MQTT device** and give the device a name.
3. **Add a field for each reading.** Enter a **Label** and the **MQTT Topic** to read. A field is read-only unless you also give it a **Command topic**, which the Hub publishes to when you switch or set it.
4. **Press Save,** then use **Add to dashboard** in the device’s ⋮ menu.

The Hub holds up to 48 such devices with six fields each. Topic options, worked examples, and Home Assistant are covered in [MQTT, ESPHome & Home Assistant](#mqtt-esphome-home-assistant).
