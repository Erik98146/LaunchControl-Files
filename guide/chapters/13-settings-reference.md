# Settings Reference

::: lead
All system configuration is organized under Settings. Use this chapter as a reference rather than a setup checklist.
:::

![Settings page](images/ch09-settings-page.png)

| **Tab** | **What lives there** |
| --- | --- |
| Status | System health: firmware version (with **Upgrade available** when a newer release is out), network state, RV-C bus health, clock, LaunchControl Remote, and MQTT and Victron while they are turned on. Debug data and the support file. |
| Network | Saved Wi-Fi networks, Hub hotspot, travel-router credentials, Dashboard PIN, hotspot password. |
| Integrations | **Remote access:** LaunchControl Remote. **Devices & services:** Bluetooth, MQTT (the Hub's built-in broker, or another broker such as a Cerbo), Victron GX, GL.iNet travel router, Weather. **Advanced connectivity:** Shortcuts & API. |
| Automations | Every automation rule and macro, the editor, and the Push / SMS alert services. |
| Floor Plans | Browse/load pre-built coach configurations and reset the current floor plan. |
| Displays | Connected displays, online status, and role-to-card assignments. |
| System | Date & time, software updates, backup & restore, connection protocol, factory reset. |
| RV-C Tools | Diagnostics and live RV-C traffic. |

::: note "Logs"
The Debug Data button on the Settings > Status page provides logs which may be downloaded and provided to tech support for analysis.
:::

## Integrations

Each integration is one card. Closed, it shows a status badge, a one‑line summary and anything that needs your attention; **Set up** or **Manage** opens its settings in place, and **Close** folds them away again without losing what you typed. Several cards can be open at once — handy for MQTT and Victron GX together.

- Settings are kept until you press **Save changes**. Until then the card shows **Unsaved changes**, and the page warns before you leave it. The badge always shows what is saved and running, never an unsaved switch.
- After a successful setup the card offers the next step — **Add Victron devices**, **Add Bluetooth devices**, **Add router card**, **Add weather card** — but never forces it.
- **Advanced settings** holds optional configuration; **Technical details** holds diagnostics, with **Copy diagnostics** for support (passwords and keys are never included).
- **Expert mode**, at the bottom of the LaunchControl Remote card, shows the relay override and the Shortcuts custom address. It is remembered on this browser only.

## LaunchControl Remote (Integrations)

The first card under Integrations. **Set up** turns LaunchControl Remote on; it needs a Dashboard PIN and a valid clock. While the Hub waits to be linked the card offers **Continue in browser** and **Scan with your phone** (a QR code and six‑digit code); once linked it shows the account and your access, with **Open remote dashboard** and **Manage remote access**. **Turn off or unlink** pauses Remote or hands the Hub to a new owner with a fresh code. See [Remote Access](#remote-access).

## Saved Wi-Fi networks

The Hub remembers up to 8 networks in priority order. At boot, and whenever it is disconnected, it joins the highest-priority saved network it can see. It also periodically checks for a higher-priority saved network. Reorder the list or forget networks you no longer use.

## The Hub hotspot

The Hub always broadcasts LaunchControl-Hub-XXXX. Touch 8 and Mini displays use this network, and it is the guaranteed direct-access path if the RV router is unavailable. A WPA2 password can be configured under Settings → Network.

## System

Settings → System holds five cards, in this order: **Date & time**, **Software updates**, **Backup & restore**, **Connection protocol** and **Factory reset**. Settings you change are kept as a draft until you press **Save changes** (or **Apply and restart** for the protocol), and the page warns before you leave it with unsaved changes. Only one action that restarts the Hub can run at a time. **Restart Hub** is on Settings → Status.

## Date & time

Schedules and timers need valid time. The card shows the Hub's current time and date, a status — **Synced**, **Manually set** or **Not synchronized** — and where the time came from and when.

- **Time zone** and **Daylight saving time** apply to Victron GPS and internet time, which report UTC. RV-C and manual time are already local. Daylight saving time is unavailable for zones that do not observe it.
- **Send Hub time to the RV-C network** lets factory panels and thermostats use the Hub's time. It is sent once a minute while the clock is set, unless the time comes from the RV-C network itself.
- **Change time source** lists RV-C network, Victron GPS, Manual and Internet time (NTP), each with the time it is offering and, if it cannot be used, why — for example *No GPS data available*.
- **Manual** shows a date and a time, and **Set to this device's time**, which saves at once. Manual time is lost when the Hub loses power. **Set the time from this browser whenever the clock is not set** restores it simply by opening Settings after a power loss.
- **Technical details** shows the RV-C address the time comes from and whether the Hub is sending time to RV-C.

## Backup & restore

**Download backup** saves one file, named after the Hub and the date, for example `launchcontrol-backup-hub-1001-2026-10-05-1348.json`. The page tells you the download started; where it is saved is up to your browser.

- **Included:** devices and their names, dashboards, panels and cards, lighting zones and scenes, automations, macros and schedules, alert settings, TV displays, display assignments, clock and unit settings, and the connection protocol. It contains the same kind of data as a Floor Plan and may be shared with others.
- **Not included:** Wi-Fi networks, the Dashboard PIN, the hotspot password, the text message key, the API access key, and the connections to MQTT, Victron GX, the travel router, weather and Remote Access. After restoring to a replacement Hub, enter those again.

**Restore from backup** never starts on its own:

1. **Choose backup file.** The page checks the file and shows what is in it — devices, cards, panels, automations, its protocol and the file date — or says why it cannot be used.
2. Read what will be replaced. **Download current backup** first if you may want today's setup back.
3. **Restore backup**, then confirm **Restore this backup?** The page shows *Restoring backup…*, *Restarting Hub…* and *Reconnecting…*, and confirms once the Hub is back. If the Hub does not answer in time, it says the result is not confirmed — reload the page a minute later.

## Connection protocol

The Hub talks to the coach's devices in one protocol at a time: **RV-C** (most RVs) or **OneControl** (Lippert coaches). The card shows the one in use. **Change protocol** opens a choice; picking one is only a draft, and the card lists exactly what the switch removes:

| **Switching to** | **Removes** |
| --- | --- |
| OneControl | All RV-C devices and their field settings, Lighting card zones and scenes, tank calibration tables, saved RV-C device details, and RV-C data on dashboard cards (the cards stay). |
| RV-C | All OneControl devices and OneControl data on dashboard cards (the cards stay). |

Victron, MQTT and Bluetooth devices, dashboards, Wi-Fi and every other setting are kept. **Download backup** first, then **Apply and restart** and confirm. Restoring a backup made before the switch brings everything back, including the protocol.

## RV-C Tools

RV-C Tools provides a live, decoded view of traffic on the coach control bus. It is intended for diagnosis and advanced troubleshooting, such as confirming what a particular device is transmitting.

A logger may be started to record a few minutes of RV-C data which may be useful for analysis.

![RV-C Tools](images/ch09-rv-c-tools.png)
