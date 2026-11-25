<!-- part: Maintain your system -->
# Security

::: lead
A new Hub is intentionally easy to access so first-time setup cannot lock you out. After setup, you can add a Dashboard PIN, a hotspot password, or both.
:::

| Protection | What it protects |
| --- | --- |
| **Dashboard PIN** | Dashboard access from untrusted networks, and always through Remote |
| **Hotspot password** | Joining the Hub hotspot |
| **API access key** | Named controls used by Shortcuts, Siri, the AI assistant, and other integrations |

These serve different purposes. Changing the hotspot password means pairing displays again; replacing the API access key means updating shortcuts.

## Recommended setup

1. **Set a Dashboard PIN.** Use a PIN you do not share publicly.
2. **Set a hotspot password** before pairing displays. Rejoin the protected Wi-Fi.
3. **Trust only your own private RV or home network.** Leave shared networks untrusted.
4. **Keep keys private.** Only enable Remote, AI and MQTT access when you need them; review their sharing and access settings.

You’re done when you can reconnect using your credentials and your intended devices can still open the dashboard.

## Dashboard PIN

Set it under **Settings → Network → Dashboard PIN**: type 4 to 32 digits and press **Save PIN**. **Remove PIN** takes it off again. A browser is asked for the PIN once and then remembered.

The PIN controls who can open the dashboard. It does not encrypt the connection between your browser and the Hub.

## Trusted networks

The PIN is asked for only on networks the Hub does not trust, so your own network can skip it while a campground network cannot.

1. **Open Settings → Network → Saved Wi-Fi Networks.**
2. **Turn on Trusted** for your own RV or home network.
3. **Leave it off** for campground, marina, or any other shared Wi-Fi.

Two rules do not change: devices on a password-protected Hub hotspot are always trusted, and LaunchControl Remote always asks for the PIN.

## Hotspot password

Under **Settings → Network → Hub Hotspot**, press **Set Password** and enter 8 to 63 characters. Saving a new password restarts the hotspot and disconnects anything using it.

::: note "Displays use the hotspot"
Touch 8 and Mini displays connect to the Hub hotspot. If you change its password, pair the displays again with the new one.
:::

## API access key

Shortcuts, Siri, and other integrations (see [Siri & Shortcuts](#siri-shortcuts)) use an **API access key** instead of the Dashboard PIN. It is kept masked under **Settings → Integrations → Shortcuts & API → API access key** and works for the control address only: a key that leaks can operate named controls, but cannot change settings, read a backup, or join a network. Press **Replace key** to replace it; every shortcut then needs its link updated. The key is not included in configuration backups.

## Remote access

LaunchControl Remote (see [Remote Access](#remote-access)) makes the dashboard reachable from the internet through LaunchControl's service, never by opening a port on the coach. It cannot be turned on without a Dashboard PIN, and every remote browser is asked for that PIN — your account proves who you are to LaunchControl, the PIN proves it to the Hub. The Hub treats a connection arriving through Remote as untrusted no matter which network it is on. Share a hub only with people you would hand the PIN to; the owner can remove a shared user at any time, and **Unlink** cuts the hub off from the account entirely.

An AI assistant connected through Remote uses a secret link instead of the PIN. Treat that link like a key; see [AI Assistant](#ai-assistant).

## Remote support

LaunchControl staff cannot open your hub through Remote on their own. You open a 24-hour support window on the hub's page and give them its PIN; they must enter it to get in, and the hub shows a yellow border while the window is open and a red one while someone is connected (see [Remote Access](#remote-access)). Turn it off at any time; it closes by itself after 24 hours.

## Locked out?

If you forget the PIN or the hotspot password, switch the Hub’s power off and on several times in a row. No cable and no support call are needed.

For each cycle, **turn the Hub on, wait about 5 seconds, and turn it off again**. The wait matters in both directions: the Hub needs a few seconds to record the power-up, and a cycle only counts if power is removed within 30 seconds. If the Hub stays on longer than that, the count starts over.

| Turn the Hub on… | What happens |
| --- | --- |
| **3 times in a row** | The Hub hotspot opens with no password for 2 minutes, so you can join it. The Dashboard PIN still applies. |
| **5 times in a row** | The Dashboard PIN and the hotspot password are both cleared. Leave the Hub on after the fifth power-up and set new ones. |

Only switching the power counts. Restarting the Hub from Settings, a software update, or a normal power interruption does not add up to a reset.

::: technical
The Dashboard PIN is stored salted and hashed. Neither the PIN nor the hotspot password is included in configuration backups or in a support file.
:::
