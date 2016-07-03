import json
from nltk.tokenize import word_tokenize
import re
import operator
import json
from collections import Counter
from nltk.corpus import stopwords
import string


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

with open(fname, 'r') as f:
    count_all1 = Counter()
    count_all2 = Counter()
    count_all3 = Counter()
    count_all4 = Counter()
    for line in f:
        tweet = json.loads(line)
        if (tweet['lang'] == 'en'):
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

    #print(count_all3.most_common(25))
    #print(count_all4.most_common(15))
