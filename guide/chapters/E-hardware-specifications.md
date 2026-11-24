# Hardware Specifications

::: lead
The hardware inside the Hub and the two displays, and the capacity limits of a LaunchControl system.
:::

## The three devices

| | Hub | Touch 8 | Mini |
| --- | --- | --- | --- |
| Processor | ESP32-S3, dual-core, 240 MHz | ESP32-P4, dual-core RISC-V | ESP32-S3 |
| Memory | 8 MB | 32 MB | 8 MB |
| Storage | 16 MB flash | 32 MB flash | 16 MB flash |
| Display | None | 8-inch IPS touchscreen, 1280×800 | 1.75-inch round AMOLED touchscreen, 466×466 |
| Wi-Fi | 2.4 GHz (802.11 b/g/n) | 2.4 GHz Wi-Fi 6, through an onboard radio module | 2.4 GHz |
| Bluetooth | Bluetooth LE 5, off until turned on in Settings | — | — |
| Connects to the RV by | RV-C (CAN) | Wi-Fi to the Hub | Wi-Fi to the Hub |
| Power | 12–24 V DC, or USB-C; never both at once | USB-C | USB-C |
| Software update | From the Hub’s Settings, with automatic fallback to the previous version | Through the Hub, with the same fallback | Through the Hub, with the same fallback |

## Hub connections

| | |
| --- | --- |
| RV-C | CAN at 250 kbps, electrically isolated and surge protected |
| Termination | A 120 Ω terminating resistor is built in and switched by a jumper. It is off as shipped; turn it on only if the Hub is at a physical end of the RV-C network |
| RS-485 | An isolated port is present and reserved for future use |
| Hub hotspot | LaunchControl-Hub-XXXX at 192.168.4.1, for up to 8 devices at a time |
| Wi-Fi | The Hub runs its hotspot and joins your router at the same time |
| Clock | Kept automatically from the internet, the RV network, a GPS, or an open browser. The Hub has no clock battery, so the time is set again after each power-up |

::: warning "One power source"
Power the Hub from the DC terminals or from USB-C, never from both at the same time. Doing so can damage it.
:::

## System limits

| Item | Limit |
| --- | --- |
| Dashboard cards | 72 |
| Panels | 6, each with up to 5 sub-panels |
| Cards that keep a history graph on the Hub | 16 |
| Saved Wi-Fi networks | 8 |
| Touch 8 and Mini displays | 8 |
| Automations | 8, with up to 4 actions on trigger and 4 on release |
| Macros | 4, with up to 8 actions each |
| Lighting Scenes cards | 8, each with 2 zones and 4 scenes of up to 32 lights |
| Shades moved by one Shades card | 12 |
| Thermostats with a daily schedule | 4 |
| Tanks with a calibration table | 4, with up to 32 entries each |
| Victron devices through a GX device | 8 |
| Victron Bluetooth devices | 8 |
| Bluetooth sensors (Ruuvi, SwitchBot, BTHome) | 16 |
| Bluetooth propane tank sensors | 8 |
| SeeLevel tank monitors | 4 |
| PowerMon battery monitors | 4 |
| Shelly BLU button remotes | 4 |
| MQTT devices added by hand | 48, with 6 fields each |
| Devices connected to the built-in MQTT broker | 16 |

## Software versions

Each device reports its own version, in the form v*major*.*minor*.*build*, under **Settings → Status** and on the software update page. The Hub, Touch 8, and Mini are numbered separately and released together as a tested set.
