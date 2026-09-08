# Install & Quick Start

::: lead
A new installation is easiest when you follow the same sequence every time: connect the Hub, connect the network, verify RV-C data, then configure the coach. If a pre-built floor plan is available, most of the work is already done for you.
:::

![Figure 1 — LaunchControl setup at a glance.](images/ch02-figure-1-launchcontrol-setup-at-a-glance.png)

## Install the Hub

![LaunchControl Hub wiring diagram showing 12–24 VDC or USB-C power and RV-C CAN-H and CAN-L connections.](images/ch02-launchcontrol-hub-wiring-connections-power.png "LaunchControl Hub wiring connections. Power the Hub from either 12–24 VDC or USB-C—do not connect both power sources at the same time.")

1. **Connect RV-C.** Connect the Hub to the coach’s RV-C bus using the correct LaunchControl cable, adapter, or harness for your RV.
2. **Connect power.** Connect the Hub using the supported power connection for your installation. The hub can be powered from 12-24 V or USB-C. **DO NOT CONNECT BOTH SIMULTANEOUSLY.**

::: warning "Connection types vary by RV"
RV-C connector styles and available connection points differ by manufacturer and coach. See the [LaunchControl FAQ at launchcontrol.tech](https://launchcontrol.tech/pages/support-faq) for supported RV-C connection types, adapter options, and installation-specific connection guidance. Use the same FAQ for the supported Hub power connection options.
:::

::: technical
Only the Hub connects to the RV-C bus. Touch 8 and Mini displays communicate with the Hub over the Hub’s private Wi-Fi network.
:::

## Connect to the Hub and set up Wi-Fi

1. **Join the Hub network.** On your phone or tablet, open Wi-Fi settings and join LaunchControl-Hub-XXXX. The XXXX identifies your Hub. A new Hub has no hotspot password.
2. **Open the setup page.** It should appear automatically, similar to a hotel Wi-Fi login. If it does not, open a browser and try [192.168.4.1](http://192.168.4.1) or [launchcontrol.local](http://launchcontrol.local)
3. **Follow the on-screen setup steps.** If you want to access through your RV or home Wi-Fi, add that network under Settings > Network.
4. **Bookmark the dashboard.** When you are on the same RV/home network as the Hub, use [http://launchcontrol.local](http://launchcontrol.local).

::: note "Wi-Fi compatibility"
The Hub joins 2.4 GHz Wi-Fi networks. If your router uses one network name for both 2.4 GHz and 5 GHz, select that normal network. If it uses separate names, select the 2.4 GHz network.
:::

::: gallery "Initial setup"
![Initial setup](images/ch02-initial-setup-1.png)
![Initial setup](images/ch02-initial-setup-2.png)
![Initial setup](images/ch02-initial-setup-3.png)
:::

::: note "Direct access is always available"
The Hub’s own Wi-Fi remains available after setup. If you didn’t setup with an RV router, join LaunchControl-Hub-XXXX directly. The Hub is at [launchcontrol.local](http://launchcontrol.local) or [192.168.4.1](http://192.168.4.1) on that private network.
:::

## Choose security settings

The first time you open the dashboard, LaunchControl offers two optional security layers: a Dashboard PIN and a password for the Hub’s own hotspot. You can set either one now or configure them later under Settings → Network.

- **Dashboard PIN —** protects the web dashboard when accessed from networks you have not marked as trusted.
- **Hotspot password —** protects the Hub’s private Wi-Fi network with WPA2.

::: note "If displays are already paired"
Changing the Hub hotspot password disconnects Touch 8 and Mini displays from that network. They must be paired again with the new credentials. If you are setting up a complete Hub + display system, it is simplest to choose the hotspot password before pairing the displays.
:::

::: gallery "Security settings"
![Security settings](images/ch02-security-settings-1.png)
![Security settings](images/ch02-security-settings-2.png)
:::

## Verify RV-C data before continuing

Before loading or building a dashboard, confirm that the Hub can actually see the coach devices.

1. **Open Settings → Status.**
2. **Find the RV-C row.** It should show that the RV-C bus is connected (green) and that data is being received (>0 frames/sec).
3. **If RV-C is not active, stop here.** Check Hub power and the physical RV-C connection before adding devices or cards. Use the FAQ for coach-specific connection guidance. It doesn’t hurt anything if the RV-C L & H wires are reversed, it just won’t work, so you can try swapping those. Just don’t swap RV-C and power wires!

## Load a floor plan (recommended)

A floor plan is a complete pre-built LaunchControl configuration for a specific coach. If one is available for your make and model, use it before spending time adding devices or building dashboards manually.

1. **Go to Settings → Floor Plans.**
2. **Browse to your manufacturer and model.** Select the plan and review its description.
3. **Press Load.** The Hub restarts with the supported devices, panels, cards, and bindings configured for that coach.
4. **Review the dashboard.** Confirm that the panels and controls match your installation.

![Floor plan page.](images/ch02-floor-plan-page.png)

::: technical "Technical detail"
A floor plan includes devices and dashboards. Because passwords and integration ID’s are unique, floor plans with Victron equipment still require setting up the Victron integration in Settings > Integrations. **Loading a floor plan replaces the current coach configuration.**
:::

## No floor plan available? Build the coach manually

If your coach does not have a published floor plan, the setup path is still straightforward: discover the equipment first, then create dashboard cards and bind those cards to the fields you want to display or control.

1. **Scan and add RV-C devices.** Open Devices, choose Add a Device → Add RV-C Device, scan the bus, then name and add the equipment you recognize. See section 3 for details.
2. **Create or choose a dashboard panel.** Enter dashboard edit mode. Add a panel if you need one, or work in an existing panel. See section 4 for details.
3. **Add a card.** Choose + Add Card, select the card type, name it, and choose its size/layout.
4. **Bind the card.** Choose the device and field or fields that provide the card’s live data and controls. Structured cards such as Thermostat expose named slots for items such as mode, setpoint, and fan.
5. **Arrange and repeat.** Move cards into the layout you want, then repeat for the rest of the coach.
6. **Create a backup.** When the dashboard is working correctly, go to Settings → System → Backup and save a copy.

![LaunchControl interface screenshot](images/ch02-launchcontrol-interface-screenshot.png "")

The system is ready for use. For customizations, continue with Chapter 3.
