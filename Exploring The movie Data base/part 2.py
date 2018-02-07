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

# >With the following data frame, we have many genres, most of the genres have little movies associated with them, which are trivial for our analyzation, so we filter them out.

# In[18]:

df = df.groupby("genres").filter(lambda x: len(x) >= 50)

# >we just used groupby to filter out genre elements whose contents are more than 50, i.e we dropped genres with movies less than 50.

# In[19]:

df.shape

# In[20]:

df['genres'].value_counts()


# >We groupby release_year and genres column and take the mean of the popularity column, we use mean over sum, because sum overlooks the importance of genres of little movies but with more popularity, so we take mean of popularity column

# In[21]:

res = df.groupby(['release_year','genres'])['popularity'].mean().reset_index()

# >We then take the list of all genres with maximum popularity in each year.

# In[22]:

sol = list()
for year in res['release_year'].unique():
    sol.append(res.loc[(res[res['release_year']==year]['popularity'].max()==res['popularity']) & (res['release_year']==year)])

# >Now we define a function to get the most popular genres for a given year.

# In[2]:

def popular_genre(year):
    for i in range(len(sol)):
        if all(sol[i]['release_year']==year):
            return sol[i]['genres'], plt.pie(res[res['release_year']==year]['popularity'],labels= res[res['release_year']==year]['genres']);




