<!-- part: Something isn't working -->
# Troubleshooting

::: lead
Find the symptom below. Settings → Status shows the Hub’s own health — network, RV-C, clock, Remote — and is the first place to look. Still stuck? Create a support file before contacting support; it is what support will ask for.
:::

## Start with these checks

1. **Check power and connection.** Is the Hub powered, and are you on its local network or using Remote?
2. **Check Settings → Status** if the dashboard opens. Note the reported problem before changing anything.
3. **Check the alert list.** The Hub reports its own faults there: no RV-C data, a lost connection, an unset clock.
4. **Follow the matching symptom below.** Start with connection and device checks before resetting configuration.

For detailed notification checks, see [Alerts](#alerts). For Shelly relay, button, and color-light issues, see [Shelly Setup](#shelly-setup). For behavior particular to one coach brand, see [Coach-Specific Notes](#coach-specific-notes).

## I can't connect to LaunchControl

- **launchcontrol.local does not open.** Make sure your phone or computer is on the same Wi-Fi as the Hub. On Android, use the router's device list to find launchcontrol-xxxx. For direct access, join **LaunchControl-Hub-XXXX** and open [192.168.4.1](http://192.168.4.1). If you cannot join or have forgotten the password, see [Security](#security).
- **The page stops loading while I am on the Hub hotspot.** The Hub hotspot has no internet, so a phone may quietly switch to cellular data or another Wi-Fi network. Rejoin LaunchControl-Hub-XXXX and choose to stay connected if the phone asks. Turning cellular data off for a moment settles it.
- **New router, or the router changed.** Join the Hub hotspot, open the dashboard, and add the new network under Settings → Network.
- **Everything froze after a power blip.** The Hub and router may be restarting together. Give the router time to return; the Hub keeps retrying its saved network.
- **The setup wizard did not pop up.** Open a browser and go to 192.168.4.1 while on the Hub hotspot.
- **A page looks old or a new feature is missing after an update.** The browser is showing a saved copy. Reload the page; if that does not help, close the tab and open the dashboard again.

## No RV equipment appears

- **Settings → Status shows no RV-C activity**, or the setup guide's first step is not done. Check Hub power and the physical RV-C connection. Reversed RV-C data wires do not damage anything, they simply do not work, so try swapping them. Never swap the RV-C and power wires. Confirm the correct coach connection or adapter using the LaunchControl FAQ.
- **The scan is empty but Status shows data.** Operate one light, pump, or switched circuit in the RV and watch **Devices you just operated**. Devices awaiting identification may also be under **Needs identification**. Everything you already added is folded under **Already configured**, and anything you hid is under **Hidden**; press **Show** to see them.
- **A Lippert coach.** Lippert OneControl coaches do not speak RV-C. Switch the protocol under Settings → System → Connection protocol and restart; the scan then lists OneControl devices. The setup guide’s **Fix connection** says the same.

## A device is missing

- **It is not in the scan.** Clear the **Show** filter and the search box, then turn **Expert mode** on (top of the Devices page). Some device types are listed only there.
- **It shows as “Moved here · updating”.** The coach gave its controller a new network address. The Hub updates the saved device, its cards, and its lighting zones by itself within a couple of minutes. Nothing to do.
- **Cards stopped updating after the coach was powered off and on.** Same cause. Lights, switches, loads, shades, door locks, roof fans, and thermostats follow their device automatically. Tanks, batteries, and chargers do not move; if one stops reading, add it again from a new scan.
- **A Bluetooth sensor is not found.** Check that Bluetooth is on under Settings → Integrations, bring the sensor close, and wake it: press its button, or open the door it is mounted on. A Victron device must have **Instant readout via Bluetooth** turned on in VictronConnect.

## A card has no data, or the wrong data

- **The card shows “—”.** The device it is connected to is not reporting. Check the device’s power; for Victron readings check Settings → Integrations; then open the card’s gear menu, choose **Edit**, and check its data source.
- **A door, motion, or leak sensor shows nothing after a Hub restart.** These sensors report only when something happens. The card fills in the next time the sensor sends.
- **A Victron card is blank.** Victron reads the GX device's own broker. Settings → Integrations → Victron GX: press **Find Cerbo GX**, or under MQTT choose **Connect to another broker** with the GX device's address.
- **The Starlink card shows only a switch.** Open the card’s **Edit** dialog and turn on **Connect to Starlink dish**. The Hub must be on a network that can reach the dish, and the dish must be powered.
- **A tank reads the wrong amount.** Set its **Tank size**, or calibrate an odd-shaped tank with Geometry Lookup; see [Add or Change Equipment](#add-or-change-equipment).

## A control does not do what I expect

- **Nothing happens when I tap.** Check that the device is listed and reporting on the Devices page, and test it there. If the test works and the card does not, check the card’s data source.
- **The card operates the wrong device.** Correct its data source before using it again.
- **The card switches back by itself.** The dashboard shows what the equipment reports. If the equipment did not obey, or the coach’s own control system overrode the command, the card returns to the real state. Some coaches do this by design; see [Coach-Specific Notes](#coach-specific-notes).
- **An awning or shade does not stop.** On press-to-command cards, press the same direction again to stop.
- **A lighting scene does nothing.** It has not been saved yet. Set the lights, then press and hold the scene button.

## Remote isn't working

- **LaunchControl Remote stays on “Connecting”.** The Hub needs internet and a valid clock. Check Settings → Status for the network, and Settings → System → Date & time. Whether the service itself is up is shown at remote.launchcontrol.tech/status.
- **“Identity conflict”.** The Hub was reset or re-flashed while linked. Sign in at remote.launchcontrol.tech, open the hub under My hubs and press Unlink, then turn Remote on again and link it with the new code.
- **“Access expired” or “Payment needed”.** The trial or plan ran out, or a renewal charge failed. Local control is unaffected. Open the hub's page in the portal to subscribe, update the card, or redeem a code.
- **An awning, slide, or leveler will not move.** They never move through Remote, by design; use the dashboard on the coach's own Wi-Fi or a Touch 8.
- **The AI assistant does not answer or act.** See **If it does not work** in [AI Assistant](#ai-assistant).

## A display won't connect

- **The Touch 8 or Mini shows its QR code.** On its first start a display joins the only Hub hotspot in range by itself. It shows the QR code when there is no Hub in range, more than one, or the Hub hotspot has a password: scan the code and follow the pairing page.
- **It shows the QR code again later.** The display lost the Hub, or the hotspot password changed. If the original network returns, wait for automatic reconnection. Otherwise pair the display again.
- **The Touch 8 shows OFFLINE.** It has lost the Hub and is retrying. Check that the Hub is powered and within Wi-Fi range.
- **It shows the wrong cards.** Settings → Displays assigns which card each display uses for each control.

## Notifications aren't arriving

- **Nothing fired at all.** Check the alert list under Settings → Status → Alerts. The rule may have been past its threshold when it was enabled (“Triggered · at start, not fired”). Enable it while the reading is on the normal side and let it cross, or tick **Act if already triggered at start**.
- **A rule fired once and never again.** If **Latch until reset** is ticked, it stays triggered until you reset it.
- **A tank or value alarm outlines the card but sends nothing.** Card alarms only change the card. Add an automation with **Send alert**; see [Alerts](#alerts).
- **Push.** Confirm the phone is subscribed to the topic shown in Settings; a **New topic** press unsubscribes every phone.
- **SMS.** Check the credit count, and that a sender name is set on the Textbelt account page. Textbelt reports 0 credits both for an empty balance and for a key it does not recognize.
- **E-mail (Remote).** Needs the Hub linked to LaunchControl Remote with access running.
- **Send test** in Settings → Automations tells you what the service said, in its own words.

## Schedules run at the wrong time, or won't enable

- **A schedule will not enable.** The Hub's clock is not set. The Hub sets it automatically from the internet, the RV network, a GPS, or the browser that is open; Settings → System → Date & time shows which source it is using and offers **Set to this device's time**.
- **Events fire an hour off.** Check the time zone and daylight saving under Settings → System → Date & time. The card warns when two sources disagree.

## Bluetooth says "Restart needed"

This is expected after changing Bluetooth without restarting. Open Settings → Integrations → Bluetooth and press **Restart now**; **Save and restart** does both in one step.

## I forgot my PIN or hotspot password

Switch the Hub’s power on and off in a row, leaving it on for about 5 seconds each time: three times opens the hotspot for 2 minutes; five times clears both the Dashboard PIN and the hotspot password. See **Locked out?** in [Security](#security).

## The update check finds nothing

The phone or computer running the browser needs internet access for the update check. The Hub itself does not.

## Still need help?

1. **Create a support file.** Open **Settings → Status**, and under **Debug Data** press **Create Support File**. Operate the equipment that is misbehaving during the 30-second recording.
2. **Download it.** The file name ends in **.zip.txt**. That is normal; send it as it is.
3. **Describe the problem.** Include the symptom, the device or card affected, whether you were local or using Remote, and what you already tried.

The file contains the recording, your configuration, and the Hub’s logs. It does not contain Wi-Fi passwords, the Dashboard PIN, or the hotspot password; see **Support file** in [Settings Reference](#settings-reference) for the full list. Use [LaunchControl support](https://launchcontrol.tech/pages/support-faq) for installation and connection guidance.
