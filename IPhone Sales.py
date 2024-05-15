#!/usr/bin/env python
# coding: utf-8

# # Project 1 (Iphone Sales Analysis)

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data=pd.read_csv("apple_products.csv")


# In[3]:


data


# In[7]:


print(data.isnull().sum())


# In[4]:


print(data.describe())


# # I Phone Sales Analysis in India

# In[6]:


highest_rated=data.sort_values(by=["Star Rating"],ascending=False)
highest_rated=highest_rated.head(10)
print(highest_rated['Product Name'])


# # Number of ratings on the highest rated I Phone on Flipkart

# In[15]:


iphones=highest_rated["Product Name"].value_counts()
label=iphones.index
counts=highest_rated["Number Of Ratings"]
figure=px.bar(highest_rated,x=label,y=counts,title="Number of ratings of highest rated I Phones")
figure.show()


# In[12]:


iphones


# # Number of reviews on the highest rated I Phone on Flipkart

# In[8]:


iphones=highest_rated["Product Name"].value_counts()
label=iphones.index
counts=highest_rated["Number Of Reviews"]
figure=px.bar(highest_rated,x=label,y=counts,title="Number of reviews of highest rated I Phones")
figure.show()


# In[9]:


figure=px.scatter(data_frame=data,x="Number Of Ratings",y="Sale Price",size="Discount Percentage",trendline="ols",
                 title="Relationship between sale price and number of rating")
figure.show()


# In[17]:


figure=px.scatter(data_frame=data,x='Number Of Ratings',y='Discount Percentage',size='Sale Price',
                 trendline='ols',title='Relationship between Discount Percentage and Number of Ratings')
figure.show()


# In[ ]:




