# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

df = pd.read_csv('tmdb-movies.csv')

# In[2]:

df.head(2)


# In[3]:

df.info()


# ## mean_revenue, mean_budget over the year

# In[4]:

yearly_stats = df.groupby('release_year').mean().reset_index()
