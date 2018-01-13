from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json

#consumer key, consumer secret, access token, access secret.


# Note these are some invalid test users.
users=["userid"]
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
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    stream = Stream(auth, l)
    # stream.filter(track=hash_tags)
    stream.filter(follow=users)
