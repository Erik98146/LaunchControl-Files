# Shelly Setup

::: lead
Connect Shelly relays, inputs and colour lights to the Hub, add them on the Devices page, and use them on the dashboard, the Touch 8, in Lighting scenes and in automations.
:::

## What you need

- A Shelly **Gen2, Gen3 or Gen4** device: the Plus and Pro lines, Gen3 and Gen4 relays, input devices such as the Plus i4, and the **Plus RGBW PM** colour LED controller. First-generation Shelly devices (the original Shelly 1 and Shelly 2.5) are not discovered automatically yet.
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
| Colour light (Plus RGBW PM) | **State**, **Brightness**, **White**, **Color**, **Power** and **Temperature** | **Color Light** (see [Colour lights](#colour-lights-plus-rgbw-pm)) |

Rename devices and cards as you like; the name has no effect on how they work. To show a relay as a fan, add a **Fan** card and bind its Switch to the Shelly's **Relay** field. Already-added channels show **Added** in the scan.

You can also select Shelly devices on the Devices page and press **Create cards for selected** later.

## Colour lights (Plus RGBW PM)

The Plus RGBW PM drives an RGBW LED strip: red, green and blue LEDs that mix into a colour, plus a separate white LED.

### Set up the Shelly

1. **Choose the RGBW profile.** In the Shelly app or on the Shelly's web page, set the device profile to **RGBW**. (The **RGB** and **Light** profiles are not supported yet.)
2. **Set the power-on state.** Under the light's settings, set **Initial state** (power-on default) to **Restore last**, so the light comes back as it was after the coach's power has been off.
3. **Point it at the Hub.** Configure MQTT exactly as in [Configure the Shelly](#configure-the-shelly). **Generic status update over MQTT** must be on: it is how the card follows the light.
4. **Add it.** In **Add devices → Scan for Shelly devices** the light appears as **Color light**. Press **Add**, close the list and accept **Create cards**.

### Use the Color Light card

- **Tap** the card to switch the light on or off. Switching off keeps the colour and levels, so the next tap brings them back.
- **Press and hold** the card for the colour controls:
    - **Colour wheel.** Drag around the wheel for the colour, toward the centre for paler colours.
    - **Colour chips.** One tap for red, orange, amber, yellow, green, cyan, blue, purple or pink. A chip also turns the white LEDs off, so you see the pure colour. **W** turns the coloured LEDs off and leaves only white.
    - **Color** sets the brightness of the coloured LEDs. **White** sets the white LEDs, separately. **Master** dims or brightens both together and keeps the balance between them.
- The bulb on the card shows the light's current colour.

When **Color** goes to 0 and comes back up, the light returns to its last colour. The Hub remembers that colour, so it is the same on every screen, survives a restart and is included in backups.

### Lighting scenes and zones

Colour lights appear in a Lighting card's settings (marked **(Shelly)**) and can be added to Zone 1, Zone 2 and the scenes:

- **Zones** switch a colour light on and off. It keeps its own colour and levels.
- **Scenes** remember each colour light's on/off state, colour, colour brightness and white level, and bring all of them back in one step. Set the lights the way you want them, then press and hold the scene to save it.

The Color Light card also works with the Mini's on/off buttons, Siri shortcuts and automations (**Switch a card**). The Touch 8 shows the light in Lighting zones and scenes; a Color Light face for the Touch 8 is coming in a later update.

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

Shelly devices, their switch settings, their macro button triggers, colour lights' remembered colours and the colours saved in Lighting scenes are included in **Download backup** and come back with a restore.

## Troubleshooting

| What you see | What to check |
| --- | --- |
| The Shelly never appears in the scan | On the Shelly's MQTT page it should say connected. Check the server is the Hub's IP address and port 1883, that the prefix is the default (`shelly…`), and that both notification options are on. The MQTT card on the Hub should count it as a client. |
| It appears, but the relay state never changes | **Generic status update over MQTT** is off on the Shelly. Turn it on and save. |
| The card does not switch the relay | Turn on **Enable "MQTT Control"** on the Shelly, where the model offers it. |
| A relay turns itself on whenever the Hub or the Shelly restarts | A command was sent to the Shelly as a *retained* MQTT message, usually from a test tool such as MQTT Explorer. Delete the retained `command/switch:0` topic in that tool. LaunchControl never sends retained commands. |
| A button is missing from the macro editor | Set the input to **Button** in the Shelly app and press it once. |
| Cards show nothing for about half a minute after a Hub restart | Normal: the Shelly reconnects after about 35 seconds and the Hub then asks it for its state. |
| A colour light is missing from the scan | Set the Shelly's profile to **RGBW**. The RGB and Light profiles are not supported yet. |
| A Color Light change says "did not take effect" | **Generic status update over MQTT** is off on the Shelly, so the card never hears the new colour. Turn it on and save. |
| A colour light comes back off after a power cut | Set its **Initial state** to **Restore last** in the Shelly app. |

::: technical "MQTT topics LaunchControl uses"
LaunchControl subscribes to `<id>/online`, `<id>/status/switch:N`, `<id>/status/input:N`, `<id>/status/rgbw:0` and `<id>/events/rpc`, where `<id>` is the device ID (the default prefix). It reads the relay from `output` and the board temperature from `temperature.tC` (or `tF`) in each `status/switch:N` object, an input's state from `state`, and button presses from `NotifyEvent` (`single_push`, `double_push`, `triple_push`, `long_push`). It switches a relay by publishing `on` or `off` to `<id>/command/switch:N`, never retained, and asks for a fresh status by publishing `status_update`.

In the Custom MQTT device editor these settings appear as a suffix after `#` on a topic: `…/status/switch:0#output` reads the `output` key, and a command topic ending `#lower` sends lowercase `on` and `off`. You can use the same suffixes for other JSON devices.

A colour light reads `output`, `brightness` (the coloured LEDs, 1–100 %), `white` (0–255), `rgb` (shown as `r,g,b`), `apower` and the temperature from `status/rgbw:0`. Its commands go to `<id>/rpc` as JSON-RPC `RGBW.Set` and `RGBW.Toggle`, never retained; on the command topic this is the `#rgbw:0` suffix. Setting the colour brightness to 0 sends the colour as black, because the Shelly's lowest brightness is 1 %.
:::
