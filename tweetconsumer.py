import datetime
import twitter
from dblayer import DBlayer

class TweetConsumer(object):

    def __init__(self,consumer_key,consumer_secret,access_token_key,access_token_secret,DEBUG):

        self.DEBUG = DEBUG

        self.pmdb = DBlayer()
        self.api = twitter.Api(consumer_key=consumer_key,
	                       consumer_secret=consumer_secret,
	                       access_token_key=access_token_key,
	                       access_token_secret=access_token_secret,
	                       cache=None,
        )
	              
        #self.merchantlist = self.pmdb.getmerchants()
        #self.s = []

        if self.DEBUG:
            print "TweetConsumer() init successful."

    def consume(self):

        if self.DEBUG:
            print "Reading merchant list from database ..."

        # get the latest merchant list
        merchantlist = self.pmdb.getmerchants()

        for merchant in merchantlist:
            self.statuses = []
            if merchant['twitterid']==None:
                try:
                    self.pulltwitterid(merchant)
                except:
                    print "no use adding any statuses..."
                    continue
                self.statuses = []
            self.statuses.extend(self.api.GetUserTimeline(user_id=merchant['twitterid'],
                            include_rts=False,
                            since_id=merchant['lasttweet'],
            ))

            if self.DEBUG:
                print "Adding statuses to database ..."
            for stat in reversed(self.statuses):
                self.pmdb.addtweet(self.filtertweet(stat))
                new = {'lastupdated':stat.created_at_in_seconds,
                       'lasttweet':stat.id,
                       'lastgeo':stat.geo,
                       'twitterhandle':stat.user.screen_name
                }
                self.pmdb.updatemerchant(merchant['_id'], new)
                if self.DEBUG:
		            print 'nom.'


    def filtertweet(self,s):
        ftweet = {'id':str(s.id),
                  'text':s.text,
                  'merchant':str(s.user.id),
                  'merchanthandle':str(s.user.screen_name),
                  'created':str(s.created_at_in_seconds),
                  'geo':str(s.geo),
                  'hashtags':str(s.hashtags)}
        return ftweet

    def pulltwitterid(self,merchant):
        print "whoops, no twitterid, must be a new user"
        try:
            user = self.api.GetUser(screen_name=merchant['twitterhandle'])
        except:
            print "holy smokes, that handle doesn't even exist!"
            return False
        merchant['twitterid'] = user.id
        print "found twitterid"
        self.pmdb.updatemerchant(merchant['_id'],{'twitterid':merchant['twitterid']})
        print "updated twitterid to db"

if __name__=="__main__":

    from twitter_creds import twitter_creds 

    tc = TweetConsumer(consumer_key=twitter_creds['consumer_key'],
                       consumer_secret=twitter_creds['consumer_secret'],
                       access_token_key=twitter_creds['access_token_key'],
                       access_token_secret=twitter_creds['access_token_secret'],
                       DEBUG=True,
    )

    tc.consume()
