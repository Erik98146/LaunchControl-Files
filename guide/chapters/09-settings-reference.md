# Settings Reference

::: lead
All system configuration is organized under Settings. Use this chapter as a reference rather than a setup checklist.
:::

![Settings page](images/ch09-settings-page.png)

| **Tab** | **What lives there** |
| --- | --- |
| Status | System health: network state, RV-C bus health, memory, uptime, version. |
| Network | Saved Wi-Fi networks, Hub hotspot, travel-router credentials, Dashboard PIN, hotspot password. |
| Integrations | MQTT broker, Victron, Bluetooth, Starlink. |
| Floor Plans | Browse/load pre-built coach configurations and reset the current floor plan. |
| Displays | Connected displays, online status, and role-to-card assignments. |
| System | Backup/restore, clock/time, software updates, restart, factory reset. |
| RV-C Tools | Diagnostics and live RV-C traffic. |

::: note "Logs"
The Debug Data button on the Settings > Status page provides logs which may be downloaded and provided to tech support for analysis.
:::

## Saved Wi-Fi networks

The Hub remembers up to 8 networks in priority order. At boot, and whenever it is disconnected, it joins the highest-priority saved network it can see. It also periodically checks for a higher-priority saved network. Reorder the list or forget networks you no longer use.

## The Hub hotspot

The Hub always broadcasts LaunchControl-Hub-XXXX. Touch 8 and Mini displays use this network, and it is the guaranteed direct-access path if the RV router is unavailable. A WPA2 password can be configured under Settings → Network.

## Backup & restore

Settings → System → Backup downloads one file containing panels, cards, devices, lighting scenes, schedules, display assignments, and automations. Save a backup after significant configuration work. This contains all the same data as a Floor Plan and may be shared with others.

::: note "Secrets are not backed up"
Wi-Fi passwords, the Dashboard PIN, hotspot password, and broker credentials are deliberately excluded from backups. After restoring to a replacement Hub, enter those credentials again.
:::

## Clock & time

Schedules and timers need valid time. The Hub can use time from RV-C, Victron GPS, or a manual setting. The Clock & Time page shows available sources and lets you select which source to trust. Timezone and DST settings apply to the GPS and NTP sources. System time can be published back to the RV-C bus so your factory panels always have the correct time.

## RV-C Tools

RV-C Tools provides a live, decoded view of traffic on the coach control bus. It is intended for diagnosis and advanced troubleshooting, such as confirming what a particular device is transmitting.

A logger may be started to record a few minutes of RV-C data which may be useful for analysis.

![RV-C Tools](images/ch09-rv-c-tools.png)
