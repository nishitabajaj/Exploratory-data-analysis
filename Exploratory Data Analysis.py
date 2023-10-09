#!/usr/bin/env python
# coding: utf-8

# # Exploratory Data Analysis
# 

# # BY : NISHITA BAJAJ
# 

# ## In this task, we will try to find out the weak areas where we can work to find out the areas of profit as a business manager.

# # Importing the data

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# # Collecting the data

# In[2]:


df = pd.read_csv("C:\\Users\\Nishita Bajaj\\Downloads\\SampleSuperStore.zip")
print("Data imported successfully")


# # Data Preprocessing

# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df.isna().sum()


# In[6]:


df.dtypes


# In[7]:


df.describe()


# In[8]:


df.info()


# In[9]:


df.sample(5)


# # Dropping the postal code column 

# In[10]:


df.drop(["Postal Code"], axis = 1, inplace = True)


# In[11]:


df.head()


# In[12]:


df.shape


# In[13]:


df2 = df.select_dtypes(include=["object","float64","int64"]).columns.tolist()


# In[14]:


df2


# In[15]:


for i in df[df2]:
    display(df[i].unique())


# # Visualizing the data

# ## Visualizing the relationship between sales and profit

# In[16]:


plt.title("Sales VS Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.scatter(df["Sales"],df["Profit"],marker="*",color="r")
plt.show()


# ### The scatter plot drawn above indicates that if the sales are low, then the organization will run into loss but if the company make more sales then profit would be more.

# ## Visualizing the relationship between discount and profit

# In[17]:


plt.title("Discount VS Profit")
plt.xlabel("Dicount")
plt.ylabel("Profit")
plt.scatter(df["Discount"],df["Profit"],marker="*",color="b")
plt.plot()


# ### The above plot indicates that if the discount is less, the profit would be more and if the discount is increased,the profit would decrease.Therefore the company should not offer the discount more the 20% to avoid the condition of loss.

# In[18]:


df.head()


# ## Ship Mode visualization

# In[19]:


plt.figure(figsize = (10,5))
sns.countplot(x = "Ship Mode", data = df)
plt.show()


# ### The above plot indicates that ship mode with standard class has positive relationship with the profits as it improves battery life during shipment stage which would result in fast shipment. If shipment is fast, then sales would be   more and profit would automatically increase.

# In[20]:


df.head()


# ## Segment Data Visualization

# In[21]:


plt.figure(figsize = (10,5))
sns.countplot(x = "Segment", data = df)
plt.show()


# ### The above plot shows that the consumer segment purchases more of the company's products. Therefore, the company should focus on more consumer products and increase their sale which will eventually increase the profit.

# In[22]:


df.head()


# # State Visualization

# In[23]:


plt.figure(figsize = (12,5))
sns.countplot(x = df["State"], data = df)
plt.xticks(rotation = (75))
plt.show()


# ### The above plot indicates that the people who are located at California,Washington Texas, Nebraska, Pennyslavnia, Illinois and New York purchase more products of the company. Therefore , the company should increase the sales in these states which will result in increment in profit.

# In[24]:


df.head()


# In[25]:


df["Country"].unique()


# ### It concludes that the people from the United States only purcahse the company's product.

# In[26]:


df.head()


# # Region visualization

# In[27]:


df.Region.unique()


# In[28]:


plt.figure(figsize = (10,5))
sns.countplot(x = df["Region"], data = df)
plt.show()


# ### The above plot indicates the highest sales of company's product in the western and eastern regions.

# In[29]:


df.head()


# # Category visualization

# In[30]:


df.Category.unique()


# In[31]:


plt.figure(figsize = (10,5))
sns.countplot(x = "Category", data = df)
plt.show()


# In[32]:


df.head()


# # Sub-Category visualization

# In[33]:


df["Sub-Category"].unique()


# In[34]:


plt.figure(figsize = (12,5))
sns.countplot(x = df["Sub-Category"], data = df)
plt.xticks(rotation = (60))
plt.show()


# # Thank You !!
