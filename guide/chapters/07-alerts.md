# Alerts

::: lead
Have the Hub tell you when something happens in the coach — a tank filling, a battery running low, the shore power dropping. Alerts show on the Hub's screens, and can also go to your phone as a notification or a text message. They are sent by an automation you set up.
:::

## Where alerts appear

Every alert lands in the **alert list**. A red triangle with a count appears at the top right of the dashboard whenever the list holds anything; click it to open the list. The same list is always available under **Settings → Status → Alerts**.

- New alerts are shown **bold** until you have looked at them.
- Alerts from your automations stay in the list until you delete them, one at a time with the trash can or all at once with **Delete all**.
- Hub health alerts cannot be deleted; they clear on their own when the problem is fixed.
- The triangle stays lit until the list is empty.

## Hub health alerts

The Hub watches itself and raises an alert when something has been wrong for a while: no RV-C data arriving, MQTT or Victron turned on but not connected, the network down, the clock not set, memory running low, or CAN frames being dropped. These are marked **active** in the list and go away as soon as the condition clears.

## Update notices

Once a day, when a browser is open on the dashboard or Settings and has internet access, the Hub checks for a newer firmware release. If one is available, an **Update available** alert appears; delete it once you have seen it. Install from Settings → System → Online Update.

## How automation alerts fit together

An alert is an **action on an automation**, in the same list as "turn the pump off":

1. Open Settings → Automations and create or edit an automation.
2. Add **Send alert** as one of its actions and write the message.
3. Tick where it should go: **On-screen** (the alert list), **Push**, **SMS**.

On-screen needs nothing else. Push and SMS need the services below, set up under Settings → Automations. Push is free; SMS is cheap — you pay the service, not us.

## Push notifications (free)

This uses **ntfy**, a free notification service with an app for iPhone and Android.

1. **Turn it on.** Settings → Automations → **Push Alerts** → Enabled → **Save**. The Hub generates a private topic name for you.
2. **Install the ntfy app** from the App Store or Google Play.
3. **Subscribe to your topic.** Scan the QR code on the Settings page with your phone, or open the app, tap **+**, and type the topic exactly as shown.
4. **Send test.** The notification should arrive in a second or two.

Repeat steps 2–4 on every phone that should get alerts.

## Text messages (prepaid)

This uses **Textbelt**, where you buy a block of messages up front.

1. **Buy credits.** Open [textbelt.com/purchase](https://textbelt.com/purchase/) and choose **generate a new API key**. Choose a pack, and pay. Packs start around $3 for 50 messages. **SAVE THE KEY. It cannot be retrieved if lost.**
2. **Set a sender name.** On the Textbelt Account page, fill in the sender name. **Textbelt will not send anything until you do**, and it is the step almost everyone misses.
3. **Paste the key** into Settings → Automations → **SMS Alerts**, add your 10-digit phone number, turn **Enabled** on, and press **Save**.
4. **Send test.** This sends a real message and uses one credit.

::: note "Watch the credit count"
The Settings card shows how many credits are left, checked after each message. The Hub will send you a notification when they run low — by push, never by text, since that would spend one of the last credits. Credits expire after a year with nothing sent.
:::

## Writing the message

- **Channels.** On-screen is always available; Push and SMS appear once set up.
- **Message.** A sensible message is filled in for you. Edit it freely.
- **Insert value.** Drops a live reading into the message at the cursor.

You can have one alert in each action list. If you want the same event sent two ways, tick two channels on the one alert rather than adding a second.

### Putting live values in the message

The words in curly brackets are replaced when the alert is sent:

| What you type | What arrives |
|---|---|
| `{value}` | The reading that set the automation off, with its units — `92 %`, `66 F` |
| `{device}` | The name of the sensor the automation watches |
| `{name}` | The name of the automation |
| `{time}` | The time, as `14:02` |

The **Insert value** button also lists every card on your dashboard, so an alert about the fresh tank can mention the battery as well. The numbers are exactly the ones the cards show.

So `{name}: {device} is {value}` arrives as **Fresh Tank: Fresh Water is 92 %**.

::: note "Macros can alert too"
A macro can send an alert when it runs — useful for "Leaving site" to confirm to yourself that it ran. Macros have no sensor, so `{value}` and `{device}` are empty there.
:::

## What happens when there is no internet

On-screen alerts never need it. For push and SMS the Hub holds the message and keeps trying — after 30 seconds, a minute, five minutes, then hourly, giving up after a day. When the connection comes back the message arrives, and **it still reports the reading that set the automation off**, not whatever the sensor says by then.

## If an alert does not arrive

- **Check the list** under Settings → Status → Alerts. An on-screen alert there means the automation fired; the Automations page also shows "fired 2 min ago" on the rule.
- **Nothing fired at all?** The rule may have been already past its threshold when you enabled it ("Triggered · at start, not fired"). Enable it while the reading is on the normal side, then let it cross.
- **Push:** confirm the phone is subscribed to the topic shown in Settings — a **New topic** press unsubscribes every phone.
- **SMS:** check the credit count, and check you set a sender name on the Textbelt account page.
- **SMS says 0 credits right after you bought some?** Textbelt reports 0 both for an empty balance and for a key it does not recognise, so the likely cause is the key rather than the purchase. Each time you press **generate a new API key** you get a *different* key, and the credits belong to the one you paid with. The Settings card shows the length and last four characters of the key the Hub is holding — compare that with the key on your Textbelt account page, and paste the right one if they differ.
- **Send test** in Settings tells you what the service said, in its own words.

::: note "How often can it send?"
No more than one push or text per minute from the same automation and edge, and by default no more than 30 an hour in total. You can change the hourly limit in Settings. It exists so a badly set-up rule cannot empty your text credits overnight. On-screen alerts are not limited.
:::
