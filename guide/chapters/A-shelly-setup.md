# Shelly Setup

::: lead
Connect Shelly relays and inputs to the Hub, add them on the Devices page, and use them on the dashboard, the Touch 8 and in automations.
:::

## What you need

- A Shelly **Gen2, Gen3 or Gen4** device: the Plus and Pro lines, Gen3 and Gen4 relays, and input devices such as the Plus i4. First-generation Shelly devices (the original Shelly 1 and Shelly 2.5) are not discovered automatically yet.
- The Shelly joined to the same network as the Hub: the RV router's Wi-Fi, or the network the Hub is connected to.
- The Hub's **Broker address**, shown on the MQTT card once the built-in broker is on (the Hub's IP address on port 1883, for example `192.168.8.8:1883`).

::: note "Use the Hub's IP address"
Shelly devices do not look up names such as `launchcontrol.local`. Enter the Hub's IP address. If the Hub's address changes, the Shelly loses its connection, so give the Hub a fixed (reserved) address in the RV router if you can.
:::

## Turn on the Hub's broker

1. **Open the MQTT card.** Go to **Settings → Integrations → MQTT** and press **Set up** (or **Manage**).
2. **Choose the built-in broker.** Turn on MQTT and choose **Use Hub's built-in broker**.
3. **Leave sign-in blank.** Leave the username and password empty unless you want devices to sign in. If you set them, every Shelly needs the same username and password.
4. **Save.** Press **Save changes**. The card shows the **Broker address** and how many **clients** are connected.

::: warning "One broker at a time"
With the built-in broker selected, the Victron GX integration is unavailable, because it reads the Cerbo's own broker. If your coach has a Cerbo GX, you can keep **Connect to another broker** (the Cerbo) and point your Shelly devices at the Cerbo instead; discovery works through either broker.
:::

## Configure the Shelly

Open the Shelly's own web page by typing its IP address into a browser (the Shelly app shows the address in the device's settings). Then open **Settings → MQTT** and set:

| Setting | Value |
| --- | --- |
| Enable MQTT | On |
| Server | The Hub's broker address, for example `192.168.8.8:1883` |
| Client ID / MQTT prefix | Leave the default (it starts with `shelly`, for example `shelly1g4-acebe6f55504`) |
| Username / Password | Blank, unless you set them on the Hub |
| TLS / SSL | Off (no TLS) |
| RPC status notifications over MQTT | On |
| Generic status update over MQTT | On |
| Enable "MQTT Control" | On, where the device offers it |

Press **Save**. Some models restart to apply the change. The MQTT card on the Hub then counts one more client.

::: warning "Keep the default prefix"
LaunchControl recognises a Shelly by its default prefix, the device ID beginning with `shelly`. If you have changed the prefix, set it back to the default.
:::

## Add Shelly devices

1. **Open the scan.** On the Devices page choose **Add devices → Scan for Shelly devices**. The list shows the Hub's address to use, and fills in by itself.
2. **Wait for the device.** A Shelly appears within about a minute of connecting, with its model name, its relay state (On or Off) and its internal temperature.
3. **Add each channel.** Press **Add** next to each relay or input you want. A device with several relays, such as a Pro 4PM, lists each relay separately; each becomes its own LaunchControl device.
4. **Create cards.** Close the list. When it offers **Create cards**, accept it.

What each kind becomes:

