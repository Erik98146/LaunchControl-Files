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

Some equipment, including thermostats, tank sensors, batteries, and inverters, regularly reports its status and normally appears without any additional action.

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

### Automatically create dashboard cards
When you select Done after adding devices, LaunchControl offers to create matching dashboard cards.

![Add Device – Found RV-C devices page](images/devices01.png)

::: technical "Technical detail"
A single device, such as a lighting dimmer, may have multiple “instances”. In the case of the dimmer, the instances define multiple switched lighting zones. Some experimentation may be necessary to figure out which physical device corresponds to which RV-C device and instance. This is best done using the test and status displays for the device. See section 14 – Technical Reference for additional detail.
:::

::: technical "Expert Mode"
To keep the found devices decluttered, some devices are hidden by default. If you can't find your RV-C device, use the Expert button to show all RV-C devices found on the bus. See chapter 14 for additional detail.
:::

## Victron equipment

If your coach has a Victron GX device such as a Cerbo GX, LaunchControl can read and control supported Victron equipment including MultiPlus inverter/chargers, battery monitors, solar chargers, GPS, and temperature sensors. This is always the best way to connect to Victron equipment and any third-party devices that use MQTT.

1. **Enable MQTT services on the Cerbo GX device: Settings → Integrations → MQTT Access On**
2. **Open Settings → Integrations.** Enable the MQTT broker and enter the Cerbo IP address and port (1883) then save. A user name and password is not required for this integration. Scroll down and enable the Victron GX integration. Auto-discover the Portal ID and save. Confirm the MQTT Broker and Victron GX integrations both show connected.
3. **Open Devices and run a Victron scan.** Add the discovered equipment. LaunchControl will create matching dashboard cards.

![Devices added after a Victron scan](images/ch03-devices-added-after-a-victron-scan.png)

::: technical
The Hub is an MQTT client. Victron field values arrive through the GX device’s MQTT topic tree; writable fields such as inverter mode, input current limit, and setpoints are written back through MQTT. The Cerbo is the best place to add non RV-C equipment like Bluetooth Ruuvi temperature sensors, Shelly devices, or ESP Home devices. See the Wi-Fi setup guide found on the [launchcontrol.tech FAQ](https://launchcontrol.tech/pages/support-faq) for additional networking details.

The hub always needs to know where to find the Cerbo GX. The Cerbo GX can be accessed directly over it's own hosted access point with a static IP, or may be accessed through your RV router. If you are using an RV router, the Cerbo GX will need static IP address. See the Wi-Fi setup guide at launchcontrol.tech for additional detail.
:::

## Bluetooth sensors

The Hub can listen directly to supported Bluetooth broadcasts without normal Bluetooth pairing:

- **Victron Instant Readout —** SmartShunts, SmartSolar chargers, and similar supported devices can broadcast readings directly, but a Cerbo GX is preferred if available.
- **Ruuvi tags —** battery-powered temperature and humidity sensors suitable for locations such as a refrigerator or outdoor reading.  

Turn Bluetooth on in Settings → Integrations, restart the Hub when prompted, then add discovered sensors from the Devices page.

::: note "Why a restart?"
Bluetooth is off by default. Turning it on or off changes how Hub memory is allocated, so the change takes effect after a restart.
:::

## Starlink

The Starlink card can show ping success when integration is activated, which is the best indicator of reliable internet. Enable Starlink in Settings → Integrations. If the card is also bound to a switched power circuit, its toggle can control dish power.

## GL.iNet travel router

With a supported GL.iNet router such as the Beryl or Slate family, the Travel Router card can show the active uplink, signal strength, and internet reachability. Tap the card to scan for and join campground or home Wi-Fi without opening the router administration page. Enable the integrations and enter the router admin password once under Settings → Integrations.

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
