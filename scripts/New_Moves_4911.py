
# coding: utf-8

# In[14]:


import pandas as pd 
import matplotlib.pyplot as plt
import datetime 


# In[2]:


#Getting the Data 
Carbon_Disulfide = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Carbon_Disulfide/Carbon_Disulfide_4911.csv')
Hydrogen_Sulfide = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4911.csv')
Toluene = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4911.csv')
Xylene = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Xylene/Xylene_4911.csv')
Ozone = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Ozone/Ozone_4911.csv')


# In[3]:


#Concatinating All Polutant together 
#Merging the Data 
R4911_All_Pollutants = [Carbon_Disulfide, Hydrogen_Sulfide,Toluene, Xylene,Ozone]
R4911_Pollutant_Fusion = pd.concat(R4911_All_Pollutants,axis=1,join= "inner")
#Richmond_Total_Fusion.to_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/All_Richmond_fused.csv')


# In[4]:


#Test to see if Data nerged and for future tests as well 
R4911_Pollutant_Fusion.head(4)


# In[5]:


#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5']}
R4911_Pollutant_Fusion = R4911_Pollutant_Fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
R4911_Pollutant_Fusion = R4911_Pollutant_Fusion.drop(['EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5'], axis=1)


# In[6]:


#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.Toluene","3.feed_4911.Toluene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4911.Benzene","3.feed_4913.Toluene","3.feed_4911.Toluene","3.feed_4913.Hydrogen_Sulfide","3.feed_4911.Toluene","3.feed_4913.Hydrogen_Sulfide","3.feed_4911.Hydrogen_Sulfide
cols = list(R4911_Pollutant_Fusion.columns.values)
R4911_Pollutant_Fusion[cols] = R4911_Pollutant_Fusion[cols].replace('Offline','-1', regex = True)
R4911_Pollutant_Fusion[cols] = R4911_Pollutant_Fusion[cols].replace('Offline','-1', regex = True)
R4911_Pollutant_Fusion[cols] = R4911_Pollutant_Fusion[cols].replace('Low Signal','-2', regex = True)
R4911_Pollutant_Fusion[cols] = R4911_Pollutant_Fusion[cols].replace('In Calibration','-3', regex = True)


# In[7]:


for col in  R4911_Pollutant_Fusion.columns[0:]:
    R4911_Pollutant_Fusion[col] = R4911_Pollutant_Fusion[col].apply(pd.to_numeric, errors='coerce')


# In[8]:


R4911_Pollutant_Fusion.tail(5)


# In[9]:


R4911_Pollutant_Fusion.to_csv('/home/amos/Desktop/New_Moves_4911.csv')


# In[10]:


def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
R4911_Pollutant_Fusion['Pollutant Detects in 4911']  = R4911_Pollutant_Fusion.apply(cond2,axis = 1 );


# In[15]:


#Visual Tings 
dates = R4911_Pollutant_Fusion['EpochTime1']
dates = [pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10)) 
plt.scatter(dates,R4911_Pollutant_Fusion['Pollutant Detects in 4911'])
plt.title('Counts of Pollutant Detects in Location 4911 in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Location/R4911_Pollutant.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')

