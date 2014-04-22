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
            'category':'meat',
        }

        """
        if self.merchants.find_one({'twitterhandle':merchant['twitterhandle']}):
            if self.DEBUG:
                print "Found merchant '{0}' already.  Consider updatemerchant() instead...".format(merchant['name'])
            return False
        
        if self.DEBUG:
            print "Adding merchant '{0}' to database ...".format(merchant['name'])
        
        success = False
        try:

            # add entity to the database
            merchant['lastupdated'] = str(strftime("%Y-%m-%d %H:%M:%S"))
            merchant['lastgeo'] = None
            merchant['lasttweet'] = None
            merchant['twitterid'] = None
            self.merchants.insert(merchant)
            success = True

        except Exception, e:
            if self.DEBUG:
                print "There was an error while adding the merchant:\n\n\t{0}".format(str(e))

        return success


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
        
        if self.DEBUG:
            print "Updating merchant '{0}' ...".format(merchid)

        success = False
        try:

            self.merchants.update({"_id": merchid},{"$set": new})
            success = True

        except Exception, e:
           if self.DEBUG:
               print "There was an error while updating the merchant:\n\n\t{0}".format(str(e))

        if self.DEBUG:
           print "Merchant successfully updated."

        return success
        
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
        if self.DEBUG:
            try:
                print "Adding tweet '{0}' ...".format(tweet['id'])
            except:
                print "Adding tweet ..."

        success = False
        try:

            self.tweets.insert(tweet)
            success = True

        except Exception, e:
           if self.DEBUG:
               print "There was an error while adding tweet:\n\n\t{0}".format(str(e))

        if self.DEBUG:
           print "Tweet successfully added."

        return success

    def _clearall(self):

        # blow away the entire database
        self.merchants.remove()
        self.tweets.remove()
        self.categories.remove()
        self.settings.remove()

        return True


