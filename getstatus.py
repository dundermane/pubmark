from dblayer import DBlayer

db = DBlayer()

merchants = db.getmerchants()

print "merchants in database: {0}".format(merchants)

