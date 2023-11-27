#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


# In[19]:


df=pd.read_csv("pokemon_alopez247.csv")
df.head()


# In[20]:


df.shape


# In[21]:


#Checking the null values
df.isnull().sum()


# In[22]:


df.info()


# In[23]:


df.describe()


# In[24]:


df=df.drop(['Type_2','Egg_Group_1'], axis=1)
df.head()


# In[25]:


df.duplicated().sum() #Checking if any rows are duplicated


# In[26]:


df=df.rename(columns={'Type_1':'Type','Egg_Group_2':'Egg_Group'})
df.head()


# In[27]:


#No of pokemons that have Mega Evolution
df['hasMegaEvolution'].values.sum()


# In[28]:


#Filling the missing values with median as it has outliers
df=df.fillna(df.Pr_Male.median())
df.isnull().sum()


# In[29]:


df.info()


# In[30]:


Y_pokaemons=df[df['Color']=='Yellow']  #we have 63 yellow pokaemons after analysis
Y_pokaemons


# In[31]:


#average catch rates 
average_catch_rate=df['Catch_Rate'].mean()
average_catch_rate


# In[32]:


#No of pokaemons that have mega evolution
mega_evolution=df[df['hasMegaEvolution']==True]
mega_evolution


# In[33]:


#no of different colors 
df['Color'].unique()


# In[34]:


#Pokaemons with height greater than 0.5 meters
print(df['Height_m']>1.5).values_counts()


# In[35]:


#Visualization
#Pie chart for percentage of colored pokaemons
color_set=set(df['Color'])
parts=[
    

    df['Color'].value_counts()['Yellow'],
    df['Color'].value_counts()['Green'],
    df['Color'].value_counts()['Red'],
    df['Color'].value_counts()['Blue'],
    df['Color'].value_counts()['White'],
    df['Color'].value_counts()['Purple'],
    df['Color'].value_counts()['Pink'],
    df['Color'].value_counts()['Black'],
    df['Color'].value_counts()['Grey'],
    df['Color'].value_counts()['Brown']
]

plt.pie(parts, colors=color_set, labels=color_set, radius=1.7, shadow=True, autopct='%1.1f%%')
plt.title('Pokaemons with distinct colors', x=0.75, y=1.4)
plt.show()


# In[36]:


#Scatterplot for catch rate vs weight of the pokaemon
x=df['Weight_kg']
y=df['Catch_Rate']

plt.scatter(x,y)
plt.xlabel("Weight of the pokaemon")
plt.ylabel("catch rate")
plt.title("Weight of the pokaemon vs their catch rate")
plt.show()


# In[37]:


#Correlation map
plt.figure(figsize=(15,15))
sns.heatmap(df.corr(), annot=True, cmap='viridis')


# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




