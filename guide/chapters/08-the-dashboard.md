<!-- part: Make it yours -->
# The Dashboard

::: lead
The dashboard is a set of live cards organized into panels. Cards update in real time; cards that support control respond when tapped. LaunchControl builds the cards for you when you add equipment; this chapter is about arranging them and adding more.
:::

![A finished dashboard](images/ch04-a-finished-dashboard.png)

## Try moving a card

1. **Enter panel edit mode** from the menu at the top right.
2. **Drag a card** using its top-left grab handle.
3. **Exit edit mode.** Your layout is saved on the Hub.

That is all you need to move a card. YOu can have a different layout on a phone. When editing from a phone, or small device, the first move creates a separate narrow-screen layout that will be seen wehn opening from that type of device.

## Panels

Panels create additional names and/or icons at the top of the dashboard. Use any names and grouping that suit you. Panels group cards; sub-panels add a second level when you need more room.

### Open a panel

- **Panel tabs —** switch between groups such as Main, Power, and Climate. Each panel has its own name, icon (or two), and layout. As many tabs as fit are shown across the top; the rest are always one tap away under the **All panels** icon (the grid icon at the end of the tabs).
- **Sub-panels —** each panel can hold up to five sub-panels, and the dashboard holds up to six panels. Tap a tab's name to open it, or tap the small arrow beside it to choose one of its sub-panels. While a sub-panel is open, its tab reads "Panel › Sub-panel".
- **All panels —** shows every panel and sub-panel in your order, with the one showing marked. Tap any of them to go there. With more than eight panels a search box appears. **Manage panels** at the bottom opens the panel manager.

### Manage panels

- **Graph History —** each panel sets the history window used by graphs on that panel.
- **Managing panels —** open **Manage panels** (from All panels, or from edit mode). Each panel has a **⋯** menu: **Edit** (name, icons and parent, with a preview), **Add sub-panel**, **Move…** (put it under another panel or back on top), **Duplicate**, **Move up / down** and **Delete**. Drag a panel by its handle to reorder it; the new order is saved when you press **Done**. Other changes save as soon as you make them, with **Undo** for a few seconds. Deleting a panel tells you first what happens to its cards and sub-panels.
- **Coming back —** reloading the page returns to the panel you were on; opening the dashboard fresh starts on the first panel.
- **Every screen follows —** a change to cards or panels made on one phone or laptop shows up on every other open dashboard, including TVs, within a couple of seconds. A dashboard that is in the middle of editing waits until the editor closes.

## Add cards

