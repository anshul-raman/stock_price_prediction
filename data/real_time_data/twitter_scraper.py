import GetOldTweets3 as got

tweetCriteria = got.manager.TweetCriteria().setQuerySearch('google stock')\
                                           .setSince("2020-09-01")\
                                               .setMaxTweets(100)
tweet = got.manager.TweetManager.getTweets(tweetCriteria)
for t in tweet:
    print(t.text)