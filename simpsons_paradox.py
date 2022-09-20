#!/usr/bin/env python
# coding: utf-8

# # Simpson's Paradox
# Use `admission_data.csv` for this exercise.

# In[2]:


# Load and view first few lines of dataset
import pandas as pd
df = pd.read_csv ('admission_data.csv')

df.to_csv('E:\raw_data.csv', index=False)


# ### Proportion and admission rate for each gender

# In[12]:


# Proportion of students that are female
(len(df[df['gender']=='female']))/df.shape[0]


# In[13]:


# Proportion of students that are male
(len(df[df['gender']=='male']))/df.shape[0]


# In[14]:


# Admission rate for females
len(df[(df['gender']=='female') & (df['admitted'])])/(len(df[df['gender']=='female']))


# In[15]:


# Admission rate for males
len(df[(df['gender']=='male') & (df['admitted'])])/(len(df[df['gender']=='male']))


# ### Proportion and admission rate for physics majors of each gender

# In[19]:


# What proportion of female students are majoring in physics?
fem_phys_rate = df.query("gender == 'female' & major == 'Physics'").count()/(df.query("gender == 'female'").count())
print (fem_phys_rate)


# In[20]:


# What proportion of male students are majoring in physics?
fem_phys_rate = df.query("gender == 'male' & major == 'Physics'").count()/(df.query("gender == 'male'").count())
print (fem_phys_rate)


# In[21]:


# Admission rate for female physics majors
len(df[(df["gender"]=='female') & (df["major"] == 'Physics') & df["admitted"]]) / len(df[(df["gender"]=='female') & (df["major"] == 'Physics')])


# In[ ]:


# Admission rate for male physics majors
len(df[(df["gender"]=='male') & (df["major"] == 'Physics') & df["admitted"]]) / len(df[(df["gender"]=='male') & (df["major"] == 'Physics')])


# ### Proportion and admission rate for chemistry majors of each gender

# In[ ]:


# What proportion of female students are majoring in chemistry?
len(df[(df['gender']=='female') & (df['major'] == 'Chemistry')]) / len(df[df['gender']=='female'])


# In[22]:


# What proportion of male students are majoring in chemistry?
len(df[(df['gender']=='male') & (df['major'] == 'Chemistry')]) / len(df[df['gender']=='male'])


# In[23]:


# Admission rate for female chemistry majors
len(df[(df['gender']=='female') & (df['major'] == 'Chemistry') & df['admitted']]) / len(df[(df['gender']=='female') & (df['major'] == 'Chemistry')])


# In[ ]:


# Admission rate for male chemistry majors
len(df[(df['gender']=='male') & (df['major'] == 'Chemistry') & df['admitted']]) / len(df[(df['gender']=='male') & (df['major'] == 'Chemistry')])


# ### Admission rate for each major

# In[ ]:


# Admission rate for physics majors
len(df[(df['major'] == 'Physics') & df['admitted']]) / len(df[(df['major'] == 'Physics')])


# In[ ]:


# Admission rate for chemistry majors

len(df[(df['major'] == 'Chemistry') & df['admitted']]) / len(df[(df['major'] == 'Chemistry')])

