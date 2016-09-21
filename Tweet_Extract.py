from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
class StdOutListener(StreamListener):
    def on_data(self, data):
        print data
        return True
    def on_error(self, status):
        print status
if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    
    #This line filter Twitter Streams to capture data by the keywords: 
    stream.filter(track=['high'])
    
    with open("tokens.txt", "r") as f:
        tokens = f.readlines()
    
    
    F = open("Tweets.csv",'w')
    print >> F,'data'
    F.close()

    

    
    