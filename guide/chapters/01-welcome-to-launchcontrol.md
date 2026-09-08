# Welcome to LaunchControl

::: lead
LaunchControl gives you one place to monitor and control the systems in your RV: lights, climate, tanks, batteries, solar, inverter, awnings, internet equipment, and more. You can use the web dashboard from a phone, tablet, or computer, and add dedicated Touch 8 or Mini displays wherever you want always-available control.
:::

LaunchControl runs locally in your RV. There is no cloud account, subscription, or internet requirement for normal monitoring and control.

LaunchControl HUB and the panels boot in just a couple seconds. Network connections, rebooting Victron Cerbo or rebooting the RV router may take longer. The hub is tolerant of power disconnects so there is not a shutdown procedure.

## What’s in the system

| Component | What it does |
| --- | --- |
| LaunchControl Hub | The central controller. It connects to the coach RV-C network, communicates with supported equipment integrations, and serves the dashboard. |
| Web Dashboard | The full browser-based interface for monitoring, control, and all system configuration. |
| Touch 8 Display | An 8-inch wall-mount touchscreen that mirrors the dashboard with full touch control. |
| Mini Display | A 1.75-inch round touchscreen for glanceable status and selected everyday controls. |

The displays are optional. A Hub plus the web dashboard is a complete LaunchControl system.

## How the pieces fit together

The Hub has three jobs:

- **RV-C connection —** the Hub connects physically to the coach control bus and reads or sends RV-C messages.
- **Device integration —** the Hub connects to other devices such as Victron equipment, Shelly devices and more through MQTT.
- **LaunchControl network —** the Hub creates its own Wi-Fi network for Touch 8, Mini, and direct phone/tablet access. The Hub can also join your existing Wi-Fi router so phones and computers on that network can open the dashboard without changing Wi-Fi networks.

::: technical
RV-C uses CAN at the physical layer. The Hub listens to the bus, maintains a live model of the coach state, and pushes changes to dashboards and displays over WebSockets. Touch 8 and Mini displays do not connect to RV-C directly; they communicate through the Hub.
:::

## How to use this guide

Chapter 2 is the normal installation and setup path. Follow it in order. The rest of the guide explains customizations, devices, dashboard building, controls, displays, settings, security, updates, and troubleshooting.

Deeper implementation information appears in shaded “Technical detail (optional)” boxes and in Chapter 14. You can skip those sections during normal setup.
