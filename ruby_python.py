
import numpy as np
from sklearn.utils import check_random_state
from sklearn.metrics.pairwise import distance_metrics
import math
import pandas as pd
from sqlalchemy import create_engine
from sklearn.cluster import KMeans

database_username = 'root'
database_password = 'jainxx'
database_ip       = 'localhost'
database_name     = 'safepath'
database_connection = create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                               format(database_username, database_password, 
                                                      database_ip, database_name))

cr = pd.read_sql('SELECT * FROM initial', con=database_connection)
cr.head()
data = cr.iloc[:,[1,2,3,4,5,6,7,12]].values
from sklearn.preprocessing import MinMaxScaler
sc_X = MinMaxScaler()
data = sc_X.fit_transform(data)

X = data

kmeans = KMeans(n_clusters=5,random_state=0).fit(X)
kmeans.labels_

pridiction=kmeans.predict(data)

safety = []
c = 0
for li in kmeans.cluster_centers_:
    sum = 0;
    sum += li[3] + li[5] + li[7]
    safety.append((sum,c))
    c += 1
safety = sorted(safety)


safety

dict1 = {}
m = 0
for s in safety:
    dict1[s[1]] = m 
    m += 1

for i in range(len(pridiction)):
    pridiction[i]=dict1[pridiction[i]]

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

