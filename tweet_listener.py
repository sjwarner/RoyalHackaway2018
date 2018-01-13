from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json

#consumer key, consumer secret, access token, access secret.


# Note these are some invalid test users.
# users=["12332342344522","1232132423422323","21323213231234","23232121323243","2490921312323137"]
hash_tags=["#something"]
# terms=["keyword1","keyword2","keyword3","keyword4"]

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        jsonData = json.loads(data)
        text = jsonData['text']
        place = jsonData['place']
        print(text)
        print(place)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    stream = Stream(auth, l)
    stream.filter(track=hash_tags)
    # stream.filter(follow=users,track=hash_tags+terms)
