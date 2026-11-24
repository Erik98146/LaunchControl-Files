<!-- part: Start here -->
# Welcome to LaunchControl

::: lead
LaunchControl gives you one place to monitor and control the systems in your RV: lights, climate, tanks, batteries, solar, inverter, awnings, internet equipment, and more. You can use the web dashboard from a phone, tablet, or computer, and add dedicated Touch 8 or Mini displays wherever you want always-available control.
:::

LaunchControl runs locally in your RV. Normal monitoring and control need no cloud account, no subscription, and no internet connection.

The Hub and displays start within a few seconds. Network connections, a Victron Cerbo GX, and the RV router may take longer. The Hub tolerates power disconnections; no shutdown procedure is required.

## Start with your task

| I want to… | Go to |
| --- | --- |
| Set up a new Hub | [Set Up Your Hub](#set-up-your-hub) |
| Add equipment or identify a switch | [Add or Change Equipment](#add-or-change-equipment) |
| Use lights, climate, tanks, or timers | [Controls](#controls) |
| Use a Touch 8 or Mini | [Touch 8](#the-touch-8-display) · [Mini](#the-mini-display) |
| Arrange cards, panels, or my phone layout | [The Dashboard](#the-dashboard) |
| Create a rule, macro, or notification | [Automations & Macros](#automations-macros) · [Alerts](#alerts) |
| Use a TV or wall tablet | [TV & Wall Displays](#tv-wall-displays) |
| Set up Siri or a shortcut | [Siri, Shortcuts & API](#siri-shortcuts-api) |
| Check or control my RV from elsewhere | [Remote Access](#remote-access) |
| Ask an AI assistant about my RV | [AI Assistant](#ai-assistant) |
| Back up, restore, or change a setting | [Settings Reference](#settings-reference) |
| Update software | [Software Updates](#software-updates) |
| Fix a problem | [Troubleshooting](#troubleshooting) |
| See what one card does | [Card Reference](#card-reference) |
| Check whether my equipment is supported | [Supported Equipment](#supported-equipment) |
| Look up bindings, MQTT topics, or API parameters | [Technical Reference](#technical-reference) · [MQTT, ESPHome & Home Assistant](#mqtt-esphome-home-assistant) |

You choose the names and organization of your equipment and panels. Names in this guide are examples.

## Words this guide uses

| Word | Meaning |
| --- | --- |
| **Device** | A piece of equipment or a function in your RV: a light, a pump, a tank sensor. |
| **Card** | The tile on the dashboard that shows or controls a device. |
| **Panel** | A tab on the dashboard that groups cards. |
| **Hub hotspot** | The Hub's own Wi-Fi network, named LaunchControl-Hub-XXXX. |
| **Setup guide** | The seven-step checklist on the dashboard that walks you through a new installation. |
| **Alert list** | The list behind the warning triangle at the top of the dashboard. |

## What’s in the system

| Component | What it does |
| --- | --- |
| LaunchControl Hub | The central controller. It connects to the RV's control network, communicates with supported equipment, and serves the dashboard. |
| Web dashboard | The full browser-based interface for monitoring, control, and all system configuration. |
| Touch 8 display | An 8-inch wall-mount touchscreen that mirrors the dashboard with full touch control. |
| Mini display | A 1.75-inch round touchscreen for glanceable status and selected everyday controls. |

The displays are optional. A Hub plus the web dashboard is a complete LaunchControl system.

## How the pieces fit together

The Hub has four jobs:

- **RV-C connection —** the Hub connects physically to the RV's control network and reads or sends RV-C messages.
- **Device integration —** the Hub connects to other equipment such as Victron devices, Shelly devices, and Bluetooth sensors.
- **Hub hotspot —** the Hub creates its own Wi-Fi network for Touch 8, Mini, and direct phone or tablet access. The Hub can also join your existing Wi-Fi router so phones and computers on that network can open the dashboard without changing Wi-Fi networks.
- **LaunchControl Remote —** with the Hub on a network that has internet, the same dashboard is available from anywhere through remote.launchcontrol.tech, with no app and no router configuration. Every new Hub includes 90 days; see [Remote Access](#remote-access).

::: technical
RV-C uses CAN at the physical layer. The Hub listens to the bus, maintains a live model of the RV's state, and pushes changes to dashboards and displays over WebSockets. Touch 8 and Mini displays do not connect to RV-C directly; they communicate through the Hub.
:::

## What you can use to open the dashboard

Any current phone, tablet, or computer browser works: Safari, Chrome, Edge, Firefox, and Samsung Internet. Older iPads are supported back to iOS 12, so a retired tablet can serve as a wall display. No app is installed; see [The Dashboard](#the-dashboard) to put the dashboard on your home screen like one.

## How to use this guide

The guide is in seven parts:

- **Start here** is the installation and setup path, in order.
- **Everyday use** covers the controls and the two displays.
- **Make it yours** covers arranging the dashboard, automations, alerts, TV displays, and voice control.
- **Remote access** covers LaunchControl Remote and the AI assistant that works through it.
- **Maintain** covers settings, software updates, and security.
- **Something isn’t working** is organized by symptom.
- **Reference** holds the technical reference and the appendices: card-by-card details, Shelly and MQTT setup, supported equipment, hardware specifications, and notes for particular coaches.

Deeper implementation information appears in shaded “Technical detail (optional)” boxes and in the Reference part. You can skip those during normal setup.
