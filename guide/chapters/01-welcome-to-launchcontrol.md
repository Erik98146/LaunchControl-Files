<!-- part: Getting started -->
# Welcome to LaunchControl

::: lead
See your RV’s battery and tank levels, switch lights, adjust the temperature, and manage your equipment from one dashboard. You can get started without learning how the RV’s control network works.
:::

LaunchControl runs locally in your RV. Normal monitoring and control need no internet connection, cloud account or subscription. Add dedicated displays, remote access and other equipment whenever you are ready.

## Start here

- **New Hub?** Follow [Quick Start](#quick-start) to get your first working dashboard.
- **Already set up?** See [Controls](#controls) for everyday use.
- **Make it yours.** [The Dashboard](#the-dashboard) explains how to arrange your controls; [Connecting Additional Equipment](#connecting-additional-equipment) explains optional integrations.
- **Need help?** Start with [Troubleshooting](#troubleshooting).

You do not need to read this entire guide. The Getting started chapters are the installation path; the rest are available as you need them. Expand optional technical details only when they are useful to you.

## Four useful words

| Word | Meaning |
| --- | --- |
| Hub | The small controller that connects your RV equipment and serves the dashboard. |
| Device | A piece of equipment or function, such as a light or tank sensor. |
| Card | A tile that displays a reading or controls a device. |
| Panel | A group of cards, such as Main, Power or Climate. The dashboard contains your panels. |

The Hub and a browser are a complete system. The Touch 8 and Mini displays are optional. Your equipment names and panel names are up to you.

## Find a specific task

| I want to… | Go to |
| --- | --- |
| Set up a new Hub | [Quick Start](#quick-start) · [Set Up Your Hub](#set-up-your-hub) |
| Add equipment or identify a switch | [Add or Change Equipment](#add-or-change-equipment) · [Connecting Additional Equipment](#connecting-additional-equipment) |
| Use lights, climate, tanks, or timers | [Controls](#controls) |
| Use a Touch 8 or Mini | [Touch 8](#the-touch-8-display) · [Mini](#the-mini-display) |
| Arrange cards, panels, or my phone layout | [The Dashboard](#the-dashboard) |
| Create a rule, macro, or notification | [Automations & Macros](#automations-macros) · [Alerts](#alerts) |
| Use a TV or wall tablet | [TV & Wall Displays](#tv-wall-displays) |
| Set up Siri or a shortcut | [Siri & Shortcuts](#siri-shortcuts) |
| Check or control my RV from elsewhere | [Remote Access](#remote-access) |
| Ask an AI assistant about my RV | [AI Assistant](#ai-assistant) |
| Back up, restore, or change a setting | [Backups, Restores & Resets](#backups-restores-resets) · [Settings Reference](#settings-reference) |
| Update software | [Software Updates](#software-updates) |
| Fix a problem | [Troubleshooting](#troubleshooting) |
| See what one card does | [Card Reference](#card-reference) |
| Check whether my equipment is supported | [Supported Equipment](#supported-equipment) |
| Look up bindings, MQTT topics, or API parameters | [Technical Reference](#technical-reference) · [MQTT, ESPHome & Home Assistant](#mqtt-esphome-home-assistant) |

You choose the names and organization of your equipment and panels. Names in this guide are examples.


## System overview

::: technical "Components, connections and browser compatibility"
**More terminology**

| Word | Meaning |
| --- | --- |
| **Device** | A piece of equipment or a function in your RV: a light, a pump, a tank sensor. |
| **Card** | The tile on the dashboard that shows or controls a device. |
| **Panel** | A tab on the dashboard that groups cards. |
| **Hub hotspot** | The Hub's own Wi-Fi network, named LaunchControl-Hub-XXXX. |
| **Setup guide** | The seven-step checklist on the dashboard that walks you through a new installation. |
| **Alert list** | The list behind the warning triangle at the top of the dashboard. |

**Components**

| Component | What it does |
| --- | --- |
| LaunchControl Hub | The central controller. It connects to the RV's control network, communicates with supported equipment, and serves the dashboard. |
| Web dashboard | The full browser-based interface for monitoring, control, and all system configuration. |
| Touch 8 display | An 8-inch wall-mount touchscreen that mirrors the dashboard with full touch control. |
| Mini display | A 1.75-inch round touchscreen for glanceable status and selected everyday controls. |

The displays are optional. A Hub plus the web dashboard is a complete LaunchControl system.


**How the pieces fit together**

The Hub has four jobs:

- **RV-C connection —** the Hub connects physically to the RV's control network and reads or sends RV-C messages.
- **Device integration —** the Hub connects to other equipment such as Victron devices, Shelly devices, and Bluetooth sensors.
- **Hub hotspot —** the Hub creates its own Wi-Fi network for Touch 8, Mini, and direct phone or tablet access. The Hub can also join your existing Wi-Fi router so phones and computers on that network can open the dashboard without changing Wi-Fi networks.
- **LaunchControl Remote —** with the Hub on a network that has internet, the same dashboard is available from anywhere through remote.launchcontrol.tech, with no app and no router configuration. Every new Hub includes 90 days; see [Remote Access](#remote-access).

RV-C uses CAN at the physical layer. The Hub listens to the bus, maintains a live model of the RV's state, and pushes changes to dashboards and displays over WebSockets. Touch 8 and Mini displays do not connect to RV-C directly; they communicate through the Hub.

**Browser compatibility**

Any current phone, tablet, or computer browser works: Safari, Chrome, Edge, Firefox, and Samsung Internet. Older iPads are supported back to iOS 12, so a retired tablet can serve as a wall display. No app is installed; see [The Dashboard](#the-dashboard) to put the dashboard on your home screen like one.


The Hub and displays start within a few seconds. Network connections, a Victron Cerbo GX, and the RV router may take longer. The Hub tolerates power disconnections; no shutdown procedure is required.
:::
