import twitter
from dblayer import DBlayer

pmdb = DBlayer()
api = twitter.Api(consumer_key='GbQ2flsAujOSxEkGTee1Yw',
	              consumer_secret='dH3lAHODXrot6yZ5T4TrKcMLukKRAUK4sQtaPIflUU',
	              access_token_key='275002578-orQLeBDCwh8ZM70LL2kyyBGgauOKIEPlHzWKURmO',
	              access_token_secret='mBnDZ7DenTOtZULZHiJkGRAviV14XHYVs0yLN1Hj3pVir',
	              cache=None)
	              
merchantlist = pmdb.getmerchants()
s = []

def consume():
    for merchant in merchantlist:
	    if merchant['twitterid']==None:
	        pulltwitterid(merchant)
	    statuses = api.GetUserTimeline(user_id=merchant['twitterid'],
	                                   include_rts=False,
	                                   since_id=merchant['lasttweet'])
	    for stat in reversed(statuses):
	        pmdb.addtweet(filtertweet(stat))
	        new = {'lastupdated':stat.created_at,
	               'lasttweet':stat.id,
	               'twitterhandle':stat.user.screen_name}
	        pmdb.updatemerchant(merchant['_id'], new)
	        
	        print 'nom.'
	        

def filtertweet(s):
    ftweet = {'id':str(s.id),
              'merchant':str(s.user.id),
              'merchanthandle':str(s.user.screen_name),
              'created':str(s.created_at),
              'geo':str(s.geo),
              'hashtags':str(s.hashtags)}
    return ftweet

def pulltwitterid(merchant):
    print "whoops, no twitterid, must be a new user"
    user = api.GetUser(screen_name=merchant['twitterhandle'])
    merchant['twitterid'] = user.id
    print "found twitterid"
    pmdb.updatemerchant(merchant['_id'],{'twitterid':merchant['twitterid']})
    print "updated twitterid to db"

		   
if __name__=="__main__":
    consume()
