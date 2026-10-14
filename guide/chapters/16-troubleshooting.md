<!-- part: Something isn't working -->
# Troubleshooting

::: lead
Find the symptom below. Settings → Status shows the Hub’s own health — network, RV-C, clock, Remote — and is the first place to look. Still stuck? Open Settings → Status before contacting support; its **Debug data** is what support will ask for.
:::

## I can't connect to LaunchControl

- **launchcontrol.local does not open.** Make sure your phone or computer is on the coach Wi-Fi. On Android, use the router's device list to find launchcontrol-xxxx. The recovery path always works: join LaunchControl-Hub-XXXX and open 192.168.4.1.
- **New router, or the router changed.** Join the Hub hotspot, open the dashboard, and add the new network under Settings → Network.
- **Everything froze after a power blip.** The Hub and router may be rebooting together. Give the router time to return; the Hub keeps retrying its saved network.
- **The setup page did not pop up.** Open a browser and go to 192.168.4.1 while on the Hub's Wi-Fi.

## No RV equipment appears

- **Settings → Status shows no RV-C activity**, or the setup guide's first step is not done. Check Hub power and the physical RV-C connection. Reversed RV-C H and L wires do not damage anything, they simply do not work, so try swapping them. Never swap the RV-C and power wires. Confirm the correct coach connection or adapter using the LaunchControl FAQ.
- **The scan is empty but Status shows data.** Lights, pumps and switched circuits appear only when operated — turn one on and off in the coach. Everything you already added is folded under **Already configured**; press **Show** to see it.
- **A Lippert coach.** Lippert OneControl coaches do not speak RV-C. Switch the protocol under Settings → System → Connection protocol and restart; the scan then lists OneControl devices. The setup guide’s **Fix connection** says the same.

## A device is missing

- **It is not in the scan.** Turn **Expert mode** on (top of the Devices page). Some device types are listed only there.
- **It shows as "Moved here from …".** The coach gave its controller a new network address. The Hub updates the saved device, its cards and lighting zones by itself within a couple of minutes. Nothing to do.
- **Cards stopped updating after the coach was powered off and on.** Same cause. Lights, switches, loads, shades and door locks follow their device automatically; other readings may need their device re-added from a new scan.

## A card has no data

- **The card shows "—".** The bound device is not reporting. Check device power; for Victron readings check Settings → Integrations; then open the card's edit menu and check its data source.
- **A Victron card is blank.** Victron reads the GX device's own broker. Settings → Integrations → Victron GX: press **Find Cerbo GX**, or under MQTT choose **Connect to another broker** with the GX device's address.
- **The Starlink card is blank.** The Hub must be on a network that can reach the dish. Check Starlink under Settings → Integrations and confirm the dish is powered.

## Remote isn't working

- **LaunchControl Remote stays on "Connecting".** The Hub needs internet and a valid clock. Check Settings → Status for the network, and Settings → System → Date & time. Whether the service itself is up is shown at remote.launchcontrol.tech/status.
- **"Identity conflict".** The Hub was reset or re-flashed while linked. Sign in at remote.launchcontrol.tech, open the hub under My hubs and press Unlink, then enable Remote again and link it with the new code.
- **"Access expired" or "Payment needed".** The trial or plan ran out, or a renewal charge failed. Local control is unaffected. Open the hub's page in the portal to subscribe, update the card, or redeem a code.
- **An awning, slide or leveler will not move.** They never move through Remote, by design; use the dashboard on the coach's own Wi-Fi or a Touch display.

## A display won't connect

- **The Touch 8 or Mini shows its QR code.** On its first start a display joins the only LaunchControl Hub hotspot in range by itself. It shows the QR code when there is no Hub in range, more than one, or the Hub hotspot has a password: scan the code and follow the pairing page.
- **It shows the QR code again later.** The display lost the Hub, or the Hub hotspot credentials changed. If the original network returns, wait for automatic reconnection. Otherwise pair the display again.
- **It shows the wrong cards.** Settings → Displays assigns which card each display uses for each role.

## Notifications aren't arriving

- **Nothing fired at all.** Check the alert list under Settings → Status → Alerts. The rule may have been past its threshold when it was enabled ("Triggered · at start, not fired"). Enable it while the reading is on the normal side, then let it cross.
- **Push.** Confirm the phone is subscribed to the topic shown in Settings; a **New topic** press unsubscribes every phone.
- **SMS.** Check the credit count, and that a sender name is set on the Textbelt account page. Textbelt reports 0 credits both for an empty balance and for a key it does not recognise.
- **E-mail (Remote).** Needs the Hub linked to LaunchControl Remote with access running.
- **Send test** in Settings → Automations tells you what the service said, in its own words.

## Schedules run at the wrong time, or won't enable

- **A schedule will not enable.** The Hub's clock is not set. The Hub sets it automatically from the internet, the coach network, a GPS or the browser that is open; Settings → System → Date & time shows which source it is using and offers **Set to this device's time**.
- **Events fire an hour off.** Check the time zone and daylight saving under Settings → System → Date & time. The card warns when two sources disagree.
- **Bluetooth says "Restart needed".** Normal after changing Bluetooth without restarting. Open Settings → Integrations → Bluetooth and press **Restart now**; **Save and restart** does both in one step.

## I forgot my PIN

Power-cycle recovery works without a cable or a support call: 3 quick power cycles temporarily opens the hotspot; 5 quick cycles clears both the Dashboard PIN and the hotspot password. See [Security](#security).

## The update check finds nothing

The phone or computer running the browser needs internet access for the update check. The Hub itself does not.
