# Snips-Bahnauskunft
A public transportation info-app for Snips.ai

## Installation

**Important:** The following instructions assume that [Snips](https://snips.gitbook.io/documentation/snips-basics) is
already configured and running on your device. [SAM](https://snips.gitbook.io/getting-started/installation) should
also already be set up and connected to your device and your account.

1. In the German [app store](https://console.snips.ai/) add the
app `Bahnauskunft` to your *German* assistant.

2. If you already have the same assistant on your platform, update it
(with [Sam](https://snips.gitbook.io/getting-started/installation)) with:
      ```bash
      sam update-assistant
      ```
      
   Otherwise install the assistant on the platform with [Sam](https://snips.gitbook.io/getting-started/installation)
   with the following command to choose it (if you have multiple assistants in your Snips console):
      ```bash
      sam install assistant
      ```
That's it!

## Usage

With this app you can ask Snips for information about when the next available bus or train departs to your destination.

### Example sentences

Wann fährt der nächste Bus zum Hauptbahnhof?
Wann kann ich nach Berlin fahren?

---
## Contribution

Please report errors (you can see them with `sam service log`) and bugs by
opening a [new issue](https://github.com/hokascha/snips-bahnauskunft/issues/new).
You can also write other ideas for this skill. Thank you for your contribution.
