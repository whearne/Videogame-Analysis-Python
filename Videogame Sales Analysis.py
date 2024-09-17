#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


df = pd.read_csv(r"C:\Users\Owner\OneDrive\Documents\Data Analyst\Pandas file reading\vgsales.csv")

df


# In[2]:


df.info()


# In[3]:


df.isnull().sum()

df = df[~df.Publisher.isnull()]
df


# In[4]:


df.groupby(["Year", "Platform", "Publisher"])[["EU_Sales", "JP_Sales", "Global_Sales", "Other_Sales", "NA_Sales"]].agg("mean").sort_values(by="Year", ascending=False)


# In[5]:


plt.figure(dpi=80)
sns.countplot(x="Genre", data=df, palette=('flare'), order=df["Genre"].value_counts().index)
plt.xticks(rotation=45, ha="right")
plt.xlabel("Genre")
plt.ylabel("Frequency")
plt.show()


# In[6]:


plt.figure(dpi=80)
sns.countplot(y="Platform", data=df, palette='flare', order=df["Platform"].value_counts().index, orient="h")
plt.xlabel("Frequency")
plt.ylabel("Platform")
plt.show()


# In[7]:


genres_sales = df.groupby("Genre")[["EU_Sales", "JP_Sales", "Global_Sales", "Other_Sales", "NA_Sales"]].agg("mean")

genres_sales


# In[8]:


plt.figure(dpi=100)
sns.heatmap(genres_sales, annot=True, fmt = '.1f')
plt.show()


# In[9]:


genres_sales.corr()


# In[ ]:





# In[ ]:





# In[ ]:




