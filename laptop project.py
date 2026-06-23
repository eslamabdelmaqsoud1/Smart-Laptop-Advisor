#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data=pd.read_excel("laptop.xlsx")


# In[51]:


data.head()


# In[52]:


data.shape


# In[53]:


data.info()


# In[54]:


data.isna().sum()


# In[55]:


data.dropna(axis=0,inplace=True)


# In[57]:


data.reset_index(inplace=True)
data.drop(['index','level_0'],axis=1,inplace=True)


# In[58]:


data.head()


# In[59]:


data.shape


# In[61]:


data['Date'].unique()


# In[38]:


data['brand'].unique()


# In[39]:


data['model_name'].unique()


# In[40]:


data['processor_name'].unique()


# In[43]:


data['ram(GB)'].unique()


# In[44]:


data['ssd(GB)'].unique()


# In[45]:


data['Hard Disk(GB)'].unique()


# In[48]:


data['Operating System'].unique()


# In[49]:


data['graphics'].unique()


# In[62]:


data=data[data['graphics']!="Missing"]


# In[63]:


data['graphics'].unique()


# In[56]:


data.shape


# In[57]:


data['screen_size(inches)'].unique()


# In[62]:


data['resolution (pixels)'].unique()


# In[63]:


data['no_of_cores'].unique()


# In[64]:


data['no_of_threads'].unique()


# In[65]:


data['spec_score'].unique()


# In[67]:


data['Used Price (EGP)'].unique()


# In[64]:


data.duplicated().sum()


# In[65]:


data.head()


# In[66]:


data.drop(['number'],axis=1,inplace=True)


# In[67]:


data.head()


# In[68]:


def laptop_user(ram):
    if ram<=8:
        return "Normal"
    elif ram<=16:
        return "Gamer"
    else:
        return "Designer"


# In[69]:


data['laptop_user']=data['ram(GB)'].apply(laptop_user)


# In[70]:


data.head()


# In[95]:


brand_counts=data['brand'].value_counts()
plt.figure(figsize=(10,8))
plt.pie(brand_counts,labels=brand_counts.index,autopct='%1.1f%%')
plt.title("brands distribution")
plt.show()


# In[100]:


plt.figure(figsize=(10,7))
sns.histplot(data['Used Price (EGP)'],kde=True)
plt.title("price distribution")
plt.show()


# In[155]:


laptop_counts=data['model_name'].value_counts().head(10)
plt.figure(figsize=(35,20))
sns.barplot(x=laptop_counts.index,y=laptop_counts.values)
plt.xlabel("laptop")
plt.ylabel("count")
plt.title("top 10 laptop sales")
plt.show()


# In[145]:


total_sales=data.groupby('brand')['Used Price (EGP)'].sum()
plt.figure(figsize=(25,10))
sns.barplot(x=total_sales.index,y=total_sales.values)
plt.xlabel("brand")
plt.ylabel("total sales")
plt.title("total sales for brand")
plt.show()


# In[171]:


processor_count=data['processor_name'].value_counts().head(10)
plt.figure(figsize=(20,7))
sns.barplot(x=processor_count.index,y=processor_count.values)
plt.xlabel("processor")
plt.ylabel("count")
plt.title("top 10 processors")
plt.show()


# In[169]:


plt.figure(figsize=(10,7))
sns.barplot(x=data['ram(GB)'],y=data['ram(GB)'].value_counts())
plt.show()


# In[174]:


operating_system_counts=data['Operating System'].value_counts()
plt.figure(figsize=(15,9))
plt.pie(operating_system_counts,labels=operating_system_counts.index)
plt.title("operating system distribution")
plt.show()


# In[188]:


graphics_counts=data['graphics'].value_counts().head(10)
plt.figure(figsize=(30,7))
sns.barplot(x=graphics_counts.index,y=graphics_counts.values)
plt.xlabel("graphics")
plt.ylabel("counts")
plt.title("top 10 graphics")
plt.show()


# In[6]:


plt.figure(figsize=(10,7))
sns.scatterplot(x=data['ssd(GB)'],y=data['Hard Disk(GB)'],hue=data['Used Price (EGP)'])
plt.xlabel("SSD")
plt.ylabel("HDD")
plt.title("SSD with HDD")
plt.show()


# In[ ]:




