# Set Up Your Hub

::: lead
Connect the Hub, join its Wi-Fi, and follow the seven-step setup guide. LaunchControl finds your equipment and creates dashboard cards as you add it. If a floor plan is available for your RV, you can load that ready-made configuration instead.
:::

![Figure 1 — LaunchControl setup at a glance.](images/ch02-figure-1-launchcontrol-setup-at-a-glance.png)

## Before you start

Have the correct Hub cable or adapter for your RV, one supported power source, and a phone, tablet, or computer with Wi-Fi. Have your RV router’s Wi-Fi password available if you plan to use it.

- **Required:** connect and power the Hub, join the Hub hotspot, confirm preferences, add your equipment, and check the dashboard.
- **Only if installed:** configure Victron, Shelly, Bluetooth, or other integrations. Your RV’s built-in equipment may be all you need.
- **Optional:** add displays and turn on LaunchControl Remote. Local control needs no internet connection and no Remote subscription.

If you plan to put a password on the Hub hotspot, choose it before pairing displays. You can also set it later and pair the displays again.

## Connect the Hub

![LaunchControl Hub wiring diagram showing 12–24 VDC or USB-C power and RV-C CAN-H and CAN-L connections.](images/ch02-launchcontrol-hub-wiring-connections-power.png "LaunchControl Hub wiring connections. Power the Hub from either 12–24 VDC or USB-C—do not connect both power sources at the same time.")

1. **Connect RV-C.** Connect the Hub to the RV’s RV-C network using the correct LaunchControl cable, adapter, or harness for your RV.
2. **Connect power.** The Hub can be powered from 12–24 V or USB-C. **Use only one power source at a time.**

