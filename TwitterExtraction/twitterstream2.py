import tweepy
from tweepy import OAuthHandler

consumer_key = 'sIj5Wq5MWxikbT49SjgOGirmY' #supply the appropriate value
consumer_secret = '37fl8M20O0iQoSrzMHmrbBEezhIABUdV8RUxASjo85ivAG5bWU'
access_token = '1072162742-YrxnXbr4p3dh8gbNdn1LjBeyvpsnOVFQRovP2Vf'
access_secret = 'Nwj2JzWpcHmy0l31RTJeicen5lTClgmRTbPE5nozGjeCX'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):

    def on_data(self, data):
        try:
            with open('twitter.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#HROS','#HRanalytics', '#peopleAnalytics',
                             '#workforceAnalytics', '#performancemanagement','#peoplemanagement',
                             '#SmarterHR','#beyondhrforum','#HRtech','#FutureofHR',
                             '#IBMKenexa','#RecruitWithData','#hrTrends','#hrdata','#hrm','#hcm',
                             '#employerbranding','#recruitmentanalytics', '#talentanalytics', '#CHRO',
                             '#engagementanalytics','#retentionanalytics','#learninganalytics',
                             '#employeeanalytics','#quantifiedemployee','#leaderschipanalytics',
                             '#smaterworkforce','#wfas2015', '#wfas2016'])

