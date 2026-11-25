# Add or Change Equipment

::: lead
Find the lights, pumps, tanks and other equipment built into your RV. Name the devices you want and LaunchControl creates their dashboard cards. You can return to this page any time to add or change equipment.
:::

For Victron, wireless sensors, Shelly, internet equipment and other optional connections, see [Connecting Additional Equipment](#connecting-additional-equipment).

## Find your built-in RV equipment

RV-C devices are the coach’s built-in lights, pumps, tanks, thermostats, awnings, slides, generators, batteries, inverters, and similar equipment. The Devices page lists everything currently configured on the Hub, grouped by its source: RV-C devices, Victron devices, and so on.

### Find equipment

1. **Open Devices.**
2. **Press Add devices.** If other sources are set up, choose **Scan RV**.
3. **Wait a few seconds.** The list fills with what the Hub hears on the RV’s control network, with a live reading on each row, in sections: **Devices you just operated**, **Needs identification**, **Ready to add**, and **Already configured**. Each row names the device type and its instance number, which is what the RV’s own paperwork uses.

Equipment that reports all the time — thermostats, tank sensors, batteries, inverters, solar — appears under Ready to add, already ticked. Lights, pumps, awnings, and other switched circuits wait under Needs identification until they are operated.

On a coach with a long list, narrow it down:

- **Search found equipment** finds a row by name.
- **Show** limits the list to one kind of equipment, such as Tank, Thermostat, or Switched output. It appears once the scan has found two or more kinds. Rows you already ticked stay ticked while they are filtered out of view.
- **Sort** orders the list by name or by the order things were found.

The **⋯ More** button holds the session details and a manual refresh. Leaving with devices ticked but not added asks first.

### Identify lights, pumps, and other switched devices

The easiest way to tell which row is which is to operate the device in the RV.

1. **Turn it on, then off,** from the RV’s own switch or panel.
2. **Watch the list.** The device that just changed moves to the top under **Devices you just operated**, ticked and highlighted in green. Work with one device at a time so it stays clear which row is which.

The other direction works too: press a row’s **ID** button to switch that output on from the Hub and see which light comes on. Press **ID** again to switch it back off. ID is offered only for lights and switched circuits; awnings, slides, and shades show a dash, because they should never be operated without someone watching them.

::: warning "Identify equipment safely"
Use the RV’s original switch first. An ID command energizes a switched output and may operate a door lock or other connected equipment. Only use ID when you know it is safe and can observe the output.
:::

### Add the devices

We suggest only adding known devices. Unknown devices may appear on the RV-C network without an obvious purpose and should be ignored. Everything happens on the one screen:

1. **Tick the devices to add.** Ready-to-add and just-operated devices start ticked; untick any you do not want. **Select all** and **none** under Ready to add tick or clear that section.
2. **Name each device** in its row — for example, Bench Light, Kitchen Light, Water Pump.
3. **Say what each switched circuit is** in its **What is it?** box. A dimmer or relay output can drive a light, a water pump, a fan, an awning, shades, a door lock, a TV lift, or a Starlink dish, and only you know which. LaunchControl shows a guess under the box but never picks for you. Choose **No card** to add the device without a dashboard card; untick the row to leave the device out. Batteries, tanks, thermostats, and the like show the card they will get.
4. **Choose where the cards go** — only when you have more than one panel, or in Expert mode. **Put the cards on**, in the bar under the list, picks the panel or makes a new one; otherwise the cards go on your dashboard.
5. **Press Add Equipment & Create Dashboard.** The bar says what one press will do — how many devices and how many cards. If a selected switched circuit has no type, you cannot continue; the red note takes you to the first unfinished row. **No card** counts as an answer and is not asked again. The devices are added one at a time and their cards are created straight after. From the setup guide, it returns you to the guide.

![Add Device – Found RV-C devices page](images/devices01.png)

### Hide equipment you will never add

Most coaches report outputs that are not connected to anything. To stop one from being offered in every scan, press **Hide** on its row. It moves to a collapsed **Hidden** section at the bottom of the list; press **Show** there and then **Unhide** to bring it back. A device you have already added cannot be hidden.

### Scanning again

A second scan folds the devices you already added under **Already configured**, with their count; press **Show** to list them anyway. When there is nothing new, the list says **Nothing new found yet** and suggests operating a light or switch.

::: technical
Some coaches give their controllers new network addresses after a power cycle. A device that moved shows as Moved here · updating instead of as something new; the Hub updates its saved address, its cards, and its lighting zones by itself within a couple of minutes, and notes it in the alert list. Nothing to do.

To keep the list readable, protocol-level detail is hidden: message numbers (DGNs), instance numbers, source addresses, and the rarely used device types. **Expert mode** — the switch at the top of the Devices page, and the same switch in the scan — shows all of it, on every page of LaunchControl, in this browser. If you cannot find a device, turn Expert mode on; some device types are listed only there. See the [Technical Reference](#technical-reference) for what the numbers mean.
:::

### Change a device

Select a device in the list to test it, rename it, or edit its fields — which readings are shown, their units and rounding, a tank’s size, a dimmer’s memory behavior. A device’s ⋮ menu offers **Add to dashboard** for a device that has no card yet, and **Remove**. Removing a device clears its card bindings and deletes a card left with nothing bound.

## Tank size and calibration

A tank sensor reports a percentage. Two optional settings turn that into an amount. Open **Devices**, select the tank, and edit it.

### Tank size

Enter how much the tank holds when full under **Tank size** and press **Save**. The Tank card then shows how much is in the tank as well as the percentage, in gallons or liters according to the Hub’s units setting. This is all a rectangular tank needs.

### Geometry Lookup for an odd-shaped tank

A sensor measures the liquid level, which does not match the contents of an irregular shaped tank. **Geometry Lookup** corrects it with a table you build once by adding known amounts of water.

1. **Level the RV and empty the tank.**
2. **Tick Geometry Lookup, then press Start.** The first entry, 0 added, is recorded for you.
3. **Add water in known amounts.** After each amount, type it under **Water added since last entry** and press **Save Entry**. A water flow meter helps. Amounts of 1–2 gallons give a good table; up to 32 entries are kept. **Undo Last** removes a mistake.
4. **Press Finish when the tank is full.** This also sets the tank size, so there is no need to enter it separately.

The correction applies immediately on the dashboard and the displays. **Export CSV** saves the table for backup or for another coach with the same tank; **Import CSV** loads one instead of entering the points by hand. **Recalibrate** starts over and **Remove Table** returns to the plain sensor reading.


### Wavetronix Fathom (radar) sensors

A Fathom sensor arrives set up as fresh tank 1 on a tank 39.3 inches deep, so it needs to be told what it is really mounted on. Press **Fathom sensor setup…** in the tank’s editor, or **Set up** on its row in the scan.

1. **Choose the tank** the sensor is on: fresh, gray, or black, 1 to 3.
2. **Enter the tank’s depth** as a single region, in inches from the bottom.
3. **Press Program sensor.** With the tank empty, **Tank is empty** lets the sensor size itself.

Changing which tank the sensor reports makes it come back as a new device: add it from the scan, then remove the old entry.

## Check your equipment

You’re done when the expected readings appear and each card controls the equipment you intended. If a control operates the wrong equipment, stop using it and correct the device or card data source. See [Troubleshooting](#troubleshooting).
