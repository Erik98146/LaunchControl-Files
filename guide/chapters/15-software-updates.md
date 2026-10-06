# Software Updates

::: lead
LaunchControl updates are released as a tested set of compatible Hub, web dashboard, Touch 8, and Mini versions. The updater manages order and compatibility.
:::

## Update the system

1. **Open Settings → System → Software updates and select Check for Updates.** The phone or computer running the browser needs internet access. The Hub does not require internet access to update.
2. **Review the available versions and release notes.**
3. **Select Update All.** Update order is handled automatically.
4. **Wait for completion.** The Hub restarts, then touchscreen updates are delivered through the Hub. The page reports each result.

::: note "Update notices"
Once a day, while a browser with internet access is open on the dashboard or Settings, the Hub checks for a newer release and adds an **Update available** alert to the alert list. Delete it once seen. Settings → Status also shows an **Upgrade available** button beside the firmware version whenever a newer Hub release is out; tap it to go straight to the update.
:::

## Safety nets

- The Hub and each display keep the previous firmware alongside the new version and can fall back if the new firmware does not start correctly.
- A display that cannot be reached is skipped and does not block the rest of the update.
- Each display has its own basic update page for manual fallback.

## Install from file

When the Hub's browser has no internet access, download the update file (`.bin`) on another device and use **Settings → System → Software updates → Install from file**:

1. **Choose update file.** Nothing is installed yet. The page reads the file and shows what it is — **Firmware update** or **Web interface update** — and its version, or why it cannot be used (for example, firmware for a different device).
2. **Install update.** Keep the Hub powered on until installation is complete. The page shows *Uploading…*, *Installing update…*, *Restarting Hub…* and *Reconnecting…*, then confirms the version now running. Devices, dashboards and settings are kept.
3. After a web interface update, reload the page to use it.

If the Hub does not answer within the wait, the page says the result is not confirmed rather than guessing; reload a minute later and check the versions shown in the card.

::: technical
Displays live on the Hub hotspot while the browser is usually on the RV router network. The Hub does not route between those networks, so display firmware is relayed through the Hub, which also reports display versions back to the browser.
:::
