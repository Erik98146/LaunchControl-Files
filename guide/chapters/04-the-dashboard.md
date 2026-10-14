# The Dashboard

::: lead
The dashboard is a set of live cards organized into panels. Cards update in real time; cards that support control respond when tapped. LaunchControl builds the cards for you when you add equipment; this chapter is about arranging them and adding more.
:::

![A finished dashboard](images/ch04-a-finished-dashboard.png)

## Panels

- **Panel tabs —** switch between groups such as Main, Power, and Climate. Each panel has its own name, icon (or two), and layout. As many tabs as fit are shown across the top; the rest are always one tap away under the **All panels** icon (the grid icon at the end of the tabs).
- **Sub-panels —** each panel can hold up to three sub-panels. Tap a tab's name to open it, or tap the small arrow beside it to choose one of its sub-panels. While a sub-panel is open, its tab reads "Panel › Sub-panel".
- **All panels —** shows every panel and sub-panel in your order, with the one showing marked. Tap any of them to go there. With more than eight panels a search box appears. **Manage panels** at the bottom opens the panel manager.
- **Graph History —** each panel sets the history window used by graphs on that panel.
- **Managing panels —** open **Manage panels** (from All panels, or from edit mode). Each panel has a **⋯** menu: **Edit** (name, icons and parent, with a preview), **Add sub-panel**, **Move…** (put it under another panel or back on top), **Duplicate**, **Move up / down** and **Delete**. Drag a panel by its handle to reorder it; the new order is saved when you press **Done**. Other changes save as soon as you make them, with **Undo** for a few seconds. Deleting a panel tells you first what happens to its cards and sub-panels.
- **Coming back —** reloading the page returns to the panel you were on; opening the dashboard fresh starts on the first panel.
- **Every screen follows —** a change to cards or panels made on one phone or laptop shows up on every other open dashboard, including TVs, within a couple of seconds. A dashboard that is in the middle of editing waits until the editor closes.

## Add cards

Most cards are created when equipment is added (see [Add or Change Equipment](#add-or-change-equipment)). For the rest:

- **Create cards for new devices —** in panel edit mode, under **Dashboard Cards**. It makes a card for every device, from every source, that has none yet, after asking what each switched output is. The setup guide’s **Create dashboard** is the same button.
- **Add a card… —** also under Dashboard Cards. Pick a type from the grouped list (Power, Climate, Water, Lights & switches, Motors, Internet, Utility, Victron) and the card editor opens with its data source to choose. Use it for cards that stand alone: Clock, Weather, Web Link, Sleep Timer, Power Diagram, an extra Lighting card for another part of the coach.
- **Add to dashboard —** on the Devices page, a device’s ⋮ menu makes its default card.

Cards are placed in the panel you are looking at. **Move or copy…** in a card’s gear menu puts it on another panel.

## Arrange the cards

1. **Enter panel edit mode** from the menu at the top right.
2. **Drag cards into position.** The grab handle is in the top left of the card. Cards snap into the dashboard grid.
3. **Open a card’s gear menu** to edit, duplicate, move or remove it.
4. **Exit edit mode.** The layout is stored on the Hub and is used by phones, browsers, and Touch 8 displays.

::: note "Responsive layout"
The dashboard grid adapts to screen size, so the same configuration can be used on desktop, phone, and Touch 8 displays. Narrow screens keep their own card positions: the first time you drag a card on a phone, the phone layout is yours to arrange separately.
:::

## Card gallery

| **Card** | **What it shows / does** |
| --- | --- |
| Thermostat | Room temperature, setpoint, mode, and fan. Available in several layouts. |
| Lighting | Two zone master switches plus four scene buttons. |
| Light Dimmer | One light with on/off and brightness control. |
| Color Light | A Shelly RGBW light: on/off, colour, white and master brightness. |
| Tank | Fresh, gray, black, LPG or fuel tank level, with an optional heater switch. |
| Battery + Power | Battery state of charge, power flow, and history graph. Three sizes: 8×4 Standard, 4×2 Compact (no graphs or detail row; time remaining shown as e.g. "4d 18h"), and 2×2 SoC + Power (just the two numbers). |
| Solar | Solar charging power with history graph. |
| Shore Power | Shore connection status and power. |
| Inverter | Inverter state with on/off control. |
| Alternator | Engine/DC-DC charging status with graph. |
| Water Pump, Switch, Fan, Tank Heat | Simple on/off tiles for one output. |
| Linked Switch | Several outputs switched together by one tap. |
| Door Lock | Lock and unlock with one tap. |
| Awning / Shades / Slide | Extend/retract or up/down controls. |
| Hydronic | Diesel/electric hydronic furnace control. |
| Power Diagram | Live power flow between shore, solar, alternator, battery, inverter, and loads. |
| Sleep Timer | Turns selected devices off at a set time each night. |
| Automation / Macro | Shows one automation's status (tap to arm) or runs one macro. Set them up under Settings → Automations. |
| Clock / Generic | Clock and general-purpose sensor value cards, with optional value alarms. |
| Starlink / Travel Router | Internet equipment status and controls. |
| Weather | Current conditions and a five-day forecast; tap for the next hours. Four sizes, from a full 8×4 card to a one-row strip. Set up under Settings → Integrations → Weather. |
| Web Link | A tile that opens a web page. |

Victron-specific cards appear in the list once the Victron integration is configured.

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

To check or change a card’s source, enter edit mode, open the card’s gear menu and choose **Edit**. **Data source** picks the device; **What this card will show** lists each reading with an on/off switch. A dash on a card, a missing control, or a control that operates the wrong device means the source is wrong — change it here. The full per-slot binding editor is under **Advanced**, and the [Technical Reference](#technical-reference) lists the usual bindings for each card type.

![Card bindings](images/card-settings01.png)

## Graphs

Solar, Battery + Power, Alternator, temperature, and similar cards can draw a small history graph. The Hub stores the history, so it remains available after the browser is closed and appears consistently on every display. The panel Graph History setting selects how much graph history should be shown.

## Look and feel

- **Themes —** choose the dashboard appearance in display settings; the Touch 8 follows the dashboard theme.
- **Units —** US customary or metric, for the whole product: temperatures, volumes and speeds on every card, display and the weather. Chosen during setup and changed under **Settings → System → Units**. Individual Victron devices can override units when needed.
- **Background regions —** optional tinted regions can visually group related cards on a panel.

## Add the dashboard to your home screen

The dashboard can sit on your phone, tablet or computer like an app, with the LaunchControl icon. Open it at the address you want the icon to use: on the coach's Wi-Fi, the Hub's own address; through LaunchControl Remote, your Remote link. A Remote shortcut gets a green cloud on its icon and is named "LC Remote", so you can keep both.

| **Device** | **How** |
|---|---|
| iPhone / iPad (Safari) | Share button → **Add to Home Screen** → **Add** |
| Android (Chrome) | ⋮ menu → **Add to Home screen** → **Add** (choose **Create shortcut** if asked) |
| Android (Samsung Internet) | ☰ menu → **Add page to** → **Home screen** |
| Windows / Mac / Chromebook (Chrome) | ⋮ menu → **Cast, save and share** → **Create shortcut** (tick **Open as window** for its own window) |
