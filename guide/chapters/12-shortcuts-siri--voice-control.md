# Voice Control, Shortcuts, Siri and Other Controllers (API)

::: lead
Say "Hey Siri, kitchen lights on" and the lights come on. LaunchControl works with the Shortcuts app that is already on every iPhone, iPad, Mac and Apple Watch — no extra hub, no HomeKit. Android phones and other automation tools can use the same links.
:::

## How it works

Every control on your dashboard already has a name — the card name you gave it. The Hub accepts a simple web address that uses those names, such as *turn Kitchen Pendants on* or *set Bedroom to 72*. 

For Siri, A Shortcut opens that address; Siri runs the Shortcut when you say its name. The Hub works out which device, which command and which setting, and answers with a short sentence that Siri can show or speak.

What you can address by name:

- **Switches and lights —** Light, Switch, Water Pump, Starlink, Inverter, Tank Heat and Linked Switch cards: on, off, toggle, status. Lights also take a brightness.
- **Thermostats —** a temperature, a mode (heat, cool, auto, fan, off), or status.
- **Lighting zones and scenes —** each zone of a Lighting card (on, off) and every saved scene (run).
- **Door locks —** lock, unlock, status.
- **Shore power —** a current limit.
- **Macros and automations —** run a macro; enable or disable an automation.
- **Readings —** ask for the status of any card that shows a value: battery, tanks, solar, temperatures.

Awnings, shades and slides are deliberately excluded. They move only while a button is held, and a voice command has no way to stop them.

## Set it up

