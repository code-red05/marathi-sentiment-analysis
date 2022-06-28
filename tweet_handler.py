# Marathi Reviews and Opinion Analysis using NLP

import marathi_classifier

import re
import time
import sys

import tweepy

#required tokens for twitter api authentication
#
auth_key = "RDRAeYNcZaSLvOOBXr3VuKVsy"
auth_secret = "3O7nIA7cJsyucARvHL9p8wJHDmZ4DMzoZ720IqinpaqotxlPlR"

auth = tweepy.AppAuthHandler(auth_key, auth_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)



#Authenticating with given tokens
if (not api):
  print ("Authentiation Failed!")
  sys.exit(-1)

def get_tweets(query, ui):  #
  tweet_counter=0
  neg_count=0
  pos_count=0

  while tweet_counter < 50:   #atleast 50 tweets
    try:
      #getting tweets
      tweets_list = api.search(q=query, lang="mr", count=50)
      for tweet in tweets_list:   #
        Tweet = tweet.text

        #Convert @username to User
        Tweet = re.sub('@[^\s]+','TWITTER_USERNAME',Tweet)
        
        #Remove additional white spaces
        Tweet = re.sub('[\s]+', ' ', Tweet)
        
        #Remove hashtags
        Tweet = re.sub(r'#([^\s]+)', r'\1', Tweet)

        #Replace urls with the phrase 'URL' for easy processing
        Tweet = re.sub('((www\.[\s]+)|(https?://[^\s]+))','URL',Tweet)
        
        #trim
        Tweet = Tweet.strip('\'"')
        
        #Deleting common happy and sad emoticon from the tweet 
        Tweet = Tweet.replace(':)','')
        Tweet = Tweet.replace(':(','')
        
        #Deleting the Twitter @username tag and reTweets 
        retweet = 'RT'
        Tweet = Tweet.replace('TWITTER_USERNAME','')

        if retweet in Tweet:
          continue

        Tweet = Tweet.replace('URL','')
        result = marathi_classifier.classify_text(Tweet)    #

        ui.textBrowser_2.append(Tweet + "\n" + result + "\n\n")
        
        if result == "negative":
          neg_count+=1
        elif result == "positive":
          pos_count+=1

        tweet_counter+=1


    except tweepy.TweepError as e:
      print("Error : " + str(e))
      print("Retrying in 10 seconds...")
      time.sleep(10)
  
  print("Total tweets found: "+ str(tweet_counter))
  if tweet_counter==0:
    tweet_counter = 1

  percent_pos = ((float(pos_count)/tweet_counter)*100)    #
  percent_neg = ((float(neg_count)/tweet_counter)*100)
  print("Positive: {0}%".format(percent_pos))
  print("Negative: {0}%".format(percent_neg))
  return percent_pos, percent_neg, pos_count, neg_count
  

def main(keyword, ui):
  print("\nFetching tweets with keyword '{0}':\n".format(keyword))
  percent_pos, percent_neg, pos_count, neg_count = get_tweets(keyword, ui)
  return percent_pos, percent_neg, pos_count, neg_count
  
if __name__ == "__main__":
  main()