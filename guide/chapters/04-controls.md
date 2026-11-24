<!-- part: Everyday use -->
# Controls

::: lead
Everyday control happens on the dashboard cards. This chapter covers the ones you will use most, grouped the way the coach is used. [Card Reference](#card-reference) describes every card, its sizes, and its settings.
:::

Two gestures do almost everything:

- **Tap** switches a device on or off, or opens a card’s controls.
- **Press and hold** opens extra controls or starts an off-timer, depending on the card.

A card that shows a dash (—) has no reading yet. The dashboard always shows what the equipment reports, so a control that did not take effect returns to the real state within a few seconds.

## Lights

### One light

A **Light Dimmer** card controls a single light. On the wide sizes, tap the bulb to switch the light on or off, drag the slider to dim it, and press and hold the bulb for full brightness. On the small 2×2 size, tap switches the light and press and hold opens the slider. A light returns to its last level when switched back on; this can be changed for each light on the Devices page.

A **Color Light** card works the same way: tap for on or off, press and hold for the color wheel and the **Color**, **White**, and **Master** sliders. A **Panel Backlight** card steps through Off, On, and Dim with each tap.

### Groups of lights and scenes

The **Lighting Scenes** card controls groups of lights from one place:

- **Two zone masters —** an On and an Off button for each of two groups of lights, such as inside and outside.
- **Four scenes —** one-tap lighting presets such as Evening or Movie. Each scene remembers the level of every light in it.

![The 8×2 Standard layout](images/ch05-lighting-master-controls.png "The 8×2 Standard layout: a zone master either side of the four scenes")

Using the zone masters:

- **On —** tap to switch the zone's lights on.
- **Off —** tap to switch them all off.
- **Full brightness —** press and hold **On** to bring every light in the zone to 100%.

The buttons also show what the lights are doing: **On** is lit while any light in the zone is on, and **Off** is lit when all of them are off. This stays correct when lights are switched at a wall switch.

Saving and using scenes:

1. **Set the lights.** Use the dimmer cards, the masters, or the wall switches to get the lights the way you want them.
2. **Press and hold a scene button.** On the dashboard, confirm **Save**. On a Touch 8 the scene is saved as soon as you hold the button.
3. **Tap the button to recall it.** Every light in the scene goes to the level it had when you saved, including lights that were off.

A scene that has never been saved does nothing when tapped. The last scene recalled stays highlighted until you recall another or press a master. Scenes can also be run from a macro or automation, from a Shelly BLU button remote, and by name with Siri and Shortcuts.

To choose which lights belong to each zone and scene, name the buttons, or change the card’s layout, see **Lighting Scenes** in the [Card Reference](#card-reference).

### Lights on a schedule

On the 8×2 Standard layout, the clock badge in the top right corner opens **Lighting Automation**. It can switch lights on and off by time of day, or use a solar panel as a light sensor to switch them at dusk and dawn. The badge is yellow while automation is on.

## Climate

The **Climate** card shows the room temperature and what the system is doing: **Heating to**, **Cooling to**, **Fan only**, or **System Off**. On the dial layout, the white dot is the room temperature and the amber tick is the setpoint.

- **Change the temperature —** use the arrows; each press is one degree.
- **Change the mode or fan —** open the controls: tap the cog on the wide card, the upper half of the dial, or anywhere on the compact tile. Choose **A/C**, **Heat**, or **Off**, and fan **Hi**, **Lo**, or **Auto**.

### Schedules

A thermostat can follow four daily periods: Awake, Away, Return, and Sleep. Tap the clock icon on the card to open **Climate Schedule**. Give each period a time, a mode, and a temperature; a period with no time is skipped. Turn on **Follow this schedule** to start it. The clock icon is amber while the schedule is followed and gray when you are setting the temperature by hand.

::: note "Clock required"
Schedules only run when the Hub has valid time. The Hub keeps its clock automatically — internet time when it has it, otherwise the RV network, a GPS, or the browser that is open. If a schedule will not turn on, see Settings → System → Date & time.
:::

### Roof fans and hydronic heat

Tap a **Roof Fan** card to choose a speed — High, Medium, Low, or Off — and to open or close the dome. Choosing a speed opens the dome; closing the dome stops the fan.

A **Hydronic** card runs a diesel and electric hydronic furnace: choose Off, Diesel, Electric, or Both, and set the target temperature.

## Power

- **Battery + Power —** state of charge, time remaining, and net power, with **Charging battery** or **Using battery power**.
- **Inverter —** tap to switch the inverter on or off; press and hold to start an off-timer. The status line shows the power being supplied, **Charger Only**, or **Off**.
- **Shore Power —** the power being drawn, or **Connected**, **Disconnected**, or **On generator**. Tap it to set the **Current limit** with − and +, so the coach does not trip a small campground breaker, and to enable or disable the charger.
- **Solar —** solar power and today’s yield. With a Victron solar charger, tap for the last seven days.
- **Alternator** and **Battery Charger —** what the engine or a charger is delivering. Tap the Alternator card for detail.
- **Power Diagram —** one picture of power flowing between shore, solar, alternator, battery, inverter, and loads, with the shore limit and inverter controls on it.

## Water and tanks

A **Tank** card shows the level as a percentage, and the amount remaining once the tank’s size is set (see [Add or Change Equipment](#add-or-change-equipment)). When a tank has a heater, press and hold the card to switch the heater; the card shows an orange outline and **HEAT** while it is on.

A tank can warn you as it fills or empties. Open the card’s gear menu, choose **Edit**, and turn on **Level alarm** with a **Warning at** and an **Alarm at** level. The card is outlined amber at the warning level and blinks red at the alarm level, on the dashboard and on the Touch 8. Waste tanks alarm as they fill; fresh water, LPG, and fuel alarm as they empty. The outline does not send a message; to be notified, add an automation with **Send alert** (see [Alerts](#alerts)).

Tap a **Water Pump** card to switch the pump; press and hold to start an off-timer.

## Awnings, shades, slides, and levelers

Tap an Awning, Shades, Slide, or Leveler card to open its two direction buttons. The card says which way it works:

- **Hold a direction to move —** the motor runs only while you hold the button. Slides and levelers always work this way.
- **Press a direction to command —** window-shade controllers start on one press and stop on the next.

Awnings, slides, and levelers do not operate through LaunchControl Remote, because nobody can see what is around them; their cards say so. Shades still work.

**Move several shades at once —** edit a Shades card and tick the other shades under **Also move these shades**. One press then moves the card’s own shade and every ticked shade, from the dashboard or a Touch 8.

A **TV Lift** card raises or lowers the lift with one tap.

## Door locks

Tap a **Door Lock** card to lock or unlock. The card shows **Locked** or **Unlocked**; when the lock has not reported its state yet, it shows a dash and asks **Lock or unlock?** when tapped.

## Switches and fans

A **Generic Switch**, **Fan**, or **Tank Heat** card switches one output with a tap. A **Linked Switch** card switches several outputs together; it reads **Mixed** when they disagree, and a tap then turns them all off.

## Internet

Tap a **Starlink** card to switch the dish’s power; press and hold to start an off-timer. Tap a **Travel Router** card to see the connection, join a Wi-Fi network, or run a speed test.

## Timers

### Device off-timers

Inverter, Victron MultiPlus, Water Pump, and Starlink cards can switch themselves off after a countdown. Press and hold the card to start the timer; the device turns on if it was off, and the card shows the time remaining. Tap the card again to cancel the timer; the device stays on. A timer is not kept through a Hub restart.

### Sleep Timer

The **Sleep Timer** card turns selected devices off at the same time every night. Choose which devices it switches — the inverter, the water pump, Starlink — then tap the time to set it, and tap the top of the card to arm or disarm it.

::: note "Timer uses"
Device timers suit short jobs, so you do not forget to turn off a water pump or inverter. The Sleep Timer is especially useful off-grid, so power-hungry devices do not run all night by accident.
:::
