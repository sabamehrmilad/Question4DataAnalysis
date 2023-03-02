#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np 


# In[3]:


#Load the dataset 
df = pd.read_csv("country_vaccination_stats.csv")


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.describe()


# In[8]:


# Group by country and fill missing values with minimum daily vaccination number
df["daily_vaccinations"]=df.groupby("country")["daily_vaccinations"].transform(lambda x:x.fillna(x.min()))


# In[9]:


df


# As we can see the in first row daily_vaccinations filled with lowest number of daily_vaccinations

# In[12]:


df.isna().sum()


# So it is clear that we have just one NAN filed in daily_vaccinations

# In[13]:


#filling the missing values with zero
df["daily_vaccinations"] = df["daily_vaccinations"].fillna(0)


# In[14]:


# Save the updated dataset
df.to_csv("vaccinations_imputed.csv", index=False)


# In[ ]:




