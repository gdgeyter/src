from twython import Twython
import json
import pandas as pd
import matplotlib.pyplot as plt

TWITTER_APP_KEY = 'sIj5Wq5MWxikbT49SjgOGirmY' #supply the appropriate value
TWITTER_APP_KEY_SECRET = '37fl8M20O0iQoSrzMHmrbBEezhIABUdV8RUxASjo85ivAG5bWU'
TWITTER_ACCESS_TOKEN = '1072162742-YrxnXbr4p3dh8gbNdn1LjBeyvpsnOVFQRovP2Vf'
TWITTER_ACCESS_TOKEN_SECRET = 'Nwj2JzWpcHmy0l31RTJeicen5lTClgmRTbPE5nozGjeCX'

t = Twython(app_key=TWITTER_APP_KEY,
            app_secret=TWITTER_APP_KEY_SECRET,
            oauth_token=TWITTER_ACCESS_TOKEN,
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)

search = t.search(q='#HROS',   #**supply whatever query you want here**
                  count=500)


tweets = search['statuses']
print(tweets[1])
print(len(tweets))
tweets_data = []
for line in tweets:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

dfTweets = pd.DataFrame(tweets)
print(list(dfTweets.columns.values))
dfTweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, dfTweets)
tweets_by_lang = dfTweets['id_str'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 contributors', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

#for tweet in tweets:
#  print(tweet['id_str'], '\n', tweet['text'], '\n\n\n')