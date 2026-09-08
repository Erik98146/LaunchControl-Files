# Automations & Macros

::: lead
Automations let the coach react to changing conditions. Macros group several actions behind one tap. Both appear as dashboard cards so they remain visible and controllable.
:::

## Automation rules

An Automation card watches one sensor and acts when the reading crosses a threshold.

- **Sensor —** any supported RV-C or Victron reading such as battery percentage, voltage, or temperature.
- **Trigger —** above or below a value, optionally held for a selected period so a short excursion does not fire the rule.
- **Release —** a second value where the rule resets. The gap between trigger and release prevents rapid on/off cycling.
- **Actions —** up to four actions on trigger and four on release, including device switching, lighting masters, and thermostat changes.

The card shows whether the rule is armed and whether it is currently triggered. Tap the card to enable or disable the rule. Common templates can pre-fill the editor.

![Automation example.](images/ch06-automation-example.png)

::: note "Power-up behavior"
When the Hub starts, or when an automation is edited or re-enabled, the rule adopts the current state without firing actions just because the Hub restarted.
:::

## Macros

A Macro card runs up to four actions with one tap. For example, an Away macro might switch off the water pump and lower the thermostat; a Return macro can reverse those actions. Configure the action list in the card settings.
