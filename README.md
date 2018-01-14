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

* Some kind of servo or stepper motor

We're using the Kuman KY66, as the stepper motor and driver supplied have no documentation **anywhere** on the internet!

* Something to house your clock

We've used some cardboard for the face, and even more cardboard for the hand.

## Current problems

At the moment, we're only using a 180 degree servo because that's the best we have available. This means the clock will only really be half a clock, with around 5 distinct 'place' sections. Either modifying the servo to rotate through 360 degrees or buying a better servo would help this.

Manual reset! Because the servo is a lower-quality one, we've not been able to get it to go two different directions. While I think it is possible for the KY66, I've not figured it out yet. As a result, when position has been updated, the hand needs to be manually reset for the next update.
