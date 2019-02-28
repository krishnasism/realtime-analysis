def getTweets(query):
    import apistore
    import tweepy
    import csv
    import pandas as pd
   
    ####set your credentials here

    consumer_key=apistore.consumer_key
    consumer_secret=apistore.consumer_secret
    access_token=apistore.access_token
    access_token_secret=apistore.access_token_secret
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True)

    csvFile = open(query+'.csv', 'a')
    #Use csv Writer
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search,query,count=5,
                            lang="en",
                            since="2019-02-28").items():
        #print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])