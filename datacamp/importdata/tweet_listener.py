import tweepy
import json


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file_name = "./data/tweets_stream.txt"

    def on_status(self, status):
        with open(self.file_name, 'w') as file:
            tweet = status.to_json
            file.write(json.dumps(tweet) + '\n')
            self.num_tweets += 1
            if self.num_tweets < 100:
                return True
            else:
                return False

    def on_error(self, status):
        print(status)
