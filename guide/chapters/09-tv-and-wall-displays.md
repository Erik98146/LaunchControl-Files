# TV & Wall Displays

::: lead
Any TV, HDMI streaming stick, or wall tablet with a web browser can show one of your dashboard panels full-screen. LaunchControl calls this a **web kiosk**. Several can run at once without slowing the Hub, your phone, or your touchscreens down.
:::

## What a web kiosk is

A web kiosk is the ordinary LaunchControl dashboard, in a display mode: one panel, edge to edge, no tabs or menus, scaled up to fill the screen. It shows exactly what your phone shows, because it *is* the same dashboard — so every card you have, and every card added in a future update, works on a TV with nothing extra to set up.

A kiosk is **read-only on purpose**. It never sends a command. If one of your displays is a touchscreen or your TV has cursor mode and you do want to control from it, turn **Allow touch** on for that display alone.

::: note "It updates every few seconds, not instantly"
A kiosk checks in with the Hub every 12 seconds by default, rather than holding a live connection the way your phone does. That is what keeps several of them almost free for the Hub to serve. You can change this if desired. Values on a TV can be a few seconds behind — for a screen you glance at across a room, that is the right trade.
:::

## What to plug into the TV

::: note "Best: a streaming stick with a kiosk browser"
An **Amazon Fire TV Stick** with the **Fully Kiosk Browser** app (a few dollars, one-time) is the most reliable setup: it starts on its own when the TV powers on, keeps the screen awake, and reloads on a schedule. Any Android TV box, or a tablet in kiosk mode, works the same way.
:::

A wall-mounted tablet is also a good kiosk. On an iPad, add the page to the Home Screen so it opens without Safari's toolbars; on Android, use Fully Kiosk Browser as above.

## Set up a display

1. Go to **Settings>Displays** to find the web address that you should point your TV or stick to. 
2. **Open that address on your TV or stick** The device needs to be on the same network as the Hub.
3. **Set the size while watching the TV.** The controls under that display's name take effect on the screen within a few seconds — no reloading, no walking back and forth. Adjust them with the TV in view.
4. **Make it start by itself.** In your kiosk browser's settings, set the same address as the start page, and turn on "launch on boot" and "keep screen on" if it offers them.

## If the edges are cut off

Most televisions crop the outside of the picture slightly — it is called **overscan**, and it is why the right-hand cards looked chopped off on the first TV we tried this on.

1. **Fix it on the TV first.** In the TV's picture settings, find the aspect or size option and choose **Just Scan**, **Screen Fit**, **Full Pixel** or **1:1** — the name varies by brand. This is the real fix and costs no screen space.
2. **Then use Safe area for whatever is left.** Raise the **Safe area** control for that display until nothing is clipped. It pulls the whole dashboard in from every edge.

## The other controls

| Control | What it does |
|---|---|
| **Panel** | Which of your dashboard panels this display shows. |
| **Theme** | Overrides the dashboard theme for this display only. A dark theme is kinder to an OLED TV. |
| **Zoom** | Leave on **auto** to fill the screen. Set it by hand only if you want the dashboard deliberately smaller. |
| **Safe area** | Inset from every edge, for overscan (above). |
| **Text size** | Makes the writing on the cards bigger or smaller without changing the tile sizes. Useful on a screen you read from across a room. |
| **Rows** | How tall the panel area is. **9 rows fills a normal 16:9 TV**; use 10 for a 16:10 computer monitor. |
| **Fit** | "Fit the whole panel" keeps everything on screen. "Fill the width" makes the cards bigger and accepts that the bottom row is cut off. |
| **Long titles** | What happens to a card name too long for its tile: shrink it to fit, cut it short, or wrap it. |
| **Update every** | Seconds between updates. Raise it if you run several displays. |
| **Nightly reload** | Reloads the page once a night, during quiet hours. Keeps a TV browser that has been running for weeks healthy. Leave blank to never reload. |
| **Allow touch** | Lets this one display send commands. Off for a TV; on for a wall tablet you want to control from. |
| **Shift pixels** | Nudges the picture a pixel or two every few minutes, to protect an OLED panel from burn-in. |
| **Diagnostics overlay** | Shows sizes, scaling and update timing in the corner of the display. Turn it on if something looks wrong and you are asked for the numbers. |

## Designing a panel for a TV

A TV cannot scroll. It shows the top of the panel and cuts off anything below — so a panel built for a phone, which scrolls happily, usually has more rows than a TV can show.

The dashboard's panel editor can outline exactly what a TV will show: enter edit mode, and under **Dashboard Cards** press **TV panel guide** until it reads `16×9`. A blue outline marks the boundary. Keep the cards you want on the TV inside it.

::: note "Give a TV its own panel"
The easiest approach is a panel built for the TV — add one, arrange eight or nine rows of the cards you want to see from the sofa, and point the display at it. Your phone panels stay as they are.
:::

## Pinning a display to fixed settings

If you would rather not pair a display at all — say a stick you set up once and forget — use the **Kiosk** builder at the bottom of Settings → Displays. Choose the panel and the size controls, then either copy the link or scan the QR code with a phone to send it on. Set that whole address as the kiosk browser's start page.

A link built this way carries its settings in the address, so it overrides anything stored in Settings for that display. That makes it the right choice for a display you want to behave identically no matter what.

## Removing a display

Press **Remove** beside it in Settings → Displays. Its settings are erased and the screen goes back to showing a pairing code, ready to be added again — so this is also how you start a display over.

On the display itself, a long press in the **bottom-left corner** brings up a small panel with "Reload now" and "Forget this display". That is the only thing a kiosk responds to being touched; it is there for when you are standing at the screen without a phone.

::: note "Do I need the PIN on every TV?"
Only if the Hub's Dashboard PIN is on and the TV is on an untrusted network. Mark your coach's Wi-Fi as trusted in Settings → Network, and your displays never ask for a PIN. See [Security](#security).
:::
