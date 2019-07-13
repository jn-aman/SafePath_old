
# coding: utf-8

# In[184]:


import numpy as np
from sklearn.utils import check_random_state
from sklearn.metrics.pairwise import distance_metrics
import math


# In[185]:


import pandas as pd


# In[186]:


# cr = pd.read_csv('crime2.csv')


# In[187]:


# cr.head()


# In[188]:



from sqlalchemy import create_engine
database_username = 'root'
database_password = ''
database_ip       = 'localhost'
database_name     = 'safepath'
database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))
# cr.to_sql('initial', con=database_connection, if_exists='replace',chunksize=1000,index=False)


# In[189]:


cr = pd.read_sql('SELECT * FROM initial', con=database_connection)


# In[190]:


cr.head()


# In[191]:


data = cr.iloc[:,[1,2,3,4,5,6,7,12]].values


# In[192]:


from sklearn.preprocessing import MinMaxScaler
sc_X = MinMaxScaler()
data = sc_X.fit_transform(data)


# In[193]:


data


# In[194]:


import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans


# sse = {}
# for k in range(1, 10):
#     kmeans = KMeans(n_clusters=k, max_iter=1000).fit(data)
#     #print(data["clusters"])
#     sse[k] = kmeans.inertia_ # Inertia: Sum of distances of samples to their closest cluster center
# plt.figure()
# plt.plot(list(sse.keys()), list(sse.values()))
# plt.xlabel("Number of cluster")
# plt.ylabel("SSE")
# plt.show()


# In[195]:


from sklearn.cluster import KMeans
import numpy as np
X = data

kmeans = KMeans(n_clusters=5,random_state=0).fit(X)
kmeans.labels_

pridiction=kmeans.predict(data)


# In[196]:


safety = []
c = 0
for li in kmeans.cluster_centers_:
    sum = 0;
    sum += li[3] + li[5] + li[7]
    safety.append((sum,c))
    c += 1
safety = sorted(safety)


# In[197]:


safety


# In[198]:


dict1 = {}
m = 0
for s in safety:
    dict1[s[1]] = m 
    m += 1


# In[199]:


dict1


# In[200]:


# before
# print(pridiction)


# In[201]:


for i in range(len(pridiction)):
    pridiction[i]=dict1[pridiction[i]]


# In[202]:


# after
# print(pridiction)


# In[203]:


# print(cr["localities"].values)


# In[204]:


import numpy as np
import pandas as pd


X = cr.iloc[0:166, 0].values
y1 = cr.iloc[:, 10].values
y2 = cr.iloc[:, 11].values
y = pridiction
places = cr["localities"].values
new_array= []
for i in range(0, 166):
    str = places[i]+", Delhi, India"
    new_array.append(str)


lati = y2
longi = y1

ar = []
   
for i in range(0, 166):
    y1[i] = round(y1[i], 4)
    y2[i] = round(y2[i], 4)

    o = {  "n": places[i],
            'mag': y[i]  ,                 
            'lati': y1[i], 
            'longi': y2[i]
           
            
        }
    ar.append(o)
loc=pd.DataFrame.from_dict(ar)
loc.to_sql('final', con=database_connection, if_exists='replace',chunksize=1000,index=False)

