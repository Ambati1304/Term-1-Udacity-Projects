# coding: utf-8

# # Which genres are most popular from year to year?

# 
# >import libraries and read the data set

# In[28]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

df = pd.read_csv('tmdb-movies.csv')

# > shape of the data frame

# In[5]:

df.shape


# > Columns of the data frame for better understanding

# In[6]:

df.columns


# > visuvalizing the head of data

# In[7]:

df.head(2)


# >Description of data to clear the null values

# In[8]:

df.info()


# >The column ‘popularity’ has no NaN, so it not needed to drop nulls, but the value counts of the popularity has long list of float values. Which will be hard to analyze. So, we round of the popularity column to nearest integer.

# In[9]:

df['popularity']= round(df['popularity'])


# In[10]:

df.head(2)
