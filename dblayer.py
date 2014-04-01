# (do we need json?)
# import json

from pymongo import MongoClient
from time import strftime


class DBlayer(object):

    def __init__(self,uri='mongodb://localhost:27017/',db='pubmarkdb',DEBUG=False):

        self.DEBUG = DEBUG

        if self.DEBUG:
            print "Starting DBlayer() INIT ..."

        self.dbclient = MongoClient(uri)
        self.db = self.dbclient[db]
        
        self.merchants = self.db['merchants']
        self.tweets = self.db['tweets']
        self.categories = self.db['categories']
        self.settings = self.db['settings']

        if self.DEBUG:
            print "DBlayer() INIT completed successfully."


    def addmerchant(self,merchant):
    
        #
        # TODO: validate merchant input against fields in dict
        #

        """
        
        merchant = {
            'name':'Default Merchant',
            'description':'Pay no attention to the default user behind the curtain.',
            'twitterhandle':'@CityRochesterNY',
            'twitterid':'275002578',
            'lastupdated':'1970-01-02 12:34:56',
            'lastgeo':'None',
            'lasttweet':'90557458052943873',
        }

        """


        # add entity to the database
        merchant['lastupdated'] = str(strftime("%Y-%m-%d %H:%M:%S"))
        merchant['lastgeo'] = None
        merchant['lasttweet'] = None
        self.merchants.insert(merchant)

        return True


    def getmerchants(self,find=None,sortby=None,direction=None):

         # get the merchants
        results = self.merchants.find(find)
        if sortby:
            results = results.sort(sortby,direction)
        output = []
        for result in results:
            output.append(result)
        return output
        
    def updatemerchant(self, merchid, new):
 
        """
        new = {
            'lastupdated':'1970-01-02 12:34:56',
            'lastgeo':'None',
            'lasttweet':'90557458052943873',
        }
        
        """
        self.merchants.update({"_id": merchid},{"$set": new})
        return False
        
    def addtweet(self,tweet):
    
        """
        
        tweet = {
            'id':'Default Merchant',
            'merchant':'275002578',
            'merchanthandle':'@CityRochesterNY',
            'created':'1970-01-02 12:34:56',
            'geo':'None(uhhh..)',
            'hashtags':'#PublicMarket',
        }

        """
        
        self.tweets.insert(tweet)
        return True

    def _clearall(self):

        # blow away the entire database
        self.merchants.remove()
        self.tweets.remove()
        self.categories.remove()
        self.settings.remove()

        return True


