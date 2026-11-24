<!-- part: Maintain -->
# Settings Reference

::: lead
All system configuration is organized under Settings. Use this chapter to look things up; for a new installation, follow [Set Up Your Hub](#set-up-your-hub) instead.
:::

## Find a common setting

| Task | Location |
| --- | --- |
| Change units or time zone | **Settings → System → Units** or **Date & time** |
| Reopen the setup guide | **Settings → System → Setup guide** |
| Save or restore a backup | **Settings → System → Backup & restore** |
| Change Wi-Fi, trusted networks, Dashboard PIN, or hotspot password | **Settings → Network** |
| Pair or assign displays | **Settings → Displays** |
| Connect equipment or Remote | **Settings → Integrations** |
| Create rules, macros, or notifications | **Settings → Automations** |
| Show technical fields | **Expert mode**; this preference is saved in the current browser |
| Check health or restart the Hub | **Settings → Status** |
| Create a support file | **Settings → Status → Debug Data → Create Support File** |
| Change the dashboard theme | Panel edit mode → **Theme** |

## Settings tabs

![Settings page](images/ch09-settings-page.png)

| **Tab** | **What lives there** |
| --- | --- |
| Status | System health: firmware version (with **Upgrade available** when a newer release is out), network state, RV-C network health, clock, LaunchControl Remote, and MQTT and Victron while they are turned on. The alert list, **Debug Data**, and the support file. |
| Network | The Hub hotspot and its password, the current Wi-Fi connection, saved Wi-Fi networks with their **Trusted** switch, and the Dashboard PIN. |
| Integrations | **Remote access:** LaunchControl Remote. **Devices & services:** Bluetooth, MQTT (the Hub's built-in broker, or another broker such as a Cerbo), Victron GX, GL.iNet travel router, Weather. **Advanced connectivity:** Shortcuts & API. |
| Automations | Every automation and macro with its editor, **Proactive alerts**, and the notification services: phone notifications, text messages, email, and notification limits. |
| Floor Plans | Browse/load pre-built coach configurations and reset the current floor plan. |
| Displays | Connected Touch 8 and Mini displays with the card each one uses for each control, and TV and wall displays. |
| System | Date & time, units, the setup guide, Expert mode, software updates, backup & restore, connection protocol, factory reset, about & legal. |
| RV-C Tools | Diagnostics and live RV-C traffic. |


## Integrations

Each integration is one card. Closed, it shows a status badge, a one‑line summary and anything that needs your attention; **Set up** or **Manage** opens its settings in place, and **Close** folds them away again without losing what you typed. Several cards can be open at once — handy for MQTT and Victron GX together.

- Edits remain a draft until you press **Save changes**. Until then the card shows **Unsaved changes**, and the page warns before you leave it. The badge always shows what is saved and running, never an unsaved switch.
- After a successful setup the card offers the next step — **Add Victron devices**, **Add Bluetooth devices**, **Add router card**, **Add weather card** — but never forces it.
- **Advanced settings** holds optional configuration; **Technical details** holds diagnostics, with **Copy diagnostics** for support (passwords and keys are never included).
- **Let the AI assistant use this Hub**, on the LaunchControl Remote card, shares the Hub’s API access key with LaunchControl Remote so an AI assistant can be connected; see [AI Assistant](#ai-assistant).
- **Expert mode**, at the bottom of the LaunchControl Remote card, is the one Expert mode for the whole product: it shows the relay override and the Shortcuts custom address here, and the technical detail everywhere else — DGNs, instances, source addresses, raw bindings. The same switch sits at the top of the Devices page. It is remembered on this browser only.

## LaunchControl Remote (Integrations)

The first card under Integrations. **Set up** turns LaunchControl Remote on; it needs a Dashboard PIN and a valid clock. While the Hub waits to be linked the card offers **Continue in browser** and **Scan with your phone** (a QR code and six‑digit code); once linked it shows the account and your access, with **Open remote dashboard** and **Manage remote access**. **Turn off or unlink** pauses Remote or hands the Hub to a new owner with a fresh code. See [Remote Access](#remote-access).

## Saved Wi-Fi networks

The Hub remembers up to 8 networks in priority order. At startup, and whenever it is disconnected, it joins the highest-priority saved network it can see. It also periodically checks for a higher-priority saved network. Reorder the list or forget networks you no longer use.

Each saved network has a **Trusted** switch. While the Hub is joined to a trusted network, the dashboard does not ask for the Dashboard PIN. Turn it on only for your own RV or home network, and leave it off for campground, marina, or other shared Wi-Fi. LaunchControl Remote always asks for the PIN.

## The Hub hotspot

The Hub always broadcasts LaunchControl-Hub-XXXX. Touch 8 and Mini displays use this network, and it is the guaranteed direct-access path if the RV router is unavailable. A WPA2 password can be set under **Settings → Network → Hub Hotspot**. Devices on a password-protected Hub hotspot are trusted and are not asked for the Dashboard PIN.

## System

Settings → System contains **Date & time**, **Units**, **Setup guide**, **Expert mode**, **Software updates**, **Backup & restore**, **Connection protocol**, **Factory reset**, and **About & Legal**.

- **Units** changes the whole product between US customary and metric.
- **Setup guide** reopens the seven-step checklist with completed and remaining steps.
- **Expert mode** shows technical detail throughout the product. The Devices page has the same switch.
- **Save changes** applies your draft edits. For the connection protocol, use **Apply and restart** instead. The page warns before you leave with unsaved changes.
- Only one restart action can run at a time. **Restart Hub** is under **Settings → Status**.

Before changing the connection protocol or restoring a backup, read what will be replaced and download your current backup.

## Date & time

Schedules and timers need valid time. The card shows the Hub's current time and date, a status — **Synced**, **Manually set** or **Not synchronized** — and where the time came from and when. The time source is **Automatic** unless you change it: internet time whenever the Hub has it, otherwise the RV-C network, then Victron GPS, then the browser that is open. The card warns when two sources disagree by more than a couple of minutes, and says which one is being used.

- **Time zone** and **Daylight saving time** apply to Victron GPS and internet time, which report UTC. RV-C and manual time are already local. Daylight saving time is unavailable for zones that do not observe it.
- **Send Hub time to the RV-C network** lets factory panels and thermostats use the Hub's time. It is sent once a minute while the clock is set, unless the time comes from the RV-C network itself.
- **Time source (advanced)** lists **Automatic (recommended)** and the four manual choices — RV-C network, Victron GPS, Manual and Internet time (NTP) — each with the time it is offering and, if it cannot be used, why — for example *No GPS data available*. Pick a source only to force one.
- **Manual** shows a date and a time, and **Set to this device's time**, which saves at once. Manual time is lost when the Hub loses power. **Set the time from this browser whenever the clock is not set** restores it simply by opening Settings after a power loss.
- **Technical details** shows the RV-C address the time comes from and whether the Hub is sending time to RV-C.

## Backup & restore

**Download backup** saves one file, named after the Hub and the date, for example `launchcontrol-backup-hub-1001-2026-10-05-1348.json`. The page tells you the download started; where it is saved is up to your browser.

- **Included:** devices and their names, panels and cards, lighting zones and scenes, automations, macros and schedules, alert settings, TV displays, display assignments, clock and unit settings, and the connection protocol. It contains the same kind of data as a floor plan. It also holds the encryption keys of any Bluetooth devices you added, so share it only with people you trust.
- **Not included:** Wi-Fi networks, the Dashboard PIN, the hotspot password, the text message key, the API access key, and the connections to MQTT, Victron GX, the travel router, weather and Remote Access. After restoring to a replacement Hub, enter those again.

**Restore from backup** never starts on its own:

1. **Choose backup file.** The page checks the file and shows what is in it — devices, cards, panels, automations, its protocol and the file date — or says why it cannot be used.
2. Read what will be replaced. **Download current backup** first if you may want today's setup back.
3. **Restore backup**, then confirm **Restore this backup?** The page shows *Restoring backup…*, *Restarting Hub…* and *Reconnecting…*, and confirms once the Hub is back. If the Hub does not answer in time, it says the result is not confirmed — reload the page a minute later.


## Support file

When support asks for a support file, open **Settings → Status**, find **Support file** in the **Debug Data** card, and press **Create Support File**. The Hub records 30 seconds of the RV’s control network, so operate the equipment that is misbehaving while it counts down, and leave the page open. Then press **Download** and email the file to support.

The file is named `launchcontrol-support-` followed by your Hub’s serial number and ends in **.zip.txt**. That odd ending is deliberate: it is an ordinary ZIP archive, named this way because browsers block ZIP downloads from a local device. Send it as it is. To look inside, remove the `.txt` from the name.

| In the file | Not in the file |
| --- | --- |
| The Hub’s serial number, software version, uptime, clock, and memory figures | Wi-Fi passwords |
| The 30-second recording of the RV’s control network | The Dashboard PIN |
| A configuration backup, the same as **Download backup** | The hotspot password |
| Network status: addresses, signal, and the names of saved Wi-Fi networks | The MQTT broker password |
| Discovered devices and their current readings | The router admin password |
| The Hub’s diagnostic log, and a crash report if one is stored | The text message key and the API access key |

The backup inside it does include the encryption keys of Bluetooth devices you added.

## RV-C Tools

RV-C Tools provides a live, decoded view of traffic on the RV’s control network. It is intended for diagnosis and advanced troubleshooting, such as confirming what a particular device is transmitting.

To capture a problem for analysis, start the frame logger, operate the equipment, stop the logger, and download the recording. Each recording is stamped with the Hub’s serial number and software version. A support file (above) makes a 30-second recording for you.

![RV-C Tools](images/ch09-rv-c-tools.png)
