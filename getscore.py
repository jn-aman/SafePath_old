
# coding: utf-8

# In[4]:


import numpy as np
from sklearn.utils import check_random_state
from sklearn.metrics.pairwise import distance_metrics
import math
import pandas as pd


# In[7]:


# from sqlalchemy import create_engine
# database_username = 'b5a53e446f5cec'
# database_password = '0f8d1ba3'
# database_ip       = 'us-cdbr-iron-east-02.cleardb.net'
# database_name     = 'heroku_7c3443583b90116'
# database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
#                                                format(database_username, database_password, 
# #                                                       database_ip, database_name))
# cr.to_sql('initial', con=database_connection, if_exists='replace',chunksize=1000,index=False)


# In[6]:



from sqlalchemy import create_engine
database_username = 'root'
database_password = 'jainxx'
database_ip       = 'localhost'
database_name     = 'safepath'
database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))
cr = pd.read_sql('SELECT * FROM final', con=database_connection)


# In[7]:


print(cr.to_dict('r'))

