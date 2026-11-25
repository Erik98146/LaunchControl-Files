# Backups, Restores & Resets

::: lead
Save a copy of your setup, restore it when needed, or choose the reset that matches what you actually want to clear.
:::

**Save a backup before clearing configuration.** Use **Settings → System → Backup & restore → Download backup**. Backups exclude certain credentials and integration connections; the full list is below.

For a connection problem, try [Troubleshooting](#troubleshooting) first. For a sale or ownership transfer, also review unlinking Remote in [Remote Access](#remote-access).

## Backup & restore

**Download backup** saves one file, named after the Hub and the date, for example `launchcontrol-backup-hub-1001-2026-10-05-1348.json`. The page tells you the download started; where it is saved is up to your browser.

- **Included:** devices and their names, panels and cards, lighting zones and scenes, automations, macros and schedules, alert settings, TV displays, display assignments, clock and unit settings. It contains the same kind of data as a floor plan. It also holds the encryption keys of any Bluetooth devices you added, so share it only with people you trust.
- **Not included:** Wi-Fi networks, the Dashboard PIN, the hotspot password, the text message key, the API access key, and the connections to MQTT, Victron GX, the travel router, weather and Remote Access. After restoring to a replacement Hub, enter those again.

**Restore from backup** never starts on its own:

1. **Choose backup file.** The page checks the file and shows what is in it — devices, cards, panels, automations, and the file date — or says why it cannot be used.
2. **Review what will be replaced.** **Download current backup** first if you may want today's setup back.
3. **Restore backup**, then confirm **Restore this backup?** The page shows *Restoring backup…*, *Restarting Hub…* and *Reconnecting…*, and confirms once the Hub is back. If the Hub does not answer in time, it says the result is not confirmed — reload the page a minute later.


## Choose the right reset

| **Action** | **What it clears** | **What it keeps** |
| --- | --- | --- |
| Reset Floor Plan<br> (Settings → Floor Plans) | Panels, cards, devices, lighting configuration, schedules — the coach configuration. | Wi-Fi, PIN, hotspot password, integrations. Use before starting a new floor plan from scratch. |
| Restart Hub<br> (Settings → Status) | Nothing; it is only a restart. Running off-timers and graph history start over. | Everything. |
| Factory reset<br> (Settings → System) | Everything, including Wi-Fi, passwords, the API access key and the Remote Access link. | The installed software version and the Hub's license. Use when selling the coach or starting completely fresh. |

The Factory reset card lists what is erased and offers **Download backup**. **Reset Hub** opens **Factory reset this Hub?**; type RESET, then press **Factory reset Hub**. The Hub then restarts on its own open Wi-Fi network, LaunchControl-Hub-XXXX, at 192.168.4.1 with the setup wizard, so this page cannot follow it — join that network to continue.

Smaller resets, each described in its own chapter: **Remove** a display under Settings → Displays; **Replace key** for the API access key; **Unlink** a Hub from LaunchControl Remote; and the power-cycle recovery for a forgotten PIN in [Security](#security).

## Transfer ownership

1. **Save any configuration you want to keep.** Store the backup securely; it can contain Bluetooth encryption keys.
2. **Remove external access.** Turn off AI access and remote support, review shared users, and delete location history if desired. Unlink the Hub in LaunchControl Remote; this cancels its plan.
3. **Factory reset the Hub.** Follow the reset procedure above. Remove old shortcuts and connector links from your own devices.
4. **Check the result.** Verify that the Hub is back at its first-use wizard and no longer appears as linked to your account. Do not hand over your private backup or credentials.

For account deletion and cloud data questions, see [Remote Access](#remote-access) or contact support.
