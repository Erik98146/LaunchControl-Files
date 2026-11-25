# The Touch 8 Display

::: lead
Touch 8 mirrors the dashboard you build on the web: the same panels, cards, names, and positions, with touch control for supported cards. When you change the web dashboard layout, Touch 8 updates to match. It connects to the Hub hotspot directly and continues to work when the RV router is off.
:::

## Set up a Touch 8

If you plan to protect the Hub hotspot with a password, set it first under [Security](#security), then pair the display.

1. **Power the display near the Hub.** A new display looks for a Hub hotspot; with exactly one in range and no hotspot password set, it joins by itself and shows the dashboard — nothing else to do.
2. **If it shows a QR code instead,** scan it with your unlocked phone and join the temporary setup network it offers. That happens when no Hub is in range, more than one is, or the Hub hotspot has a password.
3. **Follow the display’s pairing page.** Pick the Hub and enter the hotspot password if there is one.
4. **Finish.** The display downloads the dashboard and reconnects automatically after future restarts.

![Touch 8 Dashboard](images/ch07-touch-8-dashboard.jpg)

## Use the Touch 8

- **Panel tabs —** tap a tab to switch panels. A tab with a small arrow has sub-panels: press and hold it to list them, then tap one.
- **Header —** the clock, and beside it either two temperatures or the weather. Tap the weather for the forecast.
- **Cards —** tap and press-and-hold work as on the web dashboard: tap a light, pump, or lock to switch it; tap a Climate, Shore Power, awning, or shades card to open its controls; press and hold a dimmer for its slider, a color light for its color wheel, or a lighting scene to save it.
- **Alarms —** a tank or value card with an alarm set shows the same amber or red outline as the web dashboard. The alert list itself is on the web dashboard.

Touch 8 is a control surface, not a configuration interface. Device setup, card editing, schedules, scene contents, and automations are configured in the web dashboard.

## The Settings screen

The menu button at the top right opens the Settings screen.

- **Status —** firmware version and serial number, whether the Hub is connected, Wi-Fi signal, the display’s address, and a **Remote** row that mirrors the Hub’s LaunchControl Remote state: Off, Connecting, *Waiting to be linked* with the link code, or Online with the plan’s remaining days. The display never turns Remote on or off; that is done in the Hub’s Settings or in the portal.
- **Brightness —** the normal level, a dimmed level, and how long to wait before dimming.
- **Sleep —** how long before the screen turns off. The first touch only wakes the screen; it never operates a card.
- **Night mode —** a lower brightness between the hours you choose. It needs the Hub’s clock to be set.
- **Re-pair hub —** press and hold to return to the pairing screen.

## Choose which devices it uses

The Hub normally chooses the battery, water pump, climate zone, and other controls from your dashboard cards automatically. If the coach has several devices that could fill the same role, use **Settings → Displays** on the Hub to choose which card each Touch 8 should use. For example, assign the climate card for the room where the display is installed.

## If the Hub is out of reach

When the display loses the Hub, a red **OFFLINE** replaces the clock. It keeps retrying and recovers by itself when the Hub returns.

If the Hub is reset or its hotspot password changes, the display returns to its QR pairing screen while it continues to retry the previous connection. If the Hub comes back with the original settings, the display rejoins automatically; otherwise pair it again.

## Updates

Touch 8 software is updated from the Hub: **Settings → System → Software updates** lists each display with its version, and **Update All** updates the Hub first and then the displays. See [Software Updates](#software-updates).
