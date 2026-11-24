# AI Assistant

::: lead
Ask an AI assistant such as Claude or ChatGPT about your coach in plain words, by voice or by typing, and have it switch lights, pumps, locks, and thermostats for you. It works through LaunchControl Remote, from anywhere your phone has internet. This feature is in beta.
:::

## What you need

- **LaunchControl Remote, linked and running.** The assistant reaches the Hub through Remote, so it needs a Remote plan or the free trial. See [Remote Access](#remote-access).
- **An AI assistant account of your own.** Claude works on its free plan. ChatGPT needs a Plus plan for now. The assistant runs on your account; LaunchControl adds no charge of its own.
- **Share Hub status** turned on (it is, unless you turned it off) so the assistant can see readings, and **Include location history** if you want to ask where the coach is or has been. Both are on the LaunchControl Remote card in the Hub’s Settings.

## Turn it on

1. **Let the Hub share its key.** On the Hub, open **Settings → Integrations → LaunchControl Remote** and turn on **Let the AI assistant use this Hub**. Then press **Open AI assistant setup**.
2. **Copy your connector link.** The portal opens the Hub’s page. On the **AI assistant** card, press **Copy link** under **Your connector link**.
3. **Add the link to your assistant,** as described below.
4. **Try it.** Open the assistant’s app on your phone, tap the voice button, and ask “What’s my battery at?”

### Claude

1. On a computer, open **claude.ai** and sign in.
2. Go to **Customize → Connectors → Add custom connector**.
3. Name it, for example “My coach”. Paste the link as the server URL, leave sign-in off, and click **Add**.

The first time Claude uses one of the coach’s tools, it asks you to allow it.

### ChatGPT

1. Log in to ChatGPT.
2. Go to **Plugins → Add → Custom MCP server**.
3. Name it, for example “LaunchControl”, and add the connector link.
4. Switch authentication to **No Authentication**, check the box, and create it.

::: warning "Keep the link private"
Anyone with the connector link can see this Hub’s status and control it through an AI assistant. Do not post or share it. If it may have leaked, press **Regenerate link** on the AI assistant card; the old link stops working and you add the new one to your assistant.
:::

## Real-world examples

**A quick check, hands busy.** You are hooking up at a campsite. “Turn on the water pump.” “Turn all the outside lights on.” “Set the bedroom to 70.”

**The coach is in storage.** “How are the batteries doing?” “Did the battery drop more last night than the night before?” “When did the shore power go off?” “Is anything unusual?” The assistant answers from the Hub’s reports, even when the Hub is offline at that moment, and tells you how old the readings are.

**Someone or something is in the coach.** “What’s the temperature inside, and did it go above 80 today?” “Is the air conditioning running?” “Lock the front door.”

**End of a driving day.** “How far did we drive today?” “Show me yesterday’s route.” “How much solar did we make this week?”

**Something is not working.** “Is the Hub healthy?” “Which sensor stopped reporting?” “Why didn’t my low battery automation fire?” “What does the amber outline on a tank card mean?” The assistant can read the Hub’s health, its device list, your automations, and this guide.

**Your own words.** “From now on, call the awning lights ‘porch’.” The assistant remembers the nickname for that Hub.

## What it can and cannot do

| | |
| --- | --- |
| **Reads** | Power, tanks, temperatures, climate, and alerts; how a reading changed over up to 30 days; what happened and when; daily energy; trips and location when location sharing is on; the Hub’s health; your devices and automations; this guide |
| **Does at once** | Lights and color lights, the water pump, switches, tank heat, fans, the inverter, lighting zones and scenes, the Sleep Timer, a thermostat’s temperature, and locking a door |
| **Asks you to confirm first** | Unlocking a door, Starlink power, running a macro, turning an automation on or off, changing a thermostat’s mode, and the shore current limit |
| **Never does** | Awnings, shades, slides, leveling jacks, and vents. It also cannot create or change automations, scenes, timers, the dashboard layout, or settings |

- The assistant uses your card names. If two names are equally close, it asks which one you mean.
- After each command it reads back the Hub’s own answer, so you hear what actually happened.
- A confirmation is good for one minute and one command.
- If the Hub is offline, commands are refused, not saved for later. Readings from the Hub’s last report are still available.

## Privacy

- Nothing is shared with any AI provider until you turn the assistant on.
- While it is on, the names of your devices, their readings, your alerts and — if location sharing is on and you ask — the Hub’s location pass through the AI provider you connect, under that provider’s own terms.
- LaunchControl Remote keeps 30 days of readings, energy, and location history so the assistant can answer questions about the past.
- **Activity** on the AI assistant card lists the last commands the assistant sent to the Hub. Status questions are not listed. **Clear activity** empties it.
- **Proactive findings** is off unless you turn it on. When on, an unusual reading — a sudden change, a battery draining faster than usual, a sensor gone quiet, commands that fail — adds a notice to the Hub’s alert list, at most once a day for each finding.

## Turn it off

Press **Turn off** on the AI assistant card in the portal, or turn off **Let the AI assistant use this Hub** on the Hub. The link stops working and the Hub’s key is deleted from LaunchControl Remote. You can turn it on again later and add its link to your assistant again.

## If it does not work

- **“The AI assistant needs running remote access.”** The trial or plan has ended; choose a plan on the same page.
- **The assistant says the Hub is offline.** The Hub has no internet at the moment. Readings from its last report still work.
- **It operates the wrong device.** Say the card’s full name, rename one of two similar cards, or teach the assistant a nickname.
- **It will not open an awning or slide.** That is by design; operate them at the coach.
- **It stopped working after you replaced the API access key.** If the Hub shares its key itself, nothing is needed. If you pasted the key into the portal, paste the new one under **Change the Hub key**.

::: technical
The connector is a Model Context Protocol (MCP) server at `remote.launchcontrol.tech/mcp/…`, added to the assistant with no sign-in; the link itself is the secret. Commands go to the Hub through the Remote tunnel, to the same control address Siri and Shortcuts use, with the Hub’s API access key. The Hub shares that key when **Let the AI assistant use this Hub** is on, and again whenever the key is replaced. The service allows up to 20 commands a minute per Hub.
:::
