# Devices & Integrations

::: lead
The Devices page is where LaunchControl manages the equipment it knows about. If you loaded a floor plan, many RV-C devices may already be present. This is also the place you can test device control and status. Add only the integrations and devices your coach actually uses.
:::

## RV-C devices

RV-C devices are the coach’s built-in equipment: lights, tanks, thermostats, pumps, awnings, slides, generators, and similar systems. Use Add a Device → Add RV-C Device to scan the bus, identify active devices, name them, and add them to LaunchControl. A loaded floor plan performs this work for supported equipment.

::: note "Adding RV-C devices"
RV-C devices will show up on the RV-C Add Device list as soon as they send data. For many devices this takes just a few seconds because they regularly send status updates (like temperature, or tank status). For other devices, like light switches or awnings, you will need to toggle the device elsewhere to see it appear in the list.
:::

![Add Device – Found RV-C devices page](images/ch03-add-device-found-rv-c-devices-page.png)

::: technical "Technical detail"
A single device, such as a lighting dimmer, may have multiple “instances”. In the case of the dimmer, the instances define multiple switched lighting zones. Some experimentation may be necessary to figure out which physical device corresponds to which RV-C device and instance. This is best done using the test and status displays for the device. See section 14 – Technical Reference for additional detail.
:::

::: note "Expert Mode"
To keep the found devices decluttered, some devices are hidden by default. If you can't find your RV-C device, use the Expert button to show all RV-C devices found on the bus.
:::

## Victron equipment

If your coach has a Victron GX device such as a Cerbo GX, LaunchControl can read and control supported Victron equipment including MultiPlus inverter/chargers, battery monitors, solar chargers, GPS, and temperature sensors.

1. **Enable MQTT services on the Cerbo GX device: Settings → Integrations → MQTT Access On**
2. **Open Settings → Integrations.** Enable the MQTT broker and enter the Cerbo IP address and port (1883) then save. A user name and password is not required for this integration. Scroll down and enable the Victron GX integration. Auto-discover the Portal ID and save. Confirm the MQTT Broker and Victron GX integrations both show connected.
3. **Open Devices and run a Victron scan.** Add the discovered equipment. LaunchControl can also create matching dashboard cards.

![Devices added after a Victron scan](images/ch03-devices-added-after-a-victron-scan.png)

::: technical
The Hub is an MQTT client. Victron field values arrive through the GX device’s MQTT topic tree; writable fields such as inverter mode, input current limit, and setpoints are written back through MQTT. The Cerbo is the best place to add non RV-C equipment like Bluetooth Ruuvi temperature sensors, Shelly devices, or ESP Home devices. See the Wi-Fi setup guide found on the [launchcontrol.tech FAQ](https://launchcontrol.tech/pages/support-faq) for additional networking details.
:::

## Bluetooth sensors

The Hub can listen directly to supported Bluetooth broadcasts without normal Bluetooth pairing:

- **Victron Instant Readout —** SmartShunts, SmartSolar chargers, and similar supported devices can broadcast readings directly, so a Cerbo is not required for those values.
- **Ruuvi tags —** battery-powered temperature and humidity sensors suitable for locations such as a refrigerator or outdoor reading.

Turn Bluetooth on in Settings → Integrations, restart the Hub when prompted, then add discovered sensors from the Devices page.

::: note "Why a restart?"
Bluetooth is off by default. Turning it on or off changes how Hub memory is allocated, so the change takes effect after a restart.
:::

## Starlink

The Starlink card can show dish state and local statistics including connectivity, obstructions, ping success, and throughput. Enable Starlink in Settings → Integrations. If the card is also bound to a switched power circuit, its toggle can control dish power.

## GL.iNet travel router

With a supported GL.iNet router such as the Beryl or Slate family, the Travel Router card can show the active uplink, signal strength, and internet reachability. Tap the card to scan for and join campground or home Wi-Fi without opening the router administration page. Enter the router admin password once under Settings → Network.

## Custom MQTT devices

Advanced users can add devices that publish to an MQTT broker. Map MQTT topics to LaunchControl fields for card bindings; writable topics can accept commands. This provides a general integration path for equipment that LaunchControl does not support natively.