::: warning "Connection types vary by RV"
RV-C connector styles and available connection points differ by manufacturer and coach. See the [LaunchControl FAQ at launchcontrol.tech](https://launchcontrol.tech/pages/support-faq) for supported RV-C connection types, adapter options, and installation-specific connection guidance. Use the same FAQ for the supported Hub power connection options.
:::

::: technical
Only the Hub connects to the RV-C network. Touch 8 and Mini displays communicate with the Hub over the Hub hotspot.
:::

## Join the Hub hotspot

1. **Join the Hub hotspot.** On your phone or tablet, open Wi-Fi settings and join LaunchControl-Hub-XXXX. The XXXX identifies your Hub. A new Hub has no hotspot password.
2. **Open the setup wizard.** It should appear automatically, similar to a hotel Wi-Fi login. If it does not, open a browser and go to [192.168.4.1](http://192.168.4.1).
3. **Follow the on-screen steps.** Agree to the product terms, then pick your **units** and confirm your **time zone** — both are filled in from your phone, and the phone’s clock sets the Hub’s time so schedules work from the first day. Then connect the Hub to your RV or home Wi-Fi, or choose **Set Up Without Wi-Fi**.
4. **Finish.** The last screen offers **Control your coach from anywhere**: set a Dashboard PIN and turn on LaunchControl Remote (see [Remote Access](#remote-access)). You can do this later from Settings → Integrations instead.
5. **Bookmark the dashboard.** When you are on the same RV or home network as the Hub, use [http://launchcontrol.local](http://launchcontrol.local).

::: note "Your phone may say the network has no internet"
The Hub hotspot is a local network with no internet of its own. Phones often warn about this, and some quietly switch back to cellular data or another Wi-Fi network. If a page stops loading, check that the phone is still joined to LaunchControl-Hub-XXXX, and choose to stay connected if the phone asks. Once the Hub has joined your RV router, use the router’s Wi-Fi instead and the warning goes away.
:::

::: note "Wi-Fi compatibility"
The Hub joins 2.4 GHz Wi-Fi networks. If your router uses one network name for both 2.4 GHz and 5 GHz, select that normal network. If it uses separate names, select the 2.4 GHz network.
:::

::: gallery "Initial setup"
![Initial setup](images/ch02-initial-setup-1.png)
![Initial setup](images/ch02-initial-setup-2.png)
![Initial setup](images/ch02-initial-setup-3.png)
:::

::: note "The Hub hotspot is always available"
The Hub hotspot stays on after setup. If you did not set up an RV router, or the router is off, join LaunchControl-Hub-XXXX and open [192.168.4.1](http://192.168.4.1) or [launchcontrol.local](http://launchcontrol.local).
:::

## Follow the setup guide

The first time the dashboard opens it shows **Welcome to LaunchControl**: seven steps, with a check mark on each one that is done. It stays until the dashboard has cards, and it is always available afterwards under **Settings → System → Setup guide**. Whenever a step sends you to another page, that page shows a **Setting up LaunchControl** strip with the step you are on and a **Back to setup** button, and returns by itself when the step is done.

1. **Connect to your RV.** Done as soon as the Hub hears the RV’s control network. If it says the network was not detected, press **Fix connection**: check Hub power and the RV-C cable, and try swapping the two RV-C data wires. Reversed data wires do not damage anything, they simply do not work. Never swap the RV-C and power wires. If all your equipment is Victron, Bluetooth, or Shelly, this step becomes optional once that equipment is added.
2. **Preferences.** Shows your units, time zone, and whether the Hub’s clock is set. When the phone or computer you are using is in a different zone, **Use this device’s time zone** takes its zone; **Change** opens the settings. The Hub keeps its clock automatically from then on: internet time when it has it, otherwise the RV network, a GPS, or the browser that is open.
3. **Find your RV equipment.** Choose one of the two paths described in the next section: **Load a Floorplan** when a ready-made setup exists for your coach, or **Find equipment** to scan for it. Afterwards the step shows how many RV devices are configured, with **Review** and **Find more**.
4. **Additional equipment.** Answer once: press **Add other equipment** and tick the systems your RV has — Victron, Bluetooth devices, Shelly or network devices, advanced integrations — or press **None**. Each system you tick gets its own **Set up** button that opens the right settings, finds the equipment, creates its cards, and returns here. The Hub remembers the answer.
5. **Dashboard.** Completes by itself as cards are created. If something could not be added automatically, **Review** asks what each switched output is and creates the rest.
6. **Displays.** Optional. Power a Touch 8 or Mini near the Hub to pair it automatically; the step then shows it as connected.
7. **Remote access.** Optional. Shows whether LaunchControl Remote is on and linked.

When the required steps are done, including the Additional equipment answer, the guide reads **LaunchControl is ready** with **Open dashboard**. Displays and Remote never hold it up.

## Floor plan or scan: choose one

Step 3 of the setup guide offers two ways to get your RV’s equipment onto the dashboard.

| If… | Use | What happens |
| --- | --- | --- |
| A floor plan exists for your make and model | **Load a Floorplan** | The Hub restarts with devices, panels, and cards already configured for that coach. |
| No floor plan exists, or you prefer to build your own | **Find equipment** | The Hub lists what it hears; you name each item and LaunchControl creates its card. |

### Load a floor plan

A floor plan is a complete pre-built LaunchControl configuration for a specific coach.

::: warning "Loading replaces your current configuration"
Loading a floor plan replaces the current configuration, including devices and panels. If you already customized the Hub, download a backup first under **Settings → System → Backup & restore**.
:::

1. **Open Settings → Floor Plans.** The setup guide’s **Load a Floorplan** button takes you there.
2. **Browse to your manufacturer and model.** Select the plan and review its description.
3. **Press Load.** The Hub restarts with the supported devices, panels, cards, and bindings configured for that coach.
4. **Review the dashboard.** Confirm that the panels and controls match your installation.

A floor plan with Victron equipment still needs its Victron integration configured under **Settings → Integrations**, because passwords and integration IDs are unique to each installation.

![Floor plan page.](images/ch02-floor-plan-page.png)

### Find your equipment

1. **Press Find equipment** in the setup guide.
2. **Identify and name equipment.** Operate one switch at a time in the RV, then choose its type in **What is it?**. Keep factory names that are useful, or type your own.
3. **Press Add Equipment & Create Dashboard.** This creates the devices and their cards. Every selected switched output needs a type or **No card** before you can continue.
4. **Check the result.** Confirm that readings appear and that each control operates the intended equipment.

[Add or Change Equipment](#add-or-change-equipment) has the complete scan, identification, and integration procedures. [The Dashboard](#the-dashboard) covers arranging cards and panels.

## Add displays and Remote

Both are optional and can be added at any time.

- **Touch 8 and Mini displays** connect to the Hub hotspot. A new display powered up near a single Hub joins it by itself; otherwise it shows a QR code to scan. See [The Touch 8 Display](#the-touch-8-display) and [The Mini Display](#the-mini-display).
- **LaunchControl Remote** puts the same dashboard on the internet, in any browser. Open **Settings → Integrations → LaunchControl Remote → Set up**, then link the Hub to your account with **Continue in browser** or by scanning the QR code. Every new Hub includes 90 days of LaunchControl Remote; see [Remote Access](#remote-access).

![LaunchControl interface screenshot](images/ch02-launchcontrol-interface-screenshot.png "")

## Protect the Hub

A new Hub is open so that first-time setup cannot lock you out. Until you decide, the dashboard shows **Secure this hub** with two choices: **Set up now** opens the settings, and **Leave it open** dismisses the reminder. Two optional protections are set under **Settings → Network**:

- **Dashboard PIN —** asked for when the dashboard is opened from a network you have not marked as trusted, and always through LaunchControl Remote. The setup wizard’s last screen also offers it.
- **Hotspot password —** protects the Hub hotspot with WPA2. Devices that join a password-protected Hub hotspot are trusted and are not asked for the PIN.

::: note "If displays are already paired"
Changing the hotspot password disconnects Touch 8 and Mini displays. Pair them again with the new password. If you are setting up a complete Hub and display system, it is simplest to choose the hotspot password before pairing the displays.
:::

::: gallery "Security settings"
![Security settings](images/ch02-security-settings-1.png)
![Security settings](images/ch02-security-settings-2.png)
:::

See [Security](#security) for trusted networks, the API key, and what to do if you are locked out.

## Setup is complete when…

The setup guide says **LaunchControl is ready**, your expected readings appear, and you have checked that each control operates the intended equipment. Continue with [Controls](#controls) for everyday use.
