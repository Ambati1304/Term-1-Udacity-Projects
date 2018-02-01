
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

# In[5]:


budget_means = yearly_stats['budget']


ind = np.arange(1960,2016)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, budget_means, width, color='r')

revenue_means = yearly_stats['revenue']

rects2 = ax.bar(ind + width, revenue_means, width, color='y')

# add some text for labels, title and axes ticks
ax.set_ylabel('Amount in USD')
ax.set_xlabel('Year')
ax.set_title('Trend of investment over years')


ax.legend((rects1[0], rects2[0]), ('budget', 'revenue'))



plt.show()

# ## companys most produced genre

# In[6]:

yearly_profit = np.subtract(yearly_stats['revenue'],yearly_stats['budget'])

# In[25]:

plt.plot(yearly_stats['release_year'],yearly_profit)
plt.xlabel('year')
plt.ylabel('difference of budget and revenue')

# In[8]:

df['profit'] = np.subtract(df['revenue'],df['budget'])

# In[31]:

df['production_companies']


# ## Most number of Genres produced by a Company

# In[32]:

x=df[df['production_companies'] == 'Warner Bros.']['genres'].value_counts()[0:10]
plt.pie(x,labels=x.index.tolist()); 

# ## most revenue producing genres for a  production company

# In[11]:

df.isnull().sum()




