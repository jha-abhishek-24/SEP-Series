#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd


# In[23]:


# Specifying the path to your Excel file
file_path = r"C:\SEP\Leetcode1045\raw_data_leetcode_1045.xlsx"

# Reading all sheets using read_excel with sheet_name=None
data = pd.read_excel(file_path, sheet_name=None)


# In[31]:


# Accessing each sheet by its sheet name
customer_df = data["customer"]  
product_df = data["product"]  

# You can now work with each sheet's data separately using pandas methods
print(customer_df.head(5))  # Displaying the first few rows of sheet1
print(product_df.tail(5))  # Displaying the last few rows of sheet2


# In[32]:


# Group by customer_id and count the distinct product_keys
grouped = customer_df.groupby('customer_id')['product_key'].nunique() 

print(grouped.head(5))


# In[33]:


# Find the count of distinct product_keys across all products
total_product_keys = product_df['product_key'].nunique()
print(total_product_keys)


# In[34]:


# Filter customer_ids where the count of distinct product_keys matches total_product_keys
result = grouped[grouped == total_product_keys].index.tolist()

print("Customer IDs:", result)