| Shelly channel | LaunchControl device fields | Card created |
| --- | --- | --- |
| Relay (for example Shelly 1 Gen4) | **Relay** (on/off, switchable), **Temperature** (the Shelly's own board temperature), and **Switch input** when the relay has a wired input | **Generic Switch**: tap to switch the relay; the switch input shows under the icon as "Input on" or "Input off" |
| Input on an input-only device (Plus i4) | **Input** (on/off, read-only) | **Generic – Single**, showing On or Off |

Rename devices and cards as you like; the name has no effect on how they work. To show a relay as a fan, add a **Fan** card and bind its Switch to the Shelly's **Relay** field. Already-added channels show **Added** in the scan.

You can also select Shelly devices on the Devices page and press **Create cards for selected** later.

## Inputs: Switch and Button mode

Each Shelly input has a type, set in the input's settings in the Shelly app or on the Shelly's web page:

- **Switch** (a toggle or rocker switch that stays on or off): the input reports On or Off. LaunchControl shows it on a card and can use it as an automation trigger.
- **Button** (a momentary push button): the input reports presses only, not a state. It appears in the scan as **Button mode** and does not get a card. Use it to run a macro instead (below).

## Run a macro from a Shelly button

1. **Set the input to Button.** In the Shelly app, set the input type to **Button**, and make sure the Shelly is connected to the Hub's broker.
2. **Press it once.** A button appears in LaunchControl after its first press.
3. **Attach it to a macro.** Open **Settings → Automations**, open a macro (or create one), and under **Also run when a Shelly button is pressed** choose the input and **Single press**, **Double press**, **Triple press** or **Long press**.
4. **Save.** Press **Save**. The macro now runs within about a second of that press.

Each macro can have one button trigger. Different presses of the same button can run different macros, for example a single press for "Lights on" and a long press for "All off".

## Use Shelly devices in automations

- **As a trigger:** in an automation's **Sensor**, choose the Shelly device (marked **MQTT**) and its field: Relay, Switch input, Input or Temperature. On and off read as 1 and 0, so a rule with **Above 0.5** fires when the input turns on.
- **As an action:** use **Switch a card** with the Shelly's switch card and **On** or **Off**. The same works from Siri shortcuts and the Touch 8.

## After a restart

Shelly devices do not repeat their state on their own, so the Hub asks each one for it whenever it reconnects. After the Hub restarts, Shelly cards show their state again within about 35 seconds: that is how long a Shelly waits before reconnecting.

Shelly devices, their switch settings and their macro button triggers are included in **Download backup** and come back with a restore.

## Troubleshooting

| What you see | What to check |
| --- | --- |
| The Shelly never appears in the scan | On the Shelly's MQTT page it should say connected. Check the server is the Hub's IP address and port 1883, that the prefix is the default (`shelly…`), and that both notification options are on. The MQTT card on the Hub should count it as a client. |
| It appears, but the relay state never changes | **Generic status update over MQTT** is off on the Shelly. Turn it on and save. |
| The card does not switch the relay | Turn on **Enable "MQTT Control"** on the Shelly, where the model offers it. |
| A relay turns itself on whenever the Hub or the Shelly restarts | A command was sent to the Shelly as a *retained* MQTT message, usually from a test tool such as MQTT Explorer. Delete the retained `command/switch:0` topic in that tool. LaunchControl never sends retained commands. |
| A button is missing from the macro editor | Set the input to **Button** in the Shelly app and press it once. |
| Cards show nothing for about half a minute after a Hub restart | Normal: the Shelly reconnects after about 35 seconds and the Hub then asks it for its state. |

::: technical "MQTT topics LaunchControl uses"
LaunchControl subscribes to `<id>/online`, `<id>/status/switch:N`, `<id>/status/input:N` and `<id>/events/rpc`, where `<id>` is the device ID (the default prefix). It reads the relay from `output` and the board temperature from `temperature.tC` (or `tF`) in each `status/switch:N` object, an input's state from `state`, and button presses from `NotifyEvent` (`single_push`, `double_push`, `triple_push`, `long_push`). It switches a relay by publishing `on` or `off` to `<id>/command/switch:N`, never retained, and asks for a fresh status by publishing `status_update`.

In the Custom MQTT device editor these settings appear as a suffix after `#` on a topic: `…/status/switch:0#output` reads the `output` key, and a command topic ending `#lower` sends lowercase `on` and `off`. You can use the same suffixes for other JSON devices.
:::
