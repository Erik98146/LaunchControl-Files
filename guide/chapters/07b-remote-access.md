# Remote Access

::: lead
Open your coach's dashboard from anywhere — the campground, the office, the other side of the country — in the same browser, with the same cards and controls. No app, no router settings, no port forwarding. LaunchControl Remote does the connecting for you.
:::

## How it works

The Hub opens one outgoing, encrypted connection to LaunchControl's service and keeps it open. When you sign in at **remote.launchcontrol.tech**, your browser talks to the Hub through that connection. Nothing on the coach is exposed to the internet, and the Hub works behind any router, hotspot or Starlink exactly as it does at home.

Everything local keeps working whether or not Remote is on: the dashboard on the coach's Wi‑Fi, the displays, automations, alerts. Remote only adds the from‑anywhere path.

**Every new Hub includes 90 days of Remote free.** The trial starts the first time the Hub is linked to an account. After that it is **$6.99 a month or $69 a year**, cancel any time.

## Turn it on

Remote needs three things: the Hub on a network with internet access, the Hub's clock set (Settings → System → Clock & Time; usually automatic), and a **Dashboard PIN** (Settings → Network). The PIN is what protects the coach once it is reachable from outside, so Remote cannot be enabled without one.

1. **Enable it.** On the dashboard, go to **Settings → Integrations → Remote Access** and switch **Enabled** on. The card shows *Connecting*, then *Waiting to be linked* with a six‑digit code and a QR code. (The setup wizard offers the same step at the end of a new installation.)
2. **Link it to you.** Scan the QR code with your phone, or open **remote.launchcontrol.tech** in any browser and press **Link a hub**. Sign in with your e‑mail address — a sign‑in link is sent to you; there is no password to remember — and enter the six‑digit code.
3. **Open your coach.** The portal shows the hub under **My hubs**; press **Open**. Back on the dashboard, the Remote Access card now says *Online* and shows the remote address. Bookmark it: it is yours for as long as the Hub is linked.

::: note "The PIN still applies"
The first time a browser opens the remote address, LaunchControl asks for your Dashboard PIN, exactly as it would on an untrusted network at the coach. Your account proves who you are to LaunchControl; the PIN proves it to the Hub.
:::

## Using it

The remote dashboard is the real dashboard: lights, thermostats, tanks, the Settings pages, automations, alerts, the floor plan. Live values update as they do at the coach. A few things only make sense locally — pairing a display, the Hub's own hotspot, and first‑run setup — and those stay on the coach's Wi‑Fi.

Alerts can travel through Remote as well: tick **E-mail (Remote)** on an automation's Send alert action and the alert is e-mailed to the account the hub is linked to, with nothing to set up. The hub's page in the portal lists the recent ones.

Siri, Shortcuts and other controllers work from anywhere through Remote too: type the remote address into **Hub address in the links** under Shortcuts & Siri before copying a link (see [Voice Control, Shortcuts, Siri and Other Controllers (API)](#voice-control-shortcuts-siri-and-other-controllers-api)).

## Your plan

Open **remote.launchcontrol.tech**, sign in and choose the hub. Its page shows the current access and when it ends.

- **Subscribe.** Pick monthly or annual. Payment is by card; the receipt and card details live under **Card & receipts** on the same page.
- **Auto‑renew.** Shown plainly beside the end date: *Auto‑renew on — renews on … ; your card is charged … then*, or *Auto‑renew off — access ends on …*. Turn it off and nothing more is charged; turn it back on before the end date and nothing is lost.
- **Switch plans.** A switch takes effect when the current paid period runs out; until then nothing changes and nothing is charged. The page says so while a switch is scheduled, and you can keep the current plan instead.
- **Reminders.** LaunchControl e‑mails you before a renewal and before access ends, and the same notices appear in the dashboard's alert inbox (the triangle in the header).
- **If a card is declined,** remote access continues for 14 days while the charge is retried; update the card under **Card & receipts**.

The ledger at the bottom of the page lists every piece of access the hub has had — the trial, each subscription period, every code — with dates.

## Codes and gifts

A code looks like **LC‑XXXX‑XXXX** and adds its time to the end of the hub's current access, so redeeming one during the trial does not shorten the trial. Enter it under **Redeem a code** on the hub's page in the portal.

A year of Remote bought in the LaunchControl store arrives by e‑mail as a code within a few minutes of the order. If you bought it with the same e‑mail address you use to sign in, the code is also waiting on your hub's page with an **Apply to this hub** button. To give a year to someone else, forward them the code; it works once.

## Sharing a hub

Remote is per hub, not per person. The owner can share a hub with other people — a partner, a co‑owner, a technician — under **Share with others** on the hub's page. Each person signs in with their own e‑mail address and finds the hub under My hubs. They can open it and use it; only the owner can change the plan, the name or the sharing, and the owner can remove anyone at any time. A shared user can also leave on their own. The Dashboard PIN applies to them as it does to you.

## Selling the coach, or starting over

**Unlink** (on the Remote Access card in Settings, or on the hub's page in the portal) removes the hub from your account. The Hub shows a new code, ready for its next owner to link; your plan is cancelled. To close your account entirely, use **Delete my account** at the bottom of the portal: every hub is unlinked, every plan cancelled, and your sign‑in is removed.

## What the card says

| Status | Meaning |
| --- | --- |
| Off | Remote is switched off. The Hub makes no outside connection. |
| Connecting | The Hub is reaching LaunchControl's service. Normal for a few seconds after enabling or after a network change. |
| Waiting to be linked | Connected, not yet linked to an account. The code and QR are shown. |
| Online | Linked and reachable. The remote address is shown. |
| Trial / active / ending | Access is running, and when it ends. |
| Ended | The trial or plan ran out. Local control is unaffected; subscribe or redeem a code to resume. |
| Payment needed | A renewal charge failed. Access continues for 14 days; update the card. |
| Clock not set | The Hub has no valid time, which the encrypted connection needs. Set a time source under Settings → System. |
| No network | The Hub has no internet path. |
| Identity conflict | This serial is linked to an account, but from a different Hub identity — typically after a factory reset or a re‑flash. Unlink it from the owning account (My hubs → the hub → Unlink), then enable Remote again. |
| Blocked | Remote access was suspended by LaunchControl. Contact support. |

Whether LaunchControl's service itself is up is always visible at **remote.launchcontrol.tech/status**.

::: warning "No subscription, no internet — still your coach"
Remote never stands between you and the coach. If the service is unreachable, the plan has ended or the Hub has no internet, everything on the coach's own Wi‑Fi works exactly as before.
:::

::: technical
The Hub holds one outbound WebSocket over TLS (port 443) to the relay and carries the dashboard's web requests and its live update socket inside it, so no inbound port exists on the coach side. The relay checks that the signed‑in account owns or shares the hub and that access is running, then hands each request to the Hub, where the Dashboard PIN applies as on any untrusted network. The Shortcuts API key is accepted on the remote address for its control address only. The Hub identifies itself by its serial, its own secret, and a factory token derived from its license, so a serial cannot be claimed by a different device. The relay address can be overridden under **Advanced** on the Remote Access card for bench use; leave it alone otherwise.
:::
