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
