#!/usr/bin/env python
# coding: utf-8

# In[1]:


#house price prediction multiple regression 
import pandas as pd 


# In[2]:


df=pd.read_csv("E:\\Django\\HousePricePrediction\\static\\csv\\Housingdata.csv")


# In[3]:


#df.head()


# In[4]:


import seaborn as sns 


# In[5]:


x=df.drop(["date","id","sqft_lot","sqft_basement","zipcode","sqft_living15","sqft_lot15"],axis=1)


# In[6]:


x.head()


# In[7]:


#split the data 
from sklearn.model_selection import train_test_split 


# In[8]:


X=x.drop("price",axis=1)


# In[9]:


y=x[["price"]]


# In[10]:


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.50)


# In[11]:


#Analyze the algorithm
from sklearn.linear_model import LinearRegression


# In[12]:


#Initialize the algorithm
reg=LinearRegression()


# In[14]:


reg.fit(X_train,y_train)


# In[15]:


pred=reg.predict(X_test)


# In[16]:


#pred


# In[17]:


from sklearn.metrics import r2_score


# In[18]:


r2_score(pred,y_test)


# In[19]:


sns.heatmap(y.isnull())


# In[20]:


#x.isnull().sum()


# In[22]:

def predict_price(bedroom,bathroom,sliving,sabove,ybuilt,yrenovated,view,floors,lat,long,waterfront,grade):
    array_val = [int(bedroom),int(bathroom),int(sliving),int(sabove),int(ybuilt),int(yrenovated),int(view),int(floors),int(lat),int(long),int(waterfront),int(grade)]    
    print(reg.predict([[3,2.25,2570,7242,2.0,0,0,3,7,2170,400,1951,1991,98125,47,-122,1690,3]]))
    #val = reg.predict([array_val])
    return 1

# In[ ]:




