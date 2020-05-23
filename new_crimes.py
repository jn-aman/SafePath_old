#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from sqlalchemy import create_engine
import mysql.connector as mysql

database_username = 'root'
database_password = 'jainxx'
database_ip       = 'localhost'
database_name     = 'safepath'
database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))



cr = pd.read_sql('SELECT * FROM initial', con=database_connection)
locality=list(cr['localities'])
crime=list(cr.columns)


# In[3]:


localityList = [item.lower() for item in locality]
crimeList=[item.lower() for item in crime]
word=localityList+crimeList


# In[4]:


import tweepy
import json
from dateutil import parser
import time

WORDS = word

CONSUMER_KEY = "eGLtUPqEDKrBWkkkPjnr2lEjb"
CONSUMER_SECRET = "ooxJXCB9D944rUzFQ9txPH4gEPlBlU0abGwSuo8WWlyPCPeuzg"
ACCESS_TOKEN = "140283345-LFqLOC9YjgLQ3YqJI9yuh0qEFUwwl4wIOQpreTJl"
ACCESS_TOKEN_SECRET = "L708vY9b30qPXs4Ftu8maPuZHHG9asNcfozAmyqLe3F3h"
msg=[]

def store_data(text):
    msg.append(text)
    return

class StreamListener(tweepy.StreamListener):    
    #This is a class provided by tweepy to access the Twitter Streaming API. 

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")
 
    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        if (time.time() - start_time) < limit:
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
            try:
               # Decode the JSON from Twitter
                datajson = json.loads(data)

                #grab the wanted data from the Tweet
                text = datajson['text']

                #print out a message to the screen that we have collected a tweet
                text=text.lower()
                if text not in msg:
                    print("Tweet" + str(text))
                    store_data(text)

            except Exception as e:
                print(e)
            return True
        else:
            return False;
            
start_time = time.time()
limit = 300
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True)) 
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track=WORDS)


# In[7]:


db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "jainxx",
    database = "safepath"
)
cursor = db.cursor()

for m in msg:
    for ll in locality:
        for cl in crime[1:8]:
            if ll.lower() in m and cl.lower() in m:
                print(ll,cl)
                cursor.execute("update initial set "+cl+"="+cl+"+1 where localities = '" +ll+"' ;")
db.close();


# In[6]:


msg[1]


# In[ ]:




