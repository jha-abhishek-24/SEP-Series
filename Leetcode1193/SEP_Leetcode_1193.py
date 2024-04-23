#!/usr/bin/env python
# coding: utf-8

# ### 1193 monthly-transactions

# In[29]:


import pandas as pd


# In[30]:


# read pdf
df_1 = pd.read_csv(r'C:\SEP\Leetcode1193\raw_Data_for_leetcode1193.csv')
# load data 
df_1.head(10)


# In[31]:


print("Data types of columns:")
print(df_1.dtypes)


# In[32]:


# Convert trans_date to datetime type
df_1['trans_date'] = pd.to_datetime(df_1['trans_date'])

# Extract month and year in yyyy-mm format
df_1['month'] = df_1['trans_date'].dt.to_period('M')



df_1.head(10)


# In[33]:


# group the data as per SQL-like operation 
result = df_1.groupby(['month', 'country']).agg(
    trans_count=('id', 'count'),
    approved_count=('state', lambda x: sum(x == 'approved')),
    trans_total_amount=('amount', 'sum'),
    approved_total_amount=('amount', lambda x: x[df_1['state'] == 'approved'].sum())).reset_index()


print("The final result is:")
result.head(10)


# In[ ]:




