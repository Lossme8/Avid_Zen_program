#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
print('-'*10 + "Welcome to Data Vault" + '-'*10)
print("\nThis is the original data")
df=pd.read_csv("Data_Vault_Final1.csv")
df


# In[45]:


# targetting only products
# print("The below data only shows PRODUCTS column\n\n" ,df['products'])
# Defining the variables
x=df['type']
#df = pd.DataFrame(x)
plt.xticks(rotation=45)
plt.title('products vs type graph')
plt.xlabel('TYPE')
plt.ylabel('PRODUCTS')
y = df['products']
# Plotting a graph of type vs products
plt.plot(x,y, )


# In[26]:


# targetting price and type
x=df.loc[:,'type']
plt.xticks(rotation=45)
plt.title('price vs type graph')
plt.xlabel('TYPE')
plt.ylabel('PRICE')
y = df.loc[:,'price']
# Plotting a graph of type vs products
plt.plot(x,y)
print("The below data only shows TYPE vs PRICE columns\n\n" ,df[['price','type'] ])


# In[36]:


# targetting type and quantity
x=df.loc[:,'type']
plt.xticks(rotation=45)
plt.title('type vs quantity graph')
plt.xlabel('TYPE')
plt.ylabel('quantity')
y = df.loc[:,'quantity']
# Plotting a graph of type vs products
plt.plot(x,y, 'g*-')
print("The below data only shows PRODUCTS, type and quantity\n\n" ,df[['products','type', 'quantity'] ])


# In[90]:


print(x[:3]) # this is a slice function to target 
#print(y[:3])
#plt.plot(x[:3])


# In[43]:


# All data
# print("The below data only shows PRODUCTS column\n\n" ,df['products'])
# Defining the variables
#x=df['type']
plt.xticks(rotation=45)
plt.title('products vs type graph')
plt.xlabel('TYPE')
plt.ylabel('PRODUCTS')
y = df['price']
# Plotting a graph of type vs products
plt.hist(y, color='purple')
#plt.plot(x,y)


# In[32]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#print('-'*10 + "Welcome to Data Vault" + '-'*10)
print("\nThis is the original data")
df=pd.read_csv("Data_Vault_Final.csv")
#for index,row in df.iterrows():
    #print(index,row)


# In[8]:


df.columns
print(df[['type','price']])


# In[59]:


df=pd.read_csv("Data_Vault_Final.csv")
df1 = pd.DataFrame(df,index = [0,1,2,], columns = ['type', 'quantity', ]) 

plt.xticks(rotation=45)
plt.title('TYPE vs QUANTITY graph')
plt.xlabel('TYPE')
plt.ylabel('QUANTITY')
print(df1)
x=df1.loc[:,'type']
y=df1.loc[:,'quantity']
plt.plot(x,y)


# In[49]:


df.columns


# In[38]:


df=pd.read_csv("Data_Vault_Final.csv")
df1 = pd.DataFrame(df,index = [0,1,2,], columns = ['type', 'price', ]) 
df1.columns

plt.xticks(rotation=45)
plt.title('TYPE vs PRICE graph')
plt.xlabel('TYPE')
plt.ylabel('PRICE')
print(df1)
x=df1.loc[:,'type']
y=df1.loc[:,'price']
plt.grid('.')
plt.plot(x,y)


# In[93]:


df=pd.read_csv("Data_Vault_Final.csv")
#print(df)
df2 = pd.DataFrame(df,index = [3,4,5,], columns = ['type', 'price', ]) 
print(df1.columns)

plt.xticks(rotation=45)
plt.title('TYPE vs PRICE graph')
plt.xlabel('TYPE')
plt.ylabel('PRICE')
print(df1)
x=df2.loc[:,'type']
y=df2.loc[:,'price']
df2['price'].plot(kind='bar')


# In[41]:


df=pd.read_csv("Data_Vault_Final.csv")
#print(df)
df2 = pd.DataFrame(df,index = [3,4,5,], columns = ['type', 'price', ]) 
plt.xticks(rotation=45)
plt.title('TYPE vs PRICE bar graph')
plt.xlabel('TYPE')
print(df1)
x=df2.loc[:,'type']
y=df2.loc[:,'price']
df2['price'].plot(kind='bar', color='purple')


# In[46]:


df=pd.read_csv("Data_Vault_Final.csv")
df2 = pd.DataFrame(df,index = [9,10,11,], columns = ['type', 'price', ]) 
plt.xticks(rotation=45)
plt.title('TYPE vs PRICE bar graph')
plt.xlabel('TYPE')
plt.ylabel('PRICE')
print(df2)
x=df2.loc[:,'type']
y=df2.loc[:,'price']
plt.grid('.')
plt.scatter(x,y)


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Data_Vault_Final.csv")
df


# In[45]:


df3 = pd.DataFrame(df,index = [9,10,11,], columns = ['type','quantity' ])
plt.title('TYPE vs PRICE bar graph')
plt.xlabel('TYPE')
plt.ylabel('PRICE')
x=df3.loc[:,'type']
y=df3.loc[:,'quantity']
#z=df3.loc['quantity']
plt.plot(x,y)


# In[50]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
print('-'*10 + "Welcome to Data Vault" + '-'*10)
print("\nThis is the original data")
df=pd.read_csv("Data_Vault_Final.csv")
x=df['type']
plt.xticks(rotation=45)
plt.xlabel("TYPE")
plt.ylabel("PRICE")

y=df['price']
color = np.random.rand(15)

plt.scatter(x,y, c=color)


# In[48]:


import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("Data_Vault_Final.csv")
df3 = pd.DataFrame(df,index = [9,10,11,], columns = ['type','quantity' ])
plt.title('TYPE vs PRICE bar graph')
plt.xlabel('TYPE')
plt.ylabel('PRICE')
x=df3.loc[:,'type']
y=df3.loc[:,'quantity']
plt.plot(x,y)


# In[ ]:




