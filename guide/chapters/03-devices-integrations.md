# Devices & Integrations

::: lead
The Devices page is where LaunchControl manages the equipment it knows about. If you loaded a floor plan, many RV-C devices may already be present. This is also the place you can test device control and status. Add only the integrations and devices your coach actually uses.
:::

## RV-C devices

RV-C devices include the coach’s built-in lights, pumps, tanks, thermostats, awnings, slides, generators, batteries, inverters, and similar equipment.

The Devices page lists everything currently configured on the Hub. Devices are organized into groups based on their source, such as RV-C Devices and Victron Devices.

### Scan for RV-C devices

1. **Open Devices.**
2. **Select Add Devices.** 
3. **Begin the scan.**

LaunchControl listens to the RV-C network and displays the device types it finds.

Some equipment, including thermostats, tank sensors, batteries, and inverters, regularly report status and normally appears without any additional action.

Other equipment, including lights, pumps, awnings, and switched circuits, may not appear until it is operated.

### Identify lights, pumps, and other switched devices
The easiest way to identify a switched device is to operate it from the RV’s original control panel or switch.

1. **Begin and RV-C device scan.**
2. **Turn a device on then off.** 
3. **Watch the results.** The most recent device reporting the change moves toward the top of the list and is highlighted.
4. **Select the identified device.** 
5. **Give it a meaningful name** 

Repeat the process as needed.

Work with one device at a time so it is clear which RV-C instance corresponds to each physical control.

When you have finished identifying devices, select Done. LaunchControl can then create dashboard cards for the devices you added.

Confirm device and card types

LaunchControl normally recognizes the appropriate device type, but several different RV functions may appear as generic switches on the RV-C network.

Before creating the dashboard cards, review each detected type. For example, change a generic switch to Water Pump when it controls the pump. Choosing the correct type gives the card the proper name, icon, controls, and behavior.

### Add continuously reporting devices
After identifying switches and lights, run another scan to add equipment that is already visible on the network. This may include:

- House batteries
- Inverters and chargers
- Fresh, gray, and black tanks
- Thermostats
- Generator information
- Solar and other power equipment

Select a device, review or change its name, and choose Save and Add More until everything needed has been added.

### Add many devices at once
On a large coach coach with many lights, shades, etc., adding them one by one is slow. The **All Detected Devices** list has a tick box on every row for adding several devices in one pass.

1. **Tick the devices to add.** Use **Select all** or **Select none** to tick or clear every row on screen.
2. **Select Add all selected.** A review table lists each ticked device with its type, DGN, and instance.
3. **Name each device.** Type a name in each row, or select **Remove** to leave a device out.
4. **Select Add all.** The devices are added one at a time. If any cannot be added, the page lists them and the rest are still added. LaunchControl then offers to create their dashboard cards.

### Identify from the review table (ID button)
Operating a switch in the coach tells you which device is which. The **ID** button works the other way around: it switches a device on from the Hub so you can see which light comes on. This is the easiest way to tell a dozen identical lighting channels apart.

- Select **ID** once to switch the output on. The button stays highlighted while it is on.
- Select **ID** again to switch it back off.
- Give the device a name.

ID is offered only for lights and switched circuits. Awnings, slides, shades, and other moving equipment show a dash instead, because they should never be operated without someone watching them.

::: warning "Door locks"
If a switched circuit drives a door lock, pressing ID on it will operate the lock.
:::

### Automatically create dashboard cards
When you select Done after adding devices, LaunchControl offers to create matching dashboard cards.

![Add Device – Found RV-C devices page](images/devices01.png)

::: technical "Technical detail"
A single device, such as a lighting dimmer, may have multiple “instances”. In the case of the dimmer, the instances define multiple switched lighting zones. Some experimentation may be necessary to figure out which physical device corresponds to which RV-C device and instance. This is best done using the test and status displays for the device. See section 14 – Technical Reference for additional detail.
:::

::: technical "Expert Mode"
To keep the found devices decluttered, some devices are hidden by default. If you can't find your RV-C device, use the Expert button to show all RV-C devices found on the bus. See the [Technical Reference](#technical-reference) for additional detail.
:::

## Victron equipment

If your coach has a Victron GX device such as a Cerbo GX, LaunchControl can read and control supported Victron equipment including MultiPlus inverter/chargers, battery monitors, solar chargers, GPS, and temperature sensors. This is always the best way to connect to Victron equipment and any third-party devices that use MQTT.

1. **Enable MQTT services on the Cerbo GX device: Settings → Integrations → MQTT Access On**
2. **Connect MQTT to the Cerbo.** Open **Settings → Integrations → MQTT** and press **Set up**. Turn on MQTT, choose **Connect to another broker**, enter the Cerbo's IP address as the **Server address** (port 1883), and press **Save changes**. A username and password are not required for this integration. The card shows **Connected** once the Hub reaches the Cerbo.
3. **Turn on Victron GX.** Open the **Victron GX** card on the same page. Its checklist shows whether MQTT is ready; if not, **Configure MQTT** takes you straight to the MQTT card. Turn on Victron GX, press **Find Victron GX** to fill in the Portal ID (or **Enter manually** — it is on the GX under Settings → VRM online portal → VRM Portal ID), and press **Save changes**.
4. **Add the equipment.** Press **Add Victron devices** on the Victron GX card, or open Devices and run a Victron scan. Add the discovered equipment. LaunchControl will create matching dashboard cards.

![Devices added after a Victron scan](images/ch03-devices-added-after-a-victron-scan.png)

::: technical
The Hub is an MQTT client. Victron field values arrive through the GX device’s MQTT topic tree; writable fields such as inverter mode, input current limit, and setpoints are written back through MQTT. With a Cerbo, its broker is the natural place to add non RV-C equipment like Bluetooth Ruuvi temperature sensors, Shelly devices, or ESPHome devices; without one, the Hub can run its own broker (below). See the Wi-Fi setup guide found on the [launchcontrol.tech FAQ](https://launchcontrol.tech/pages/support-faq) for additional networking details.
:::

The hub always needs to know where to find the Cerbo GX. The Cerbo GX can be accessed directly over it's own hosted access point with a static IP, or may be accessed through your RV router. If you are using an RV router, the Cerbo GX will need static IP address. See the Wi-Fi setup guide at launchcontrol.tech for additional detail.

## The Hub's own MQTT broker

Under **Settings → Integrations → MQTT** the **Broker** choice has two options:

- **Connect to another broker —** the Hub connects to a broker somewhere else: a Cerbo GX, a Home Assistant broker, or any other. This is the Victron setup above.
- **Use Hub's built-in broker —** the Hub runs the broker itself. Use this on a coach that has no Cerbo. The card shows the **Broker address** your devices should use (the Hub's IP address on port 1883) and how many **clients** are connected. The username and password are optional: leave the username blank and any device on the coach network can connect; enter one and devices must sign in with it and the password.

Shelly, ESPHome and other MQTT devices are pointed at that address in their own settings. Home Assistant, Node-RED or MQTT Explorer can connect to it too and will see the Hub's published fields. The Hub uses one broker at a time: with the built-in broker selected, the Victron GX integration is unavailable, because it reads the Cerbo's broker — the Victron GX card then says **MQTT connection required**.

**Publish data to MQTT** has three independent options — **RV-C data**, **Victron data** and **Bluetooth sensor data** — and turning one on never starts the others. RV-C data covers the fields marked "MQTT" on the Devices page. The topic prefix is under **Advanced settings**. Changes take effect when you press **Save changes**; the card shows **Unsaved changes** until you do.

::: note "Coming later"
Automatic discovery of Shelly and ESPHome devices on the Devices page, with cards created for them, is planned. Until then, add them as Custom MQTT devices (below).
:::

## Bluetooth sensors

The Hub can listen directly to supported Bluetooth broadcasts without normal Bluetooth pairing:

- **Victron Instant Readout —** SmartShunts, SmartSolar chargers, and similar supported devices can broadcast readings directly, but a Cerbo GX is preferred if available.
- **Ruuvi tags —** battery-powered temperature and humidity sensors suitable for locations such as a refrigerator or outdoor reading.  

Open **Settings → Integrations → Bluetooth**, choose **On** and press **Save and restart**. The Hub restarts — the dashboard and displays pause for about 30 seconds and reconnect by themselves — and the card confirms Bluetooth is on. Then press **Add Bluetooth devices** (or use the Devices page) to add the sensors you want; the Hub only reads devices you add.

::: note "Why a restart?"
Bluetooth is off by default. Turning it on or off changes how Hub memory is allocated, so the change takes effect after a restart. Saving does the restart for you.
:::

## Starlink

The Starlink card can show ping success when integration is activated, which is the best indicator of reliable internet. Enable Starlink in Settings → Integrations. If the card is also bound to a switched power circuit, its toggle can control dish power.

## GL.iNet travel router

With a supported GL.iNet router such as the Beryl or Slate family, the Travel Router card can show the active uplink, signal strength, and internet reachability. Tap the card to scan for and join campground or home Wi-Fi without opening the router administration page.

To set it up, open **Settings → Integrations → GL.iNet travel router**, turn the integration on and press **Find router**. Enter the **Router admin password** — the one you use to sign in to the router's admin page — and press **Save changes**. The card checks the password and shows **Connected** with the router model, then offers **Add router card**. If the router is not the one the Hub connects through, press **Enter manually** and type its address under **Advanced settings**.

## Weather

The Weather card shows current conditions and a five-day forecast, with the next hours on a tap; the same weather can also sit in a panel's header. Open **Settings → Integrations → Weather**, turn weather on and pick a **Weather location**:

- **Use GPS —** follows the coach, using a Victron GX device that has GPS. If GPS stops reporting, the Hub keeps the last position until it restarts, then a location you chose earlier.
- **Choose a location —** type a city or ZIP code, press **Search**, and pick the right place from the results. The card shows what you selected and what is saved, so you can tell them apart.

Press **Save changes**; the card then shows **Forecast ready** and offers **Add weather card**. **Refresh now** fetches a new forecast at once. The forecast refreshes every 30 minutes, and again once the coach has moved 20 miles. Forecast data by Open-Meteo.com; no account or key is needed.

## Custom MQTT devices

Advanced users can add devices that publish to an MQTT broker. Map MQTT topics to LaunchControl fields for card bindings; writable topics can accept commands. This provides a general integration path for equipment that LaunchControl does not support natively.

## Tank Geometry Calibration (Optional)

Tank sensors report the liquid level at the sensor, which may not accurately represent the amount of liquid in an irregularly shaped tank. LaunchControl’s optional Geometry Lookup feature corrects this by comparing the sensor reading with the tank’s actual contents. After calibration the tank will report the actual percentage and amount remaining.

One-time tank calibration process:

- Level the RV.
- Open Devices and edit the tank device.
- Enable Geometry Lookup.
- Begin with the tank empty, then fill it in measured increments (a water flow meter is very helpful).
- The more increments recorded, the better results. We suggest entering data around 1 or 2 gal increments.
- At each step, enter the amount of liquid added.
- Finish the calibration when full and this will also record the maximum size of the tank

LaunchControl uses these calibration points to calculate a corrected percentage and estimate the amount remaining. Volume is displayed in gallons or liters according to the Hub-wide units setting.

Calibration tables can be exported as CSV files for backup or reuse. You can also import a compatible CSV table instead of entering the calibration points manually.
