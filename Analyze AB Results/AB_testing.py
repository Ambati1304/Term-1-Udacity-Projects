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

# In[13]:

df2 = df2.drop(df2[df2['user_id'].duplicated()].index.get_values())    
    
    
    
# `4.` Use **df2** in the below cells to answer the quiz questions related to **Quiz 4** in the classroom.
# 
# a. What is the probability of an individual converting regardless of the page they receive?

    
    # In[14]:

len(df2[df2['converted'] == 1])/len(df2)


# b. Given that an individual was in the `control` group, what is the probability they converted?

# In[15]:

p_con = len(df2[((df2['group'] == 'control') & (df2['converted'] == 1))])/len(df2[df2['group']=='control']) 
p_con

    # c. Given that an individual was in the `treatment` group, what is the probability they converted?

# In[16]:

p_trt = len(df2[((df2['group'] == 'treatment') & (df2['converted'] == 1))])/len(df2[df2['group']=='treatment']) 
p_trt

    # d. What is the probability that an individual received the new page?

# In[17]:

len(df2[df2['landing_page'] == 'new_page'])/len(df2) 

    # e. Use the results in the previous two portions of this question to suggest if you think there is evidence that one page leads to more conversions?  Write your response below.

# ><b>`1.` We observe that the landing into either new page or old page are equally probable </b> <br/>
# ><b>`2.` From the observations above we have evidence that given a particular group the probability for conversions are 0.1</b> <br/>
# ><b>`3.` Looking at the analysis above, It would be better to make the experiment run little longer, or use a different statistical tool to analyse better </b> <br/>

# <a id='ab_test'></a>
# ### Part II - A/B Test
# 
# Notice that because of the time stamp associated with each event, you could technically run a hypothesis test continuously as each observation was observed.  
# 
# However, then the hard question is do you stop as soon as one page is considered significantly better than another or does it need to happen consistently for a certain amount of time?  How long do you run to render a decision that neither page is better than another?  
# 
# These questions are the difficult parts associated with A/B tests in general.  
# 
# 
# `1.` For now, consider you need to make the decision just based on all the data provided.  If you want to assume that the old page is better unless the new page proves to be definitely better at a Type I error rate of 5%, what should your null and alternative hypotheses be?  You can state your hypothesis in terms of words or in terms of **$p_{old}$** and **$p_{new}$**, which are the converted rates for the old and new pages.

# <b>`1.` Null Hypothesis: </b> <br/>
# > the difference in conversion rates for old page and new page will be zero, i.e. P(old) will be equal to P(new)
# 
# <b>`2.` Alternative Hypothesis: </b> <br/>
# > the difference in conversion rates for old page and new page will be different
# 
    
# `2.` Assume under the null hypothesis, $p_{new}$ and $p_{old}$ both have "true" success rates equal to the **converted** success rate regardless of page - that is $p_{new}$ and $p_{old}$ are equal. Furthermore, assume they are equal to the **converted** rate in **ab_data.csv** regardless of the page. <br><br>
# 
# Use a sample size for each page equal to the ones in **ab_data.csv**.  <br><br>
# 
# Perform the sampling distribution for the difference in **converted** between the two pages over 10,000 iterations of calculating an estimate from the null.  <br><br>
# 
# Use the cells below to provide the necessary parts of this simulation.  If this doesn't make complete sense right now, don't worry - you are going to work through the problems below to complete this problem.  You can use **Quiz 5** in the classroom to make sure you are on the right track.<br><br>
# a. What is the **convert rate** for $p_{new}$ under the null? 

# In[18]:

p_new = len(df2[df2['converted'] == 1])/len(df2)
p_new


# In[19]:

p_old = len(df2[df2['converted'] == 1])/len(df2)
p_old
# b. What is the **convert rate** for $p_{old}$ under the null? <br><br>

# In[20]:

len(df2[df2['converted'] == 1])/len(df2)
# c. What is $n_{new}$?

# In[21]:

n_new = len(df2[df2['landing_page']=='new_page'])
print(n_new)
# d. What is $n_{old}$?

# In[22]:

n_old=len(df2[df2['landing_page']=='old_page'])
n_old
    
    # e. Simulate $n_{new}$ transactions with a convert rate of $p_{new}$ under the null.  Store these $n_{new}$ 1's and 0's in **new_page_converted**.

# In[23]:

new_page_converted = np.random.choice(2,n_new,p=[0.8804,0.1196])
    
    # f. Simulate $n_{old}$ transactions with a convert rate of $p_{old}$ under the null.  Store these $n_{old}$ 1's and 0's in **old_page_converted**.

# In[24]:

old_page_converted = np.random.choice(2,n_old,p=[0.8804,0.1196])

# g. Find $p_{new}$ - $p_{old}$ for your simulated values from part (e) and (f).

# In[25]:

p_new = np.count_nonzero(new_page_converted)/len(new_page_converted)
p_old = np.count_nonzero(old_page_converted)/len(old_page_converted)
a = p_new - p_old
print("%.5f" % a)
    
    # h. Simulate 10,000 $p_{new}$ - $p_{old}$ values using this same process similarly to the one you calculated in parts **a. through g.** above.  Store all 10,000 values in **p_diffs**.
# In[26]:

p_diffs=[]
for _ in range(10000):
    new_page_converted = np.random.choice([0,1],n_new,p=[0.8804,0.1196])
    p_new = np.count_nonzero(new_page_converted)/len(new_page_converted)
    old_page_converted = np.random.choice([0,1],n_old,p=[0.8804,0.1196])
    p_old = np.count_nonzero(old_page_converted)/len(old_page_converted)
    p_diffs.append(p_new - p_old)
    
    # i. Plot a histogram of the **p_diffs**.  Does this plot look like what you expected?  Use the matching problem in the classroom to assure you fully understand what was computed here.

# In[27]:

p_diffs = np.array(p_diffs)
plt.hist(p_diffs)
    
    # j. What proportion of the **p_diffs** are greater than the actual difference observed in **ab_data.csv**?

# In[28]:

p_diffs_actual =-0.1203 + 0.1188 
greater_than_diff = [i for i in p_diffs if i > (p_diffs_actual)]
print('Proportion greater than actual difference:', len(greater_than_diff)/len(p_diffs))

# In[29]:

n = p_diffs.mean()


# In[37]:

(p_diffs<p_diffs_actual).mean()+(p_diffs>p_diffs+(n-p_diffs_actual)).mean()

    # k. In words, explain what you just computed in part **j.**.  What is this value called in scientific studies?  What does this value mean in terms of whether or not there is a difference between the new and old pages?

# > we now have evidence, with the P-value caluclated above, that the difference in conversions in old page and new page are equal.i.e we may decide to run the experiment to run a little longer.

# l. We could also use a built-in to achieve similar results.  Though using the built-in might be easier to code,
    #the above portions are a walkthrough of the ideas that are critical to correctly thinking about statistical significance. 
    #Fill in the below to calculate the number of conversions for each page, as well as the number of individuals 
  #  who received each page. 
  #  Let `n_old` and `n_new` refer the the number of rows associated with the old page and new pages, respectively
