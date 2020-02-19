#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
print('-'*10 + "Welcome to Data Vault" + '-'*10)
print("\nThis is the original data")
df=pd.read_csv("Data_Vault_Final1.csv")
df


# In[3]:


df1 = pd.DataFrame(df,index = [0,1,2,], columns = ['type', 'quantity', ])  # to filter only certain columns and rows
df1


# In[ ]:




