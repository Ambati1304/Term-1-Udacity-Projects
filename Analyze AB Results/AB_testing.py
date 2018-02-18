# coding: utf-8

# ## Analyze A/B Test Results
# 
# This project will assure you have mastered the subjects covered in the statistics lessons.  The hope is to have this project be as comprehensive of these topics as possible.  Good luck!
# 
# ## Table of Contents
# - [Introduction](#intro)
# - [Part I - Probability](#probability)
# - [Part II - A/B Test](#ab_test)
# - [Part III - Regression](#regression)
# 
# 
# <a id='intro'></a>
# ### Introduction
# 
# A/B tests are very commonly performed by data analysts and data scientists.  It is important that you get some practice working with the difficulties of these 
# 
# For this project, you will be working to understand the results of an A/B test run by an e-commerce website.  Your goal is to work through this notebook to help the company understand if they should implement the new page, keep the old page, or perhaps run the experiment longer to make their decision.
# 
# **As you work through this notebook, follow along in the classroom and answer the corresponding quiz questions associated with each question.** The labels for each classroom concept are provided for each question.  This will assure you are on the right track as you work through the project, and you can feel more confident in your final submission meeting the criteria.  As a final check, assure you meet all the criteria on the [RUBRIC](https://review.udacity.com/#!/projects/37e27304-ad47-4eb0-a1ab-8c12f60e43d0/rubric).
# 
# <a id='probability'></a>
# #### Part I - Probability
# 

# To get started, let's import our libraries.

# In[1]:

import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
#We are setting the seed to assure you get the same answers on quizzes as we set up
random.seed(32)

# `1.` Now, read in the `ab_data.csv` data. Store it in `df`.  **Use your dataframe to answer the questions in Quiz 1 of the classroom.**
# 
# a. Read in the dataset and take a look at the top few rows here:

# In[2]:

df = pd.read_csv('ab_data.csv')
df.head(5)

# b. Use the below cell to find the number of rows in the dataset.

# In[3]:

len(df)


# c. The number of unique users in the dataset.

# In[4]:

len(df['user_id'].unique())


# d. The proportion of users converted.

# In[5]:

100*(len(df[df['converted'] == 1])/len(df))

# e. The number of times the `new_page` and `treatment` don't line up.

# In[6]:

df_treatment = df[df['group'] == 'treatment']
len(df_treatment[df_treatment['landing_page']=='old_page']

# In[7]:

df[((df['group'] == 'treatment') == (df['landing_page'] == 'new_page')) == False].shape[0]

# f. Do any of the rows have missing values?

# In[8]:

df.info()

# For the rows where **treatment** is not aligned with **new_page** , or **control** is not aligned with **old_page**, we cannot be sure if this row truly received the new or old page.
    # Use **Quiz 2** in the classroom to provide how we should handle these rows.  
# # a. Now use the answer to the quiz to create a new dataset that meets the specifications from the quiz.  Store your new dataframe in **df2**.
    
    # In[9]:

x = df[((df['group'] == 'treatment') == (df['landing_page'] == 'new_page')) == False]
y = x.index.get_values()
df2 = df.drop(y)

    
# In[10]:

# Double Check all of the correct rows were removed - this should be 0
df2[((df2['group'] == 'treatment') == (df2['landing_page'] == 'new_page')) == False].shape[0]

    
    # `3.` Use **df2** and the cells below to answer questions for **Quiz3** in the classroom.

# a. How many unique **user_id**s are in **df2**?

# In[11]:

len(df2['user_id'].unique())


# b. There is one **user_id** repeated in **df2**.  What is it?

# In[12]:

df2[df2['user_id'].duplicated()]


# d. Remove **one** of the rows with a duplicate **user_id**, but keep your dataframe as **df2**.

    
    
    
    
    
    
    
    
    
