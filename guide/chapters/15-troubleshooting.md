# Troubleshooting

| **Symptom** | **What to try** |
| --- | --- |
| Can’t reach launchcontrol.local | Make sure your phone/computer is on the coach Wi-Fi. On Android, use the router device list to find launchcontrol-xxxx. Recovery path: join LaunchControl-Hub-XXXX and open 192.168.4.1. |
| Router changed / new router | Join the Hub hotspot, open the dashboard, and add the new network under Settings → Network. |
| Settings → Status shows no RV-C activity | Check Hub power and the physical RV-C connection. Confirm the correct coach connection/adapter using the LaunchControl FAQ before adding devices or dashboards. |
| A card shows “—” or no value | The bound device is not reporting. Check device power; for Victron fields check Settings → Integrations; then review the card binding in edit mode. |
| Touch 8 shows its QR code again | The display lost the Hub or the Hub hotspot credentials changed. If the original network returns, wait for automatic reconnection. Otherwise pair the display again. |
| Thermostat schedule won’t enable | The Hub clock is not set. Go to Settings → System → Clock & Time and select or set a valid source. |
| Bluetooth toggle says restart required | Normal. Restart the Hub after enabling or disabling Bluetooth. |
| Forgot PIN or hotspot password | Use power-cycle recovery: 3 quick cycles temporarily opens the hotspot; 5 quick cycles clears both secrets. See Chapter 10. |
| Update check finds nothing / errors | The phone or computer running the browser needs internet access for the update check. |
| Starlink card is blank | The Hub must be on a network that can reach the dish. Check Starlink under Settings → Integrations and confirm the dish is powered. |
| Everything froze after a power blip | The Hub and router may be rebooting together. Give the router time to return; the Hub keeps retrying its saved network. |

Still stuck? Open Settings → Status before contacting support. That page contains the health information most support conversations will need.
