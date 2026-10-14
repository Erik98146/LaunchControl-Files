# Set Up Your Hub

::: lead
Connect the Hub, open its setup page, and follow the seven-step setup guide. LaunchControl finds your equipment and creates dashboard cards as you add it. If a floor plan is available for your RV, you can load that configuration instead.
:::

![Figure 1 — LaunchControl setup at a glance.](images/ch02-figure-1-launchcontrol-setup-at-a-glance.png)

## Before you start

Have the correct Hub cable or adapter for your RV, one supported power source, and a phone, tablet, or computer with Wi-Fi. Have your RV router’s Wi-Fi password available if you plan to use it.

- **Required:** connect and power the Hub, join its Wi-Fi, confirm preferences, add your equipment, and check the dashboard.
- **Only if installed:** configure Victron, Shelly, Bluetooth, or other integrations. Your RV’s built-in equipment may be all you need.
- **Optional:** add displays and enable LaunchControl Remote. Local control needs no internet connection or Remote subscription.

Choose a hotspot password before pairing displays if you plan to use one. You can also set it later and pair the displays again.

## Connect the Hub

![LaunchControl Hub wiring diagram showing 12–24 VDC or USB-C power and RV-C CAN-H and CAN-L connections.](images/ch02-launchcontrol-hub-wiring-connections-power.png "LaunchControl Hub wiring connections. Power the Hub from either 12–24 VDC or USB-C—do not connect both power sources at the same time.")

1. **Connect RV-C.** Connect the Hub to the coach’s RV-C bus using the correct LaunchControl cable, adapter, or harness for your RV.
2. **Connect power.** The Hub can be powered from 12–24 V or USB-C. **Use only one power source at a time.**

