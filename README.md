# RoyalHackaway 2018

A 'magic' clock to passively present information about where you someone is, based on their most recent geotagged tweets.

Inspired by the Weasley Clock from the Harry Potter series, this system is extensible enough to add a few users, have many hands, and set it up for your entire family / flat!

*By Sam Warner and Selina-Jane Spencer*

## Dependencies and things

You'll need Python and Tweepy installed on your Dragonboard 410c.

* Python is the entire way the system works. GPIO pin interaction, and twitter listener both need this!
`sudo apt install python`
* Tweepy is needed to listen for tweets:
`pip install tweepy`
* Dragonboard 410c
This is obvious - you can pick them up at [96boards](https://www.96boards.org/)!
* Something to house your clock
We've used some cardboard for the face, and even more cardboard for the hand.