1. **Open the settings.** On the dashboard, go to **Settings → Integrations → Shortcuts & API** and press **Set up shortcuts**. The card has two tabs: **Apple Shortcuts & Siri**, and **API & custom integrations** for other apps.
2. **Choose the connection method.** **RV network** makes links that work while the phone is on a network that can reach the Hub; **LaunchControl Remote** makes links that work from anywhere the phone has internet (it needs Remote linked and active, see [Remote Access](#remote-access)). A VPN address such as Tailscale can be used as a **Custom address** once **Expert mode** is on (at the bottom of the LaunchControl Remote card). The choice is remembered on this browser only.
3. **Try a command.** Type *turn on the kitchen lights* (using one of your own names) in **Try a command** and press **Test command**. The Hub's answer appears below it — exactly what Siri will say. Testing really sends the command to your RV; copying a link never does.

::: note "The API key"
Links contain an API access key that lets a Shortcut run commands without entering the Dashboard PIN, and it only works for this feature — it cannot change settings, read a backup or join a network. It is kept masked under **API access key**: **Show**, **Copy key**, and **Replace key**. If a phone with your shortcuts is lost, press **Replace key**; every shortcut then needs its link updated. The key is not included in configuration backups.
:::

## One shortcut for everything

Build this one first. It takes whatever you say and lets the Hub work it out, so you never build a shortcut per device unless you want to.

1. **Copy the voice link.** On the **Apple Shortcuts & Siri** tab, choose **Control by voice** and press **Copy shortcut link**. **View setup guide** shows these steps on the page.
2. **Create a Shortcut.** Open the Shortcuts app, tap **+**, and add the action **Ask for Input**. Choose **Text** and set the prompt to something like *What should LaunchControl do?*
3. **Add the web request.** Add the action **Get Contents of URL** and paste the link. Expand its options and leave **Method** set to **GET**. Under **Headers**, add the key `X-Say`; for its value choose **Select Variable** and pick **Ask for Input** (usually shown as *Provided Input*) near the top. Do not pick *Shortcut Input*.
4. **Hear the answer.** Add the action **Speak Text** with **Contents of URL** from the previous step. To see the answer instead, use **Show Result**.
5. **Name it.** Tap the name at the top and call it **Coach** (or anything you like). That name is the Siri phrase.

Now say "Hey Siri, Coach". Siri asks what you would like; answer in plain words:

| Say | What happens |
| --- | --- |
| *kitchen lights on* / *turn off the kitchen lights* | Switches the card named Kitchen Lights (or the closest match, such as Kitchen Pendants) |
| *kitchen to 40 percent* | Dims a light to 40 % |
| *bedroom to 72* | Sets the active setpoint of the Bedroom thermostat to 72° (in the Hub's display units) |
| *bedroom heat* / *bedroom cool 74* | Changes the mode, optionally with a setpoint |
| *inside lights off* | A lighting zone, by its zone name |
| *movie night* | Recalls the lighting scene with that name |
| *run away* / *run return* | Runs a macro |
| *lock the front door* | Locks a Door Lock card |
| *is the water pump on* / *what is the fresh tank* / *battery status* | Reads a value back |
| *disable low battery guard* | Turns an automation off |

Filler words are ignored, so *please turn on the kitchen lights* and *kitchen lights on* are the same request. If two names match equally, the Hub answers *Which one: …?* — say the full name next time, or rename one card.

## One-tap shortcuts

A phrase of its own is faster when you say it often: "Hey Siri, kitchen lights on" with no follow-up question. Each needs its own small Shortcut.

1. **Pick the action.** On the **Apple Shortcuts & Siri** tab, choose **Create a specific shortcut**. Find the **Device**, choose the **Action**, and enter a value where the action takes one (50 %, 72°, 30 A). The command is summarized below.
2. **Copy it.** Press **Copy shortcut link**. This makes the link only; it does not operate the device. **Test command** tries it for real.
3. **Create the Shortcut.** In Shortcuts, tap **+**, add **Get Contents of URL**, and paste the link. Add **Show Result** if you want to see the Hub's answer.
4. **Name it with the phrase.** The Shortcut's name is what you say: *Kitchen Lights On*.

Shortcuts can also be put on the Home Screen, in a widget, on the Action Button, in the Apple Watch Shortcuts app, or run from a Shortcuts automation — for example *when I arrive at the campground, run Return*.

::: note "Apple Watch"
Shortcuts synced to the watch appear in its Shortcuts app and respond to "Hey Siri" on the watch. The watch needs a path to the Hub: your phone nearby on the coach's Wi‑Fi, or the LaunchControl Remote address.
:::

## Away from the coach

A link works from anywhere the phone can reach the Hub. On the coach's Wi‑Fi that is the local address. From the road, use LaunchControl Remote: under **Connection method** pick **LaunchControl Remote** before copying, and the links — and Siri — work wherever the phone has internet; the API key is accepted there too. A VPN such as Tailscale on the coach router works the same way with its address. The Hub does not need to be exposed to the internet — never forward its port.

## Other phones and apps

Any tool that can open a web address can use the same links: Android's Shortcut Maker or Tasker, a browser bookmark, a Stream Deck, or a Home Assistant *rest_command*. The **API & custom integrations** tab builds request URLs for them — by device and action, or as a plain‑language command — with a text or JSON response, and **API documentation** lists every parameter. The link is a plain GET request; the answer is one line of text, or JSON if you leave `fmt=text` off.

::: warning "Names change the links"
A link names the card. If you rename a card, a zone or a scene, update the shortcuts that use the old name — the Hub answers *I don't know a device called …* until you do.
:::

::: technical "The control address"
`GET /api/control` on the Hub, authenticated by a session (the Dashboard PIN or a trusted network) or by the API key as `?key=<key>` or an `Authorization: Bearer <key>` header. The key is accepted by this address only.

| Parameter | Meaning |
| --- | --- |
| `say=<sentence>` | Free text; the Hub extracts the device, the action and any number. Also accepted as an `X-Say` request header. |
| `device=<name>` | A card, zone, scene, macro or automation name (`#<id>` for a card id). |
| `action=` | `on` `off` `toggle` `lock` `unlock` `run` `status` |
| `level=` `temp=` `limit=` `mode=` | A brightness %, a setpoint in the Hub's display units, a shore limit in amps, or `heat` `cool` `auto` `fan` `off` |
| `fmt=text` | Reply as one spoken line with HTTP 200 regardless of outcome. Without it the reply is JSON (`ok`, `device`, `action`, `say`, `error`, `candidates`) with 400/404/409/502 on failure. |
| *(no device)* | Lists every name and what each accepts, as JSON. |
| `op=newkey` | Rotates the key; PIN or trusted-network session required. |

A successful reply means the Hub accepted and sent the command, not that the device obeyed; the dashboard and displays show the real state as the device reports it.
:::