::: warning "Connection types vary by RV"
RV-C connector styles and available connection points differ by manufacturer and coach. See the [LaunchControl FAQ at launchcontrol.tech](https://launchcontrol.tech/pages/support-faq) for supported RV-C connection types, adapter options, and installation-specific connection guidance. Use the same FAQ for the supported Hub power connection options.
:::

::: technical
Only the Hub connects to the RV-C bus. Touch 8 and Mini displays communicate with the Hub over the Hub’s private Wi-Fi network.
:::

## Join LaunchControl

1. **Join the Hub network.** On your phone or tablet, open Wi-Fi settings and join LaunchControl-Hub-XXXX. The XXXX identifies your Hub. A new Hub has no hotspot password.
2. **Open the setup page.** It should appear automatically, similar to a hotel Wi-Fi login. If it does not, open a browser and try [192.168.4.1](http://192.168.4.1) or [launchcontrol.local](http://launchcontrol.local).
3. **Follow the on-screen steps.** Agree to the product terms, then pick your **units** and confirm your **time zone** — both are filled in from your phone, and the phone’s clock sets the Hub’s time so schedules work from the first day. Then connect the Hub to your RV or home Wi-Fi, or choose **Set Up Without Wi-Fi**.
4. **Finish.** The last screen offers **Control your coach from anywhere**: set a Dashboard PIN and turn on LaunchControl Remote (see [Remote Access](#remote-access)). You can do this later from Settings → Integrations instead.
5. **Bookmark the dashboard.** When you are on the same RV/home network as the Hub, use [http://launchcontrol.local](http://launchcontrol.local).

::: note "Wi-Fi compatibility"
The Hub joins 2.4 GHz Wi-Fi networks. If your router uses one network name for both 2.4 GHz and 5 GHz, select that normal network. If it uses separate names, select the 2.4 GHz network.
:::

::: gallery "Initial setup"
![Initial setup](images/ch02-initial-setup-1.png)
![Initial setup](images/ch02-initial-setup-2.png)
![Initial setup](images/ch02-initial-setup-3.png)
:::

::: note "Direct access is always available"
The Hub’s own Wi-Fi remains available after setup. If you did not set up an RV router, join LaunchControl-Hub-XXXX directly. The Hub is at [launchcontrol.local](http://launchcontrol.local) or [192.168.4.1](http://192.168.4.1) on that private network.
:::

## The setup guide

The first time the dashboard opens it shows **Welcome to LaunchControl**, seven steps with a check mark on each one that is done. It stays until the dashboard has cards, and it is always available afterwards under **Settings → System → Setup guide**. Whenever a step sends you to another page, that page shows a **Setting up LaunchControl** strip with the step you are on and a **Back to setup** button, and comes back by itself when the step is done.

1. **Connect to your RV.** Done as soon as the Hub hears the RV’s control network. If it says the network was not detected, press **Fix connection**: check Hub power and the RV-C cable, and try swapping the two RV-C data wires. Reversed wires do not damage anything, they simply do not work. Never swap the RV-C and power wires. If all your equipment is Victron, Bluetooth or Shelly, this step becomes optional once that equipment is added.
2. **Preferences.** Shows your units, time zone and whether the Hub’s clock is set. When the phone or computer you are using is in a different zone, **Use this device’s time zone** takes its zone; **Change** opens the settings. The Hub keeps its clock automatically from then on: internet time when it has it, otherwise the coach network, a GPS, or the browser that is open.
3. **Find your RV equipment.** **Find equipment** opens the scan described in [Add or Change Equipment](#add-or-change-equipment): it adds the equipment, creates its cards and brings you back here. **Load a Floorplan** loads a ready-made setup instead, when one exists for your coach. Afterwards the step shows how many RV devices are configured, with **Review** and **Find more**.
4. **Additional equipment.** Answer once: press **Add other equipment** and tick the systems your RV has — Victron, Bluetooth devices, Shelly or network devices, advanced integrations — or press **None**. Each system you tick gets its own **Set up** button that opens the right settings, finds the equipment, creates its cards and returns here. The question is asked once; the Hub remembers the answer.
5. **Dashboard.** Completes by itself as cards are created. If something could not be added automatically, **Review** asks what each switched output is and creates the rest.
6. **Displays.** Optional. Power a Touch 8 or Mini near the Hub to pair it automatically; the step then shows it as connected.
7. **Remote access.** Shows whether LaunchControl Remote is on and linked. Optional.

When the required steps are done, including the Additional equipment answer, the guide reads **LaunchControl is ready** with **Open dashboard**. Displays and Remote never hold it up.

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

## Load a floor plan (if one exists)

A floor plan is a complete pre-built LaunchControl configuration for a specific coach. If one is available for your make and model, use it before adding devices or building dashboards by hand.

::: warning "Loading replaces your current configuration"
Loading a floor plan replaces the current coach configuration, including devices and dashboards. If you already customized the Hub, download a backup first under **Settings → System → Backup & restore**.
:::

A floor plan with Victron equipment still needs its Victron integration configured under **Settings → Integrations**, because passwords and integration IDs are unique.

1. **Go to Settings → Floor Plans.** The setup guide’s **Load a Floor Plan** button takes you there.
2. **Browse to your manufacturer and model.** Select the plan and review its description.
3. **Press Load.** The Hub restarts with the supported devices, panels, cards, and bindings configured for that coach.
4. **Review the dashboard.** Confirm that the panels and controls match your installation.

![Floor plan page.](images/ch02-floor-plan-page.png)



## No floor plan? Find your equipment

1. **Open Find equipment** from the setup guide.
2. **Identify and name equipment.** Operate one switch at a time in the RV, then choose its type in **What is it?**. Keep factory-useful names or use your own.
3. **Add the selected equipment.** **Add Equipment & Create Dashboard** creates devices and their cards. Selected switched outputs need a type or **No card** before you can continue.
4. **Check the result.** Confirm readings appear and each control operates the intended equipment. Arrange the cards whenever you are ready.

See [Add or Change Equipment](#add-or-change-equipment) for the complete scan, identification, and integration procedures; see [The Dashboard](#the-dashboard) to arrange cards and panels.

## Add displays and Remote

- **Touch 8 and Mini displays** connect to the Hub’s own Wi-Fi. A new display powered up near a single Hub joins it by itself; otherwise it shows a QR code to scan. See [The Touch 8 Display](#the-touch-8-display) and [The Mini Display](#the-mini-display).
- **LaunchControl Remote** puts the same dashboard on the internet, in any browser. Settings → Integrations → LaunchControl Remote → **Set up**, then link the Hub to your account with **Continue in browser** or by scanning the QR code. Every new Hub includes 90 days of LaunchControl Remote; see [Remote Access](#remote-access).

![LaunchControl interface screenshot](images/ch02-launchcontrol-interface-screenshot.png "")

**Setup is complete when** the guide says **LaunchControl is ready**, your expected readings appear, and you have checked that controls operate the intended equipment. Continue with [Controls](#controls) for everyday use.
