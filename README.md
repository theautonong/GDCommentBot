Geometry Dash Comment Bot

A Python bot that connects to your Geometry Dash account and automatically posts comments on selected levels.
It is built using the gd.py
 library.
Disclaimer

Using bots in the official Geometry Dash may result in account bans if RobTop detects spam.

It’s highly recommended to test first on a GDPS (private server).

Use responsibly (don’t flood or spam).
Features

Logs into your Geometry Dash account.

Selects random levels from a predefined list.

Posts random comments from a custom list.

Waits a random amount of time between comments to look more human.

Saves a log in bot_log.txt with all posted comments.

Requirements

Python 3.9 or higher
pip install gd.py

Logs

Every posted comment is saved in bot_log.txt, including:

Date and time

Level ID
Comment text

gd.py
