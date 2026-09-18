# Alerts

::: lead
Have the Hub tell you when something happens in the coach — a tank filling, a battery running low, the shore power dropping. Alerts go to your phone as a notification or as a text message, and they are sent by an automation you set up.
:::

## How it fits together

An alert is an **action on an automation**, in the same list as "turn the pump off". So the sequence is always:

1. Set up one or both of the services below, in Settings → Integrations.
2. Add an Automation card and tell it what to watch.
3. Add **Send alert** as one of its actions, and write the message.

You pay the service, not us. Both are cheap; one is free.

::: warning "The Hub sends alerts over the internet without encryption"
Anyone able to watch the coach's internet connection could read your alert messages and the topic or key they are sent with. That is why we only support services where the worst case is small: a notification topic you can replace in one click, and a prepaid text balance. Do not put anything private in an alert message.
:::

## Push notifications (free)

This uses **ntfy**, a free notification service with an app for iPhone and Android.

1. **Turn it on.** Settings → Integrations → **Push Alerts** → Enabled → **Save**. The Hub generates a private topic name for you.
2. **Install the ntfy app** from the App Store or Google Play.
3. **Subscribe to your topic.** Scan the QR code on the Settings page with your phone, or open the app, tap **+**, and type the topic exactly as shown.
4. **Send test.** The notification should arrive in a second or two.

Repeat steps 2–4 on every phone that should get alerts.

::: warning "The topic name is the password"
There is no login. Anyone who knows your topic can read every alert you send. Do not post it anywhere or put it in a photo. If you think it has got out, press **New topic** — but remember every phone then has to subscribe to the new one.
:::

## Text messages (prepaid)

This uses **Textbelt**, where you buy a block of messages up front.

1. **Buy credits.** Open [textbelt.com/purchase](https://textbelt.com/purchase/) and choose **generate a new API key**. Pick United States / Canada, choose a pack, and pay. Packs start around $3 for 50 messages.
2. **Set a sender name.** On the Textbelt Account page, fill in the sender name. **Textbelt will not send anything until you do**, and it is the step almost everyone misses.
3. **Paste the key** into Settings → Integrations → **SMS Alerts**, add your 10-digit phone number, turn **Enabled** on, and press **Save**.
4. **Send test.** This sends a real message and uses one credit.

::: note "Watch the credit count"
The Settings card shows how many credits are left, checked after each message. The Hub will send you a notification when they run low — by push, never by text, since that would spend one of the last credits. Credits expire after a year with nothing sent.
:::

::: warning "Accented characters cost double"
A text message holds 160 plain characters. A single accented or special character switches the whole message to a format that holds only 70, so one alert can quietly cost two credits. The Hub strips those characters before sending — degree signs become plain letters — and the message box warns you as you approach the limit.
:::

## Adding an alert to an automation

Open an Automation card's settings and pick **Send alert** in either action list — **when it triggers**, **when it clears**, or both.

- **Channels.** Tick Push or SMS. Only the ones you have set up are offered.
- **Message.** A sensible message is filled in for you. Edit it freely.
- **Insert value.** Drops a live reading into the message at the cursor.

You can have one alert in each list. If you want the same event sent two ways, tick two channels on the one alert rather than adding a second.

### Putting live values in the message

The words in curly brackets are replaced when the alert is sent:

| What you type | What arrives |
|---|---|
| `{value}` | The reading that set the automation off, with its units — `92 %`, `66 F` |
| `{device}` | The name of the sensor the automation watches |
| `{name}` | The name of the Automation card |
| `{time}` | The time, as `14:02` |

The **Insert value** button also lists every card on your dashboard, so an alert about the fresh tank can mention the battery as well. The numbers are exactly the ones the cards show.

So `{name}: {device} is {value}` arrives as **Fresh Tank: Fresh Water is 92 %**.

::: note "Macros can alert too"
A Macro card can send an alert when you tap it — useful for "Leaving site" to confirm to yourself that it ran. Macros have no sensor, so `{value}` and `{device}` are empty there.
:::

## What happens when there is no internet

The Hub holds the message and keeps trying — after 30 seconds, a minute, five minutes, then hourly, giving up after a day. When the connection comes back the message arrives, and **it still reports the reading that set the automation off**, not whatever the sensor says by then.

## If an alert does not arrive

- **Check the Automation card.** It shows `alert sent 2m ago`, or the reason it failed, right on the card face.
- **Push:** confirm the phone is subscribed to the topic shown in Settings — a **New topic** press unsubscribes every phone.
- **SMS:** check the credit count, and check you set a sender name on the Textbelt account page.
- **SMS says 0 credits right after you bought some?** Textbelt reports 0 both for an empty
  balance and for a key it does not recognise, so the likely cause is the key rather than the
  purchase. Each time you press **generate a new API key** you get a *different* key, and the
  credits belong to the one you paid with. The Settings card shows the length and last four
  characters of the key the Hub is holding — compare that with the key on your Textbelt
  account page, and paste the right one if they differ.
- **Send test** in Settings tells you what the service said, in its own words.

::: note "How often can it send?"
No more than one alert per minute from the same automation and edge, and by default no more than 30 an hour in total. You can change the hourly limit in Settings. It exists so a badly set-up rule cannot empty your text credits overnight.
:::
