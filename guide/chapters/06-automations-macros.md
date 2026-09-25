# Automations & Macros

::: lead
Automations let the coach react to changing conditions. Macros group several actions behind one tap. Both are managed under **Settings → Automations**; a dashboard card is optional.
:::

## The Automations page

Settings → Automations lists every automation rule and macro with its status, the alert channels it uses, whether it has a dashboard card, and an enable switch (or a **Run** button for a macro). Click a row to edit it, or use **New Automation** / **New Macro**. The Push Alerts and SMS Alerts settings sit below the list.

## Automation rules

An automation rule watches one sensor and acts when the reading crosses a threshold.

- **Sensor —** press **Choose sensor** and expand a device to pick one of its readings: battery percentage, a tank level, a temperature, shore voltage. Any value a dashboard card can show can be watched.
- **Trigger —** above or below a value, optionally held for a selected period so a short excursion does not fire the rule.
- **Release —** a second value where the rule resets. The gap between trigger and release prevents rapid on/off cycling.
- **Actions —** up to four actions on trigger and four on release: device switching, lighting masters, thermostat changes, and **Send alert** (see Alerts).

Common templates can pre-fill the condition.

![Automation example.](images/ch06-automation-example.png)

::: note "Power-up behavior"
When the Hub starts, or when an automation is edited or re-enabled, the rule adopts the current state without firing. If the reading is already past the threshold at that moment, the list shows **Triggered · at start, not fired** — nothing runs until the value crosses back and trips again.
:::

## Macros

A macro runs up to eight actions in order. For example, an Away macro might switch off the water pump and lower the thermostat; a Return macro can reverse those actions. Run it from the **Run** button in the list or from its dashboard card.

## Dashboard cards

Cards are optional. From the dashboard's **+** menu choose **Automation** or **Macro**, then pick which automation the card should show. An Automation card shows whether the rule is armed and whether it is triggered; tapping it enables or disables the rule. A Macro card runs the macro on a tap. Each automation can have one card. Removing the card keeps the automation; deleting the automation removes its card.
