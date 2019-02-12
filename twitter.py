def getTweets(query):
    import tweepy
    import csv
    import pandas as pd
    ####input your credentials here
    consumer_key = 'lGL1qanIIla3zP3jt9RJkmBOC'
    consumer_secret = 'NZZcUgUMeYz6iGtFZTSexbjXiYshTTKpPfo3mSf8ut6VsFBFhx'
    access_token = '806132871823912964-kq6Tc8lwiOrSwoGvUPcVOiSV3YJEJbP'
    access_token_secret = 'VT7LGrqI94nP4Kq5w0FS7hURJAhD3FtYim9r6NScGkvEd'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    csvFile = open(query+'.csv', 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search,query,count=100,
                            lang="en",
                            since="2019-02-6").items():
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])