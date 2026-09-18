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

## Locked out?

Power-cycle recovery provides a way back in without a cable or support call:

- **3 quick power cycles —** opens the hotspot for 2 minutes so you can reconnect. The Dashboard PIN still applies.
- **5 quick power cycles —** clears both the Dashboard PIN and hotspot password so you can set new ones.

Only rapid cycles during the startup window count. Normal power interruptions do not accumulate into a reset.

::: technical
The Dashboard PIN is stored salted and hashed. Neither the PIN nor the hotspot password is included in configuration backups.
:::
