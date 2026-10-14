# Resetting Things

::: lead
LaunchControl offers several very different reset actions. Choose the one that matches what you actually want to clear.
:::

**Save a backup before clearing configuration.** Use **Settings → System → Backup & restore → Download backup**. Backups exclude network credentials, access keys, and integration connections; see [Settings Reference](#settings-reference).

For a connection problem, try [Troubleshooting](#troubleshooting) first. For a sale or ownership transfer, also review unlinking Remote in [Remote Access](#remote-access).

| **Action** | **What it clears** | **What it keeps** |
| --- | --- | --- |
| Reset Floor Plan<br> (Settings → Floor Plans) | Panels, cards, devices, lighting configuration, schedules — the coach configuration. | Wi-Fi, PIN, hotspot password, integrations. Use before starting a new floor plan from scratch. |
| Restart Hub<br> (Settings → Status) | Nothing; it is only a reboot. | Everything. |
| Factory reset<br> (Settings → System) | Everything, including Wi-Fi, passwords, the API access key and the Remote Access link. | The installed software version and the Hub's licence. Use when selling the coach or starting completely fresh. |

The Factory reset card lists what is erased and offers **Download backup**. **Reset Hub** opens **Factory reset this Hub?**; type RESET, then press **Factory reset Hub**. The Hub then restarts on its own open Wi-Fi network, LaunchControl-Hub-XXXX, at 192.168.4.1 with the setup wizard, so this page cannot follow it — join that network to continue.
