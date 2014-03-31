import twitter
api = twitter.Api(consumer_key='GbQ2flsAujOSxEkGTee1Yw',
                  consumer_secret='dH3lAHODXrot6yZ5T4TrKcMLukKRAUK4sQtaPIflUU',
                  access_token_key='275002578-orQLeBDCwh8ZM70LL2kyyBGgauOKIEPlHzWKURmO',
                  access_token_secret='mBnDZ7DenTOtZULZHiJkGRAviV14XHYVs0yLN1Hj3pVir',
                  cache=None)
print api.VerifyCredentials()
