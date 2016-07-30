import json
from nltk.tokenize import word_tokenize
import re
import operator
import json
from collections import Counter
from nltk.corpus import stopwords
import string
import pandas as pd
import matplotlib.pyplot as plt
import os
import vincent

os.chdir('/Users/gdgeyter/Documents/Projects/trydjango18/src/TwitterExtraction')
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens



#
# with open(fname, 'r') as f:
#     count_all = Counter()
#     for line in f:
#         tweet = json.loads(line)
#         # Create a list with all the terms
#         if(tweet['lang']=='en'):
#             terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
#             # Count terms only once, equivalent to Document Frequency
#             terms_single = set(terms_stop)
#             # Count hashtags only
#             terms_hash = [term for term in preprocess(tweet['text'])
#                           if term.startswith('#')]
#             # Count terms only (no hashtags, no mentions)
#             terms_only = [term for term in preprocess(tweet['text'])
#                           if term not in stop and
#                           not term.startswith(('#', '@'))]
#             # mind the ((double brackets))
#             # startswith() takes a tuple (not a list) if
#             # we pass a list of inputs
#         # Update the counter
# count_all.update(terms_all)
#     # Print the first 5 most frequent words
#
# print(count_all.most_common(15))
# print(terms_hash)
#
# from nltk import bigrams
#
# terms_bigram = bigrams(terms_stop)
# print(terms_bigram[1])
# #print(terms_bigram)

import operator
import json
from collections import Counter
from nltk import bigrams

fname = 'twitter.json'

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['RT', 'via','…','The','0','1','Thx','fr']
alltweets = []
with open(fname, 'r') as f:
    count_all1 = Counter()
    count_all2 = Counter()
    count_all3 = Counter()
    count_all4 = Counter()
    for line in f:
        tweet = json.loads(line)
        if (tweet['lang'] == 'en'):
            alltweets.append(tweet)
            # Create a list with all the terms
            terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]
            #print(terms_stop)
            # Count terms only once, equivalent to Document Frequency
            terms_single = set(terms_stop)
            # Count hashtags only
            terms_hash = [term for term in preprocess(tweet['text'])
                          if term.startswith('#')]
            # Count terms only (no hashtags, no mentions)
            terms_only = [term for term in preprocess(tweet['text'])
                          if term not in stop and
                          not term.startswith(('#', '@'))]
            terms_bigram = bigrams(terms_stop)
            # mind the ((double brackets))
            # startswith() takes a tuple (not a list) if
            # we pass a list of inputs

        # Update the counter
        count_all1.update(terms_stop)
        count_all2.update(terms_hash)
        count_all3.update(terms_only)
        count_all4.update(terms_bigram)

    # Print the first 5 most frequent words
    #print(count_all1.most_common(25))
    for hash in count_all2.most_common(30):
        print(hash)

    for hash in count_all2.most_common(30):
        print(hash)
    #print(count_all3.most_common(25))
    #print(count_all4.most_common(15))

    dates_HRanalytics = []
    # f is the file pointer to the JSON data set
    with open(fname, 'r') as f:
        for line in f:
            tweet = json.loads(line)
            # let's focus on hashtags only at the moment
            terms_hash = [term for term in preprocess(tweet['text']) if term.startswith('#')]
            # track when the hashtag is mentioned
            if '#HRAnalytics' in terms_hash:
                dates_HRanalytics.append(tweet['created_at'])

    # a list of "1" to count the hashtags
    ones = [1] * len(dates_HRanalytics)
    # the index of the series
    idx = pd.DatetimeIndex(dates_HRanalytics)
    # the actual series (at series of 1s for the moment)
    HRanalytics = pd.Series(ones, index=idx)
    print(HRanalytics)
    # Resampling / bucketing
    per_minute = HRanalytics.resample('1H', how='sum').fillna(0)
    print(per_minute)
    time_chart = vincent.Line(per_minute)
    time_chart.axis_titles(x='Time', y='Freq')
    time_chart.to_json('time_chart.json')
    print('end')

    # tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, alltweets)
    # tweets_by_country = tweets['country'].value_counts()
    # print(tweets.country.unique())
    # fig, ax = plt.subplots()
    # ax.tick_params(axis='x', labelsize=15)
    # ax.tick_params(axis='y', labelsize=10)
    # ax.set_xlabel('Countries', fontsize=15)
    # ax.set_ylabel('Number of tweets', fontsize=15)
    # ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
    # tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
    #
    # import time\

