<!-- part: Start here -->
# Welcome to LaunchControl

::: lead
LaunchControl gives you one place to monitor and control the systems in your RV: lights, climate, tanks, batteries, solar, inverter, awnings, internet equipment, and more. You can use the web dashboard from a phone, tablet, or computer, and add dedicated Touch 8 or Mini displays wherever you want always-available control.
:::

LaunchControl runs locally in your RV. There is no cloud account, subscription, or internet requirement for normal monitoring and control.

The Hub and displays start within a few seconds. Network connections, a Victron Cerbo GX, and the RV router may take longer. The Hub tolerates power disconnections; no shutdown procedure is required.

## Start with your task

| I want to… | Go to |
| --- | --- |
| Set up a new Hub | [Set Up Your Hub](#set-up-your-hub) |
| Add equipment or identify a switch | [Add or Change Equipment](#add-or-change-equipment) |
| Arrange cards, panels, or my phone layout | [The Dashboard](#the-dashboard) |
| Use lights, climate, or timers | [Controls](#controls) |
| Use a Touch 8 or Mini | [Touch 8](#the-touch-8-display) · [Mini](#the-mini-display) |
| Check or control my RV from elsewhere | [Remote Access](#remote-access) |
| Create a rule, macro, or notification | [Automations & Macros](#guide-automations) · [Alerts](#alerts) |
| Use a TV or wall tablet | [TV & Wall Displays](#guide-tv-displays) |
| Set up Siri or a shortcut | [Voice Control and Shortcuts](#voice-control-shortcuts-siri-and-other-controllers-api) |
| Back up, restore, or change a setting | [Settings Reference](#settings-reference) |
| Update software | [Software Updates](#software-updates) |
| Fix a problem | [Troubleshooting](#troubleshooting) |
| Look up bindings, protocols, or API parameters | [Technical Reference](#technical-reference) |

You choose the names and organization of your equipment and panels. Names in this guide are examples.

**Three useful terms:** a **device** is equipment or a function in your RV; a **card** shows or controls it; a **panel** groups cards on the dashboard.

## What’s in the system

| Component | What it does |
| --- | --- |
| LaunchControl Hub | The central controller. It connects to the coach RV-C network, communicates with supported equipment integrations, and serves the dashboard. |
| Web Dashboard | The full browser-based interface for monitoring, control, and all system configuration. |
| Touch 8 Display | An 8-inch wall-mount touchscreen that mirrors the dashboard with full touch control. |
| Mini Display | A 1.75-inch round touchscreen for glanceable status and selected everyday controls. |

The displays are optional. A Hub plus the web dashboard is a complete LaunchControl system.

## How the pieces fit together

The Hub has four jobs:

- **RV-C connection —** the Hub connects physically to the coach control bus and reads or sends RV-C messages.
- **Device integration —** the Hub connects to other devices such as Victron equipment, Shelly devices and more through MQTT.
- **LaunchControl network —** the Hub creates its own Wi-Fi network for Touch 8, Mini, and direct phone/tablet access. The Hub can also join your existing Wi-Fi router so phones and computers on that network can open the dashboard without changing Wi-Fi networks.
- **LaunchControl Remote —** with the Hub on a network that has internet, the same dashboard is available from anywhere through remote.launchcontrol.tech, with no app and no router configuration. Every new Hub includes 90 days; see [Remote Access](#remote-access).

::: technical
RV-C uses CAN at the physical layer. The Hub listens to the bus, maintains a live model of the coach state, and pushes changes to dashboards and displays over WebSockets. Touch 8 and Mini displays do not connect to RV-C directly; they communicate through the Hub.
:::

## How to use this guide

The guide is in five parts. **Start here** is the installation and setup path, in order; **Using LaunchControl** covers everyday operation; **Customize** the settings; **Something isn’t working** is organized by symptom; and the **Advanced** part holds the technical reference.

Deeper implementation information appears in shaded “Technical detail (optional)” boxes and in the [Technical Reference](#technical-reference). You can skip those sections during normal setup.
