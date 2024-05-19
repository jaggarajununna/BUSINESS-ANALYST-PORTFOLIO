#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pymysql as pm
import pandas as pd
import ydata_profiling as yp


# In[36]:


sql=pm.connect(host='localhost',user='root',password='',database='stylelabs')
cursor=sql.cursor()


# In[37]:


dt=pd.read_sql("select * from order_details;",con=sql)


# In[38]:


dt


# In[39]:


yp.ProfileReport(dt)

