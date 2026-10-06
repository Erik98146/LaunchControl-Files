# Controls

![Lighting master controls](images/ch05-lighting-master-controls.png)

## Lighting Masters & Scenes

The Lighting card provides whole-coach lighting controls:

- **Two zone masters —** tap to switch each group on or off. Press and hold a master to bring that group to full brightness.
- **Four scenes —** one-tap lighting scenes such as Evening or Movie. Set the lights as desired, then press and hold a scene to save. Scene names and icons may be customized in the card editor.
- **Automation badge —** run lighting on a schedule from the card settings. Lights can be controlled by time of day or by using solar panels as a sensor.

The Lighting card setup lets you choose which lights are controlled by Zone 1 master, Zone 2 master, and lighting scenes. Each Lighting card maintains its own list of lights, allowing you to create multiple cards for different zones throughout the coach.

When the master is turned off, LaunchControl remembers the state of each light. Turning the master back on restores the lights to their previous settings. To turn all lights on at 100%, press and hold the On button.

## Lighting Dimmers

The Light Dimmer card provides controls for an individual light. Dimmers for small cards can be accessed by pressing and holing the card. Lights remember their last value when turned back on. This setting can be changed in the device setup for each light.

## Climate

The Thermostat card is available as a wide card, a large dial, or a compact tile. The dial shows current room temperature and the selected setpoint. Tap the compact tile to open the full mode, fan, and setpoint controls. 

### Schedules

A thermostat can follow four daily periods: Awake, Away, Return, and Sleep. Each period has its own time, mode, and setpoint. The clock control switches between following the schedule and manual hold.

::: note "Clock required"
Schedules only run when the Hub has valid time. Choose a time source under Settings → System → Date & time if a schedule will not enable.
:::

## Tanks

Fluid tanks with heaters that have been bound to a card may be toggled by pressing and holding the card. 

Irregularly shaped tanks may produce sensor readings that do not accurately represent the amount of liquid they contain. The optional Geometry Lookup calibration corrects this by mapping sensor readings to the tank’s actual contents. To create a calibration table, open the tank device for editing and enable geometry. Fill the tank in measured increments (like 1 or 2 gal at a time) usig a flow meter and enter the values as you go. LaunchControl uses these calibration points to calculate the tank’s actual percentage full and estimated amount remaining. Volume is displayed in gallons or liters according to the Hub’s system-wide units setting.

## Awnings & Shades

Awning and Shades cards have two direction buttons. Depending on the device, a button is either hold-to-move (the motor runs while you hold it) or press-to-command (window-shade controllers start on a press and stop on the next press). The card settings say which.

**Move several shades at once —** when you add or edit a Shades card yourself, the card editor lists every other shade on the Hub under **Also move these shades**. Tick the ones that should follow. One press then moves the card's own shade and every ticked shade, from the dashboard or a Touch display. Cards created automatically are one shade each; edit a card to group them.

## Graphs

Solar, Shore Power, Alternator, Generator, Battery and Net Power cards have graphs that can be configured for time and scal markers from the panel edit mode.

## Device Off-timers

Many on/off cards can start a device with a countdown timer to automatically turn off the device when the time expires. Press and hold a device to start the timer. Tap the device again to cancel the timer (device remains on).

## Sleep Timer

The Sleep Timer card turns selected devices off at the same time every night. Choose the devices, set the time, and arm the timer.

::: note "Timer uses"
Device timers are useful for short duration use, when you don’t want to forget to turn off a water pump or inverter, for example. The sleep timer is especially useful when you are off-grid and don’t want to accidentally run power hungry devices all night.
:::
