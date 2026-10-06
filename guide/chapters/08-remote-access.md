# Remote Access

::: lead
Open your coach's dashboard from anywhere — the campground, the office, the other side of the country — in the same browser, with the same cards and controls. No app, no router settings, no port forwarding. LaunchControl Remote does the connecting for you.
:::

## How it works

You connect the Hub to the internet, and visit the portal at remote.launchcontrol.tech. Everything local keeps working whether or not Remote is on.

**Every new Hub includes 90 days of Remote free.** The trial starts the first time the Hub is linked to an account. After that it is **$6.99 a month or $69 a year**, cancel any time.

::: technical
The Hub opens one outgoing, encrypted connection to LaunchControl's service and keeps it open. When you sign in at **remote.launchcontrol.tech**, your browser talks to the Hub through that connection. Nothing on the coach is exposed to the internet, and the Hub works behind any router, hotspot or Starlink exactly as it does at home.
:::

## Turn it on

Remote needs three things: the Hub on a network with internet access, the Hub's clock set, and a **Dashboard PIN** set.

1. **Enable it.** On the dashboard, go to **Settings → Integrations**, press **Set up** on the **LaunchControl Remote** card, then **Set up LaunchControl Remote**. The card shows *Connecting*, then *Ready to link*. (The setup wizard offers the same step at the end of a new installation.)
2. **Link it to you.** Press **Continue in browser**, or **Scan with your phone** to show a QR code and a six‑digit link code. You can also open **remote.launchcontrol.tech** in any browser and press **Link a hub**. Sign in with your e‑mail — a sign‑in link is sent to you; there is no password to remember — and enter the six‑digit link code.
3. **Open your coach.** The portal shows the hub under **My hubs**; press **Open**. Bookmark the remote address: it is yours for as long as the Hub is linked.

::: note "The PIN still applies"
The first time a browser opens the remote address, LaunchControl asks for your Dashboard PIN, exactly as it would on an untrusted network at the coach. Your account proves who you are to LaunchControl; the PIN proves it to the Hub.
:::

## Using it

The remote dashboard is the real dashboard: lights, thermostats, tanks, the Settings pages, automations, alerts, the floor plan. Live values update as they do at the coach. 

A small **cloud** next to the connection dot at the top of the dashboard shows the remote link: green while connected, amber while reconnecting. Tap it for the remote‑use guidance. On the localk network the same cloud appears while someone is viewing the Hub through Remote, so people at the coach can see that it is being used from afar.

**Awnings and slides do not move from Remote.** You cannot see what is around them, so the Hub refuses those commands when they arrive through Remote, whoever sends them, and their cards say "Not available remotely". Shades still work. Automations that move an awning run on the Hub itself and are unaffected.

If the Hub is not connected to Remote when you open the remote address, the page says **Hub offline** and when the Hub was last seen, in UTC. The Hub reconnects by itself as soon as it has internet again.

Siri, Shortcuts and other controllers work from anywhere through Remote too: under Shortcuts & API pick **LaunchControl Remote** as the **Connection method** before copying a link (see [Voice Control, Shortcuts, Siri and Other Controllers (API)](#voice-control-shortcuts-siri-and-other-controllers-api)).

## Your plan

Open **remote.launchcontrol.tech**, sign in and choose the hub. Its page shows the current access and when it ends.

- **Subscribe.** Press **Subscribe · $69 a year** or **Subscribe · $6.99 a month**. The plan starts when the access the hub already has runs out, so subscribing during the free trial does not shorten it: your card is saved now and first charged on that day. Payment is by card; the receipt and card details live under **Card & receipts** on the same page. Your first paid subscription carries a 30‑day money‑back guarantee from the first charge.
- **Auto‑renew.** Shown plainly beside the end date: *Auto‑renew on — renews on … ; your card is charged … then*, or *Auto‑renew off — access ends on …*. Turn it off and nothing more is charged; turn it back on before the end date and nothing is lost.
- **Switch plans.** A switch takes effect when the current paid period runs out; until then nothing changes and nothing is charged. The page says so while a switch is scheduled, and you can keep the current plan instead.
- **Reminders.** LaunchControl e‑mails you before a renewal and before access ends, and the same notices appear in the dashboard's alert inbox (the triangle in the header).
- **If a card is declined,** remote access continues for 14 days while the charge is retried; update the card under **Card & receipts**.

The ledger at the bottom of the page lists every piece of access the hub has had — the trial, each subscription period, every code — with dates.

## Sharing a hub

The owner can share a hub with other people — a partner, a co‑owner, a technician — under **Share with others** on the hub's page. Each person signs in with their own e‑mail address and finds the hub under My hubs. They can open it and use it; only the owner can change the plan, the name or the sharing, and the owner can remove anyone at any time. A shared user can also leave on their own. The Dashboard PIN applies to them as it does to you.

## Letting LaunchControl support in

If support asks to look at your hub, you decide, and you hold the key. On the hub's page in the portal press **Allow remote support for 24 hours**. The page shows a six-digit PIN; send it to LaunchControl support. Only an admin who enters that PIN can open your dashboard, and only for the next 24 hours, or until you press **Turn off remote support**, whichever comes first.

While the window is open, every page of your hub, on your own screen as well as theirs, shows a yellow border with "Remote support enabled". The moment an admin is actually connected the border turns red and reads "Remote support active" with your serial number, so there is never any doubt about who is in. Local control is never affected.

## Selling the coach, or starting over

**Unlink** (under **Turn off or unlink** on the LaunchControl Remote card in Settings, or on the hub's page in the portal) removes the hub from your account. **Turn off** in the same place only pauses Remote; the hub stays linked. The Hub shows a new code, ready for its next owner to link; your plan is cancelled. To close your account entirely, use **Delete my account** at the bottom of the portal: every hub is unlinked, every plan cancelled, and your sign‑in is removed.

::: warning "No subscription, no internet — still your coach"
Remote never stands between you and the coach. If the service is unreachable, the plan has ended or the Hub has no internet, everything on the coach's own Wi‑Fi works exactly as before.
:::

::: technical
The Hub holds one outbound WebSocket over TLS (port 443) to the relay and carries the dashboard's web requests and its live update socket inside it, so no inbound port exists on the coach side. The relay checks that the signed‑in account owns or shares the hub and that access is running, then hands each request to the Hub, where the Dashboard PIN applies as on any untrusted network. The Shortcuts API key is accepted on the remote address for its control address only. The Hub identifies itself by its serial, its own secret, and a factory token derived from its license, so a serial cannot be claimed by a different device. The relay address can be overridden under **Advanced settings** on the LaunchControl Remote card, shown when **Expert mode** at the bottom of that card is on, for bench use; leave it alone otherwise.
:::

## Free remote access

For those that are technically inclined, Tailscale, running on a travel router, or a similar VPN, can be used for remote access with no subscription fee.
