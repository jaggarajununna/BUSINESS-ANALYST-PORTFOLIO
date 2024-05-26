#!/usr/bin/env python
# coding: utf-8

# Import required libraries

# In[185]:


import pandas as pd
import numpy as np
import ydata_profiling as yp


# Import dataset

# In[18]:


dt = pd.read_csv("D:\\datasets\\data cleaning.csv")


# Descriptive stats of data

# In[186]:


yp.ProfileReport(dt)


# In[19]:


dt


# cleaning the dataset

# In[107]:


dt['marks']=dt['marks'].str.strip('[!#$%@}{][\|^&''""*^)(]')


# In[105]:


dt['name']=dt['name'].str.strip('[!#$%@}{][\|^&''""*^)(1234567890]')


# In[178]:


dt=dt.iloc[:20]


# In[180]:


dt=dt.fillna(' ')


# In[181]:


dt

