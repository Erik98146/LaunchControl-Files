# Security

::: lead
A new Hub is intentionally easy to access so first-time setup cannot lock you out. After commissioning, you can add a Dashboard PIN, a hotspot password, or both.
:::

## Dashboard PIN

The Dashboard PIN is 4–32 digits. LaunchControl requests it only on networks the Hub does not trust. Mark your own RV/home network as trusted to avoid repeated prompts while still protecting access from an untrusted campground network.

## Hotspot password

The Hub hotspot can use a WPA2 password of 8–63 characters. Saving a new password restarts the hotspot and disconnects anything currently using it.

::: note "Displays use the hotspot"
Touch 8 and Mini displays connect to the Hub hotspot. If you change its password, re-pair displays with the new credentials.
:::

## API key

Shortcuts, Siri and other integrations (see the Shortcuts, Siri & Voice Control chapter) use an **API key** instead of the Dashboard PIN. It is shown under **Settings → Integrations → Shortcuts & Siri** and works for the control address only: a key that leaks can operate named controls, but cannot change settings, read a backup or join a network. Press **New key** to replace it; every shortcut then needs its link updated. The key is not included in configuration backups.

## Remote access

LaunchControl Remote (see [Remote Access](#remote-access)) makes the dashboard reachable from the internet through LaunchControl's service, never by opening a port on the coach. It cannot be enabled without a Dashboard PIN, and every remote browser is asked for that PIN as it would be on an untrusted network — your account proves who you are to LaunchControl, the PIN proves it to the Hub. The Hub treats a connection arriving through Remote as untrusted no matter which network it is on. Share a hub only with people you would hand the PIN to; the owner can remove a shared user at any time, and **Unlink** cuts the hub off from the account entirely.

## Locked out?

Power-cycle recovery provides a way back in without a cable or support call:

- **3 quick power cycles —** opens the hotspot for 2 minutes so you can reconnect. The Dashboard PIN still applies.
- **5 quick power cycles —** clears both the Dashboard PIN and hotspot password so you can set new ones.

Only rapid cycles during the startup window count. Normal power interruptions do not accumulate into a reset.

::: technical
The Dashboard PIN is stored salted and hashed. Neither the PIN nor the hotspot password is included in configuration backups.
:::