Most cards are created when equipment is added (see [Add or Change Equipment](#add-or-change-equipment)). For the rest:

- **Create cards for new devices —** in panel edit mode, under **Dashboard Cards**. It makes a card for every device, from every source, that has none yet, after asking what each switched output is. The setup guide’s **Create dashboard** is the same button.
- **Add a card… —** also under Dashboard Cards. Pick a type from the grouped list (Power, Climate, Water, Security, Lights & switches, Motors, Internet, Utility, Victron) and the card editor opens with its data source to choose. Use it for cards that stand alone: Clock, Weather, Web Link, Sleep Timer, Power Diagram, an extra Lighting Scenes card for another part of the coach.
- **Add to dashboard —** on the Devices page, a device’s ⋮ menu makes its default card.

Cards are placed in the panel you are looking at. **Move or copy…** in a card’s gear menu puts it on another panel.

## Arrange the cards

1. **Enter panel edit mode** from the menu at the top right.
2. **Drag cards into position.** The grab handle is in the top left of the card. Cards snap into the dashboard grid.
3. **Open a card’s gear menu** to edit, duplicate, move or remove it.
4. **Exit edit mode.** The layout is stored on the Hub. Narrow screens can keep their own card positions, as described below.

::: note "Responsive layout"
The dashboard grid adapts to screen size, so the same configuration can be used on desktop, phone, and Touch 8 displays. Narrow screens keep their own card positions: the first time you drag a card on a phone, the phone layout is yours to arrange separately.
:::

## The cards at a glance

The **Add a card…** list is grouped the way this table is. [Card Reference](#card-reference) describes each card’s sizes, gestures, and settings.

| **Group** | **Cards** | **What they are for** |
| --- | --- | --- |
| Power | Battery + Power, Inverter, Shore Power, Solar, Alternator, Battery Charger, Power Diagram | State of charge, power flow, charging sources, the inverter, and the shore current limit |
| Climate | Climate, Hydronic, Roof Fan | Thermostats with schedules, hydronic heat, and roof fans |
| Water | Tank, Water Pump, Tank Heat | Tank levels with optional alarms, the pump, and tank heaters |
| Security | Door Lock | Lock and unlock with one tap |
| Lights & switches | Light Dimmer, Color Light, Lighting Scenes, Generic Switch, Fan, Linked Switch, Panel Backlight, Sleep Timer | Single lights, groups and scenes, plain on/off outputs, and the nightly shut-off |
| Motors | Awning, Shades, Slide, TV Lift | Things that move |
| Internet | Starlink, Travel Router | Connection status, dish power, joining Wi-Fi, and speed tests |
| Utility | Clock, Generic - Single, Generic - Dual, Automation, Macro, Web Link, Weather | A clock, any other reading with an optional alarm, one-tap automations and macros, links, and the forecast |
| Victron | Victron MultiPlus, Battery Monitor, Shore Power, MPPT, GPS, and temperature cards | Equipment read through a Victron GX device or Victron Bluetooth |

The card editor shows a preview of the card at its real size, with sample values, for every layout you pick.

## Header icons

The icons at the top right of the dashboard, from left to right:

- **Warning triangle —** appears when something needs attention; a number on it is the count of unread alerts. Tap it to see them.
- **Connection dot —** green while the dashboard is receiving live data, amber while it reconnects.
- **Cloud —** LaunchControl Remote. On a dashboard opened through Remote it shows that page's own link: green while connected, amber while reconnecting. On the coach's own network it appears while someone is viewing the Hub through Remote.
- **Menu —** Settings, Devices and the other pages.

When a panel header shows the weather and space is tight, the place name is left out so the temperature, wind and rain always fit.

## Where a card gets its data

A card is connected to the device readings and controls it shows. LaunchControl makes those connections when it creates the card, so in normal use there is nothing to set up: test each new card from the dashboard, and if its values appear and its controls operate the intended equipment, you are done.

To check or change a card’s source, enter edit mode, open the card’s gear menu and choose **Edit**. **Data source** picks the device; **What this card will show** lists each reading with an on/off switch. If a card shows a dash, first check that its device is powered and reporting. If data or controls are still missing, check the selected source. If a control operates the wrong device, correct its source before using it again. The full per-slot binding editor is under **Advanced**, and the [Technical Reference](#technical-reference) lists the usual bindings for each card type.

![Card bindings](images/card-settings01.png)

## Graphs

Solar, Shore Power, Battery + Power, Alternator, temperature, and similar cards can draw a small history graph. The Hub stores the history, so it remains available after the browser is closed and appears consistently on every display. Each panel’s **Graph History** setting, in panel edit mode, selects how many hours its graphs show; time and scale markers are turned on in the same place. The history starts over when the Hub restarts.

## Look and feel

- **Themes —** in panel edit mode, **Theme** offers Midnight, Slate, Gray, and Nightfall. The choice applies to every browser showing this dashboard and is saved at once. The Touch 8 and Mini keep their own look, and each TV display can have its own theme.
- **Units —** US customary or metric, for the whole product: temperatures, volumes and speeds on every card, display and the weather. Chosen during setup and changed under **Settings → System → Units**. Individual Victron devices can override units when needed.
- **Background regions —** optional tinted regions can visually group related cards on a panel.

## Add the dashboard as an app

The dashboard can sit on your phone, tablet or computer like an app, with the LaunchControl icon. Open LaunchControl the way you would normally (locally or through remote). Then:

| **Device** | **How** |
|---|---|
| iPhone / iPad (Safari) | Share button → **Add to Home Screen** → **Add** |
| Android (Chrome) | ⋮ menu → **Add to Home screen** → **Add** (choose **Create shortcut** if asked) |
| Android (Samsung Internet) | ☰ menu → **Add page to** → **Home screen** |
| Windows / Mac / Chromebook (Chrome) | ⋮ menu → **Cast, save and share** → **Create shortcut** (tick **Open as window** for its own window) |
