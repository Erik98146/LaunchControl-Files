# Add or Change Equipment

::: lead
The Devices page is where LaunchControl manages the equipment it knows about. Adding equipment is one screen: find it, name it, say what it is, and its dashboard cards are made at the same time. This is also where you test a device, change its name, or set up an integration such as Victron, Shelly or Bluetooth sensors. Add only the integrations your coach actually uses.
:::

## Choose the equipment you are adding

Use only the sections that match your installation. Built-in RV equipment may be your only source; integrations are optional.

| Equipment | Where to begin |
| --- | --- |
| Built-in lights, pumps, tanks, or climate | **Devices → Add devices**; follow the scan below |
| Lippert OneControl equipment | Check **Settings → System → Connection protocol**; see the note below |
| Victron equipment with a GX device | **Settings → Integrations → Victron GX** |
| Shelly relays, inputs, or RGBW lights | [Shelly Setup](#shelly-setup); choose the broker before configuring devices |
| Bluetooth sensors or a Shelly BLU remote | **Settings → Integrations → Bluetooth** |
| Starlink, GL.iNet router, or Weather | The matching card under **Settings → Integrations** |
| Other MQTT equipment | Custom MQTT devices; technical setup is optional |

::: note "OneControl installations"
For a Lippert OneControl installation, choose the matching **Connection protocol** under **Settings → System** before scanning. Changing protocol removes source-specific configuration and restarts the Hub; review the effects and back up an existing setup first. See [Settings Reference](#settings-reference).
:::

## RV-C devices

RV-C devices are the coach’s built-in lights, pumps, tanks, thermostats, awnings, slides, generators, batteries, inverters, and similar equipment. The Devices page lists everything currently configured on the Hub, grouped by its source: RV-C devices, Victron devices, and so on.

### Find equipment

1. **Open Devices.**
2. **Press Add devices.** If other sources are set up, choose **Scan RV**.
3. **Wait a few seconds.** The list fills with what the Hub hears on the RV’s control network, with a live reading on each row, in sections: **Devices you just operated**, **Needs identification**, **Ready to add** and **Already configured**. Each row names the device type and its instance number, which is what the RV’s own paperwork uses; the **⋯ More** button holds the session details and a manual refresh. Leaving with devices ticked but not added asks first.

Equipment that reports all the time — thermostats, tank sensors, batteries, inverters, solar — appears under Ready to add, already ticked. Lights, pumps, awnings and other switched circuits wait under Needs identification until they are operated.

### Identify lights, pumps, and other switched devices

The easiest way to tell which row is which is to operate the device in the RV.

1. **Turn it on, then off,** from the RV’s own switch or panel.
2. **Watch the list.** The device that just changed moves to the top under **Devices you just operated**, ticked and highlighted in green. Work with one device at a time so it stays clear which row is which.

The other direction works too: press a row’s **ID** button to switch that output on from the Hub and see which light comes on. Press **ID** again to switch it back off. ID is offered only for lights and switched circuits; awnings, slides and shades show a dash, because they should never be operated without someone watching them.

::: warning "Door locks"
If a switched circuit drives a door lock, pressing ID on it will operate the lock.
:::

### Add the devices

Everything happens on the one screen:

1. **Tick the devices to add.** Ready-to-add and just-operated devices start ticked; untick any you do not want. **Select all** and **none** under Ready to add tick or clear that section.
2. **Name each device** in its row — Bench Light, Kitchen Ceiling, Water Pump.
3. **Say what each switched circuit is** in its **What is it?** box. A dimmer or relay output can drive a light, a water pump, a fan, an awning, shades, a door lock or a Starlink dish, and only you know which. LaunchControl shows a guess under the box but never picks for you. Choose **No card** to add the device without a dashboard card; untick the row to leave the device out. Batteries, tanks, thermostats and the like show the card they will get.
4. **Choose where the cards go** — only when you have more than one dashboard, or in Expert mode. **Put the cards on**, in the bar under the list, picks the panel or makes a new one; otherwise the cards go on your dashboard.
5. **Press Add Equipment & Create Dashboard.** The bar says what one press will do — how many devices and how many cards. If a selected switched circuit has no type, you cannot continue. The red note takes you to the first unfinished row. **No card** counts as an answer and is not requested again. The devices are added one at a time and their cards are created straight after. From the setup guide it returns you to the guide.

![Add Device – Found RV-C devices page](images/devices01.png)

::: note "The card limit"
The Hub holds up to 72 dashboard cards. The bar counts what it is about to create and the button stays off while the selection would go past that; untick a row or choose No card. It also says when more than 16 cards would keep a history graph on the Hub.
:::

### Scanning again

A second scan folds the devices you already added under **Already configured**, with their count; press **Show** to list them anyway.

Some coaches give their controllers new network addresses after a power cycle. A device that moved shows as **Moved here · updating** instead of as something new; the Hub updates its saved address, its cards and its lighting zones by itself within a couple of minutes, and notes it in the alert list. Nothing to do.

### Expert mode

To keep the list readable, protocol-level detail is hidden: message numbers (DGNs), instance numbers, source addresses and the rarely used device types. **Expert mode** — the switch at the top of the Devices page, and the same switch in the scan — shows all of it, on every page of LaunchControl, in this browser. If you cannot find a device, turn Expert mode on; some device types are listed only there. See the [Technical Reference](#technical-reference) for what the numbers mean.

### Change a device

Select a device in the list to test it, rename it, or edit its fields — which readings are shown, their units and rounding, a tank’s geometry table, a dimmer’s memory behaviour. A device’s ⋮ menu offers **Add to dashboard** for a device that has no card yet, and **Remove**. Removing a device clears its card bindings and deletes a card left with nothing bound.

## Victron equipment

If your coach has a Victron GX device such as a Cerbo GX, LaunchControl can read and control supported Victron equipment including MultiPlus inverter/chargers, battery monitors, solar chargers, GPS, and temperature sensors. Use the GX integration when you have a supported GX device. Other MQTT equipment can share its broker.

1. **Enable MQTT on the Cerbo GX.** On the GX device: Settings → Services → **MQTT on LAN (plaintext)** on.
2. **Find the Cerbo.** On the Hub, open **Settings → Integrations → Victron GX** and press **Set up**. Press **Find Cerbo GX**; the Hub looks for the GX device on your network and offers it. Press **Use this Cerbo**. LaunchControl connects MQTT to it, finds its Portal ID and turns Victron on, in one go.
3. **Add the equipment.** Press **Add Victron devices** on the Victron GX card, or open Devices and run a Victron scan. Add the discovered equipment; LaunchControl creates matching dashboard cards.

![Devices added after a Victron scan](images/ch03-devices-added-after-a-victron-scan.png)

If the Cerbo is not found, press **Enter the address manually**: under **Settings → Integrations → MQTT** choose **Connect to another broker**, enter the Cerbo’s IP address as the **Server address** (port 1883) and press **Save changes**, then on the Victron GX card press **Find Victron GX** to fill in the Portal ID and **Save changes**.

::: technical
The Hub is an MQTT client. Victron field values arrive through the GX device’s MQTT topic tree; writable fields such as inverter mode, input current limit, and setpoints are written back through MQTT. With a Cerbo, its broker is the natural place to add non RV-C equipment like Bluetooth Ruuvi temperature sensors, Shelly devices, or ESPHome devices; without one, the Hub can run its own broker (below). See the Wi-Fi setup guide found on the [launchcontrol.tech FAQ](https://launchcontrol.tech/pages/support-faq) for additional networking details.
:::

The Hub always needs to know where to find the Cerbo GX. The Cerbo GX can be accessed directly over its own hosted access point with a static IP, or through your RV router. If you are using an RV router, the Cerbo GX will need a static IP address. See the Wi-Fi setup guide at launchcontrol.tech for additional detail.

## The Hub's own MQTT broker

Under **Settings → Integrations → MQTT** the **Broker** choice has two options:

- **Connect to another broker —** the Hub connects to a broker somewhere else: a Cerbo GX, a Home Assistant broker, or any other. This is the Victron setup above.
- **Use Hub's built-in broker —** the Hub runs the broker itself. Use this on a coach that has no Cerbo. The card shows the **Broker address** your devices should use (the Hub's IP address on port 1883) and how many **clients** are connected. The username and password are optional: leave the username blank and any device on the coach network can connect; enter one and devices must sign in with it and the password.

Shelly, ESPHome and other MQTT devices are pointed at that address in their own settings. Home Assistant, Node-RED or MQTT Explorer can connect to it too and will see the Hub's published fields. The Hub uses one broker at a time: with the built-in broker selected, the Victron GX integration is unavailable, because it reads the Cerbo's broker — the Victron GX card then says **Victron isn’t connected**.

**Publish data to MQTT** has three independent options — **RV-C data**, **Victron data** and **Bluetooth sensor data** — and turning one on never starts the others. RV-C data covers the fields marked "MQTT" on the Devices page. The topic prefix is under **Advanced settings**. Changes take effect when you press **Save changes**; the card shows **Unsaved changes** until you do.

## Shelly devices

Shelly relays, inputs and colour lights (Gen2, Gen3 and Gen4 models such as the Plus, Pro and Gen4 lines, and the Plus RGBW PM) connect to the Hub over MQTT and are found automatically: there are no topics to type. The short version:

1. **Choose the broker.** If you use Victron GX, keep **Connect to another broker** and use the Cerbo’s broker address. Otherwise, in **Settings → Integrations → MQTT**, turn on MQTT, choose **Use Hub's built-in broker**, and press **Save changes**. Note the **Broker address**.
2. **Point the Shelly at that broker.** On the Shelly's own web page, open **Settings → MQTT**, turn MQTT on, enter the chosen broker address as the server, and turn on **RPC status notifications** and **Generic status update**. Leave the client ID / prefix at its default.
3. **Add it.** On the Devices page choose **Add devices → Scan for Shelly devices**. Each relay, input and colour light appears within a minute; press **Add** for the ones you want.
4. **Create cards.** Close the list and accept **Create cards**. A relay becomes a switch card (with its wired switch input shown under the icon when it has one); an input-only device such as a Plus i4 becomes a card that shows On or Off; a colour light becomes a **Color Light** card.

A **Color Light** card switches the light on or off with a tap. Press and hold it for the colour wheel and three sliders: **Color** (the brightness of the coloured LEDs), **White** (the white LEDs, set separately) and **Master** (both together, keeping their balance). Colour lights can be added to a Lighting card's zones and scenes, and a scene remembers each light's colour and levels.

Shelly devices work everywhere other devices do: on the Touch 8, in automations (a Shelly input can trigger a rule, and **Switch a card** can turn a Shelly relay on or off), and in backups. An input set to **Button** mode in the Shelly app has no on/off state, so it does not get a card; instead it can run a macro on a single, double, triple or long press.

::: note "Full setup"
Step-by-step settings, colour lights, button presses, automations and troubleshooting are in [Appendix A: Shelly Setup](#shelly-setup).
:::

ESPHome discovery is planned. Until then, add ESPHome and other MQTT devices as Custom MQTT devices (below).

## Bluetooth sensors

The Hub can listen directly to supported Bluetooth broadcasts without normal Bluetooth pairing:

- **Victron Instant Readout —** SmartShunts, SmartSolar chargers, and similar supported devices can broadcast readings directly, but a Cerbo GX is preferred if available.
- **Ruuvi tags —** battery-powered temperature and humidity sensors suitable for locations such as a refrigerator or outdoor reading.
- **Shelly BLU button remotes —** each press of each button runs a macro, recalls a lighting scene, switches a device or turns an automation on or off. See [Shelly Setup](#shelly-setup).
- **Garnet SeeLevel —** Bluetooth tank monitors; each tank they report becomes a Tank card.

Open **Settings → Integrations → Bluetooth**, choose **On** and press **Save and restart**. The Hub restarts — the dashboard and displays pause for about 30 seconds and reconnect by themselves — and the card confirms Bluetooth is on. Then press **Add Bluetooth devices** (or use the Devices page) to add the sensors you want; the Hub only reads devices you add.

::: note "Why a restart?"
Bluetooth is off by default. Turning it on or off changes how Hub memory is allocated, so the change takes effect after a restart. Saving does the restart for you.
:::

## Starlink

The Starlink card can show ping success when the integration is activated, which is the best indicator of reliable internet. Enable Starlink in Settings → Integrations. If the card is also bound to a switched power circuit, its toggle can control dish power.

## GL.iNet travel router

With a supported GL.iNet router such as the Beryl or Slate family, the Travel Router card can show the active uplink, signal strength, and internet reachability. Tap the card to scan for and join campground or home Wi-Fi without opening the router administration page.

To set it up, open **Settings → Integrations → GL.iNet travel router**, turn the integration on and press **Find router**. Enter the **Router admin password** — the one you use to sign in to the router's admin page — and press **Save changes**. The card checks the password and shows **Connected** with the router model, then offers **Add router card**. If the router is not the one the Hub connects through, press **Enter manually** and type its address under **Advanced settings**.

## Weather

The Weather card shows current conditions and a five-day forecast, with the next hours on a tap; the same weather can also sit in a panel's header. Open **Settings → Integrations → Weather**, turn weather on and pick a **Weather location**:

- **Use GPS —** follows the coach, using a Victron GX device that has GPS. If GPS stops reporting, the Hub keeps the last position until it restarts, then a location you chose earlier.
- **Choose a location —** type a city or ZIP code, press **Search**, and pick the right place from the results. The card shows what you selected and what is saved, so you can tell them apart.

Press **Save changes**; the card then shows **Forecast ready** and offers **Add weather card**. **Refresh now** fetches a new forecast at once. The forecast refreshes every 30 minutes, and again once the coach has moved 20 miles. Forecast data by Open-Meteo.com; no account or key is needed.

## Custom MQTT devices

::: technical "Custom MQTT integration"
Advanced users can add devices that publish to an MQTT broker. Map MQTT topics to LaunchControl fields for card bindings; writable topics can accept commands. This provides a general integration path for equipment that LaunchControl does not support natively.
:::

## Tank Geometry Calibration (Optional)

Tank sensors report the liquid level at the sensor, which may not accurately represent the amount of liquid in an irregularly shaped tank. LaunchControl’s optional Geometry Lookup feature corrects this by comparing the sensor reading with the tank’s actual contents. After calibration the tank will report the actual percentage and amount remaining.

1. **Level the RV** and begin with the tank empty.
2. **Open Devices**, edit the tank, and enable **Geometry Lookup**.
3. **Fill in measured increments.** A water flow meter helps. Suggested increments are 1–2 gallons; more calibration points improve the result.
4. **Record each increment** by entering the amount of liquid added.
5. **Finish when full.** This also records the tank’s maximum capacity.

LaunchControl uses these calibration points to calculate a corrected percentage and estimate the amount remaining. Volume is displayed in gallons or liters according to the Hub-wide units setting.

Calibration tables can be exported as CSV files for backup or reuse. You can also import a compatible CSV table instead of entering the calibration points manually.
