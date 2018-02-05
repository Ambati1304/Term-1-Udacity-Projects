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


# >Now, value counts of popularity counts looks as.

# In[11]:

df['popularity'].value_counts()

# >But there are outliers we need popularity on scale 10, so we drop the rows with popularity above 9.0. 

# In[12]:

df = df[df['popularity'] <= 9.0]

# >This is how the popularity looks after cleaning.

# In[13]:

df['popularity'].value_counts()

# >We then check for duplicated rows and drop them

# In[14]:

df[df.duplicated()]

# In[15]:

df = df.drop(2090)


# In[16]:

df[df.duplicated()]


# In[17]:

df.shape

