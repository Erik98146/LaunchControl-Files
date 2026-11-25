# Automations & Macros

::: lead
Automations let the coach react to changing conditions. Macros group several actions behind one tap. Both are managed under **Settings → Automations**; a dashboard card is optional.
:::

| Use… | When you want… |
| --- | --- |
| **Automation** | A sensor reading to trigger actions by itself |
| **Macro** | One tap or button press to run a sequence of actions |
| **Send alert** action | A message when a rule triggers or releases, or a macro runs; see [Alerts](#alerts) |

The Hub holds up to eight automations and four macros. They run on the Hub itself, with no browser open and no internet.

## The Automations page

Settings → Automations lists every automation and macro with its status, the alert channels it uses, whether it has a dashboard card, and an enable switch (or a **Run** button for a macro). Click a row to edit it, or use **New Automation** / **New Macro**. Below the list are **Proactive alerts** and the notification services; see [Alerts](#alerts).

## Try a low-water alert

1. **Create a rule.** Open Settings → Automations → **New Automation** and choose the fresh-water tank level as the sensor.
2. **Set the trigger.** Choose below 20%, with a release above 25% so the rule can reset after refilling. These are example values.
3. **Add an action.** Choose **Send alert**, write a message, and select **On-screen**. Save and enable the rule.
4. **Test it.** Observe a safe threshold crossing and confirm that the alert arrives. Review the startup behavior below if the tank is already low.

::: warning "Test before relying on an automation"
Verify the sensor, actions, release behavior and delivery method. Automations are not a substitute for factory safety systems. Never use a macro, automation or generic switch to bypass restrictions on moving equipment.
:::

## Automation rules

An automation rule watches one sensor and acts when the reading crosses a threshold.

- **Sensor —** press **Choose sensor** and expand a device to pick one of its readings: battery percentage, a tank level, a temperature, shore voltage, water leak sensor. Any value a dashboard card can show can be watched.
- **Trigger —** above or below a value, optionally held for a period you choose so a short excursion does not fire the rule.
- **Release —** a second value where the rule resets. The gap between trigger and release prevents rapid on/off cycling.
- **Actions —** up to four actions on trigger and four on release.

A template can fill in the condition as a starting point: **Battery guard (SoC %)** or **Shore power (AC volts)**. It does not pick the sensor, and every value stays editable.

![Automation example.](images/ch06-automation-example.png)

### Actions

| Action | What it does |
| --- | --- |
| **Device on/off** | Switches the inverter, water pump, or Starlink |
| **Switch a card** | Turns any switchable card on or off |
| **Toggle a card** | Switches a card to the opposite of how it is now |
| **Lighting master** | Switches a lighting zone on or off |
| **Lighting scene** | Recalls one of a Lighting Scenes card’s scenes |
| **Climate set** | Sets a thermostat to Off, A/C, Heat, or Fan Only, with a temperature |
| **Panel backlight** | Sets switch-panel backlights to off, dim, or on |
| **Send alert** | Sends a message; see [Alerts](#alerts) |

### What happens at start

Normally, restarting the Hub, editing a rule or enabling it does not run its actions again. The rule uses the current reading as its starting state. If the reading is already past the threshold at that moment, the list shows **Triggered · at start, not fired** — nothing runs until the value crosses back and trips again. This stops a restart from repeating actions that already happened.

Two options change that for rules that protect the coach:

- **Act if already triggered at start —** a first reading that is already past the trigger runs the actions instead of waiting for the next crossing. Use it when missing the event matters more than repeating it.
- **Latch until reset —** once triggered, the rule stays triggered, through a restart too, and the release actions never run until you press **Reset**. The list and the rule’s dashboard card show **Latched**; tap the card, or press **Reset** in the list, to clear it. Reset runs nothing: switch things back on yourself. It is refused while the sensor still reads past the threshold.

## A leak shut-off example

This example closes the water supply and tells you when a leak sensor gets wet. It needs a leak sensor and something to switch: a water valve, the water pump, or both. See **Leak sensors and water valves** in [Connecting Additional Equipment](#connecting-additional-equipment).

1. **Create the automation.** Settings → Automations → **New Automation**, and choose the leak sensor’s state as the **Sensor**.
2. **Set the trigger to above 0.5.** A leak sensor reads 1 when wet and 0 when dry.
3. **Add the trigger actions.** **Switch a card** → the valve’s card → **Off** closes the valve. **Device on/off** → **Water Pump** → off stops the pump. **Send alert** tells you about it.
4. **Tick both safety options.** **Act if already triggered at start** covers a leak the sensor reports just after a Hub restart. **Latch until reset** keeps the water off after the sensor dries.
5. **Test it** by wetting the sensor, before you rely on it.

After the leak is fixed and the sensor is dry, reset the rule, then open the valve and switch the pump back on yourself.

## Macros

A macro runs up to eight actions in order. For example, an Away macro might switch off the water pump and lower the thermostat; a Return macro can reverse those actions. Run it from the **Run** button in the list, from its dashboard card, from a Shelly button, or by voice.

A macro can use every action above, plus two of its own:

- **Automation on/off —** enables a disabled automation rule, or disables an enabled one.
- **Wait (delay) —** pauses for 1 to 3600 seconds before the next action, for example to let the inverter come up before the water pump starts. The wait runs on the Hub, so the macro finishes even if you close the page. Each wait uses one of the eight action slots. Running the macro again while it is waiting starts it over from the first action; editing or deleting the macro cancels the wait.

## Dashboard cards

Cards are optional. In panel edit mode, use **Add a card…** under **Dashboard Cards**, choose **Automation** or **Macro**, then pick the rule or macro. An Automation card shows whether the rule is armed and whether it is triggered; tapping it enables or disables the rule, or resets it when it is latched. A Macro card runs the macro on a tap. Each automation can have one card. Removing the card keeps the automation; deleting the automation removes its card.
