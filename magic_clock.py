from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from GPIOLibrary import GPIOProcessor

import time
import json

#consumer key, consumer secret, access token, access secret.
consumer_key = # secret_key
consumer_secret = # secret_key
access_token = # secret_key
access_secret = # secret_key

# Note these are some invalid test users.
users=["0123456789"]
# hash_tags=["#hashtag"]
# terms=["keyword1","keyword2","keyword3","keyword4"]

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        jsonData = json.loads(data)
        text = jsonData['text']
        place = jsonData['place']
        place_name = place['full_name']
        print(text)
        print(place_name)

        Pin25 = GP.getPin25()
        Pin25.out()

        if place_name == 'a':
            for x in range(0, 60):
                Pin25.high()
                Pin25.low()
        elif place_name == 'b':
            for x in range(0, 100):
                Pin25.high()
                Pin25.low()
        elif place_name == 'c':
            for x in range(0, 140):
                Pin25.high()
                Pin25.low()
        elif place_name == 'd':
            for x in range(0, 180):
                Pin25.high()
                Pin25.low()

        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    try:
        l = StdOutListener()
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        GP = GPIOProcessor()

        stream = Stream(auth, l)
        # stream.filter(track=hash_tags)
        stream.filter(follow=users)

    finally:
        GP.cleanup()
