
# coding: utf-8

# In[3]:


import pandas as pd
#import plotly.plotly as py
#from plotly.graph_objs import *
df1 = pd.read_csv("pointcloud2.csv")
#print(df1)


# In[4]:


df1.head()


# In[5]:


df1.describe()


# In[6]:


df1.plot()

