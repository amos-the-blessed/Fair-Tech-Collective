
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import datetime 
import matplotlib.pyplot as plt


# In[2]:


Toluene_4909= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4909.csv',low_memory=False)
Toluene_4910= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4910.csv', low_memory=False)
Toluene_4911= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4911.csv',low_memory=False)
Toluene_4912= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4912.csv',low_memory=False)
Toluene_4913= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4913.csv', low_memory=False)
Toluene_4914= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4914.csv',low_memory=False)


# In[3]:


#Fusion for Toluene 
All_Toluene = [Toluene_4909, Toluene_4910, Toluene_4911,Toluene_4912,Toluene_4913, Toluene_4914 ];
Toluene_fusion = pd.concat(All_Toluene,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6']}
Toluene_fusion = Toluene_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
Toluene_fusion = Toluene_fusion.drop(['EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6'], axis=1)

#Cleaning the Data
cols = list(Toluene_fusion.columns.values)
Toluene_fusion[cols] = Toluene_fusion[cols].replace('Offline','-1', regex = True)
Toluene_fusion[cols] = Toluene_fusion[cols].replace('Offline','-1', regex = True)
Toluene_fusion[cols] = Toluene_fusion[cols].replace('Low Signal','-2', regex = True)
Toluene_fusion[cols] = Toluene_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  Toluene_fusion.columns[0:]:
    Toluene_fusion[col] = Toluene_fusion[col].apply(pd.to_numeric, errors='coerce')

#Toluene_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_Toluene.csv')


# In[4]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
Toluene_fusion['Total Toluene in Air(ppm)'] = Toluene_fusion.apply(cond,axis = 1 );
Toluene_fusion['Count of Toluene Detects']  = Toluene_fusion.apply(cond2,axis = 1 );


# In[5]:


#Visual Tings 
dates = Toluene_fusion['EpochTime1']
dates = [pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10)) 
plt.subplot(211)
plt.scatter(dates, Toluene_fusion['Total Toluene in Air(ppm)'])
plt.title('Total Toluene in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Toluene (ppm)')
plt.subplot(212)
plt.scatter(dates,Toluene_fusion['Count of Toluene Detects'])
plt.title('Toluene Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/Toluene.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[6]:


Benzene_4909= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4909.csv') 
Benzene_4910= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4910.csv') 
Benzene_4911= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4911.csv') 
Benzene_4912= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4912.csv') 
Benzene_4913= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4913.csv') 
Benzene_4914= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4914.csv') 


# In[7]:


#Fusion for Benzene 
All_Benzene = [Benzene_4909, Benzene_4910, Benzene_4911,Benzene_4912,Benzene_4913, Benzene_4914 ];
Benzene_fusion = pd.concat(All_Benzene,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6']}
Benzene_fusion = Benzene_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
Benzene_fusion = Benzene_fusion.drop(['EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.Benzene","3.feed_4912.Benzene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.Benzene","3.feed_4914.Benzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(Benzene_fusion.columns.values)
Benzene_fusion[cols] = Benzene_fusion[cols].replace('Offline','-1', regex = True)
Benzene_fusion[cols] = Benzene_fusion[cols].replace('Offline','-1', regex = True)
Benzene_fusion[cols] = Benzene_fusion[cols].replace('Low Signal','-2', regex = True)
Benzene_fusion[cols] = Benzene_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  Benzene_fusion.columns[0:]:
    Benzene_fusion[col] = Benzene_fusion[col].apply(pd.to_numeric, errors='coerce')

Benzene_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_Benzene.csv')


# In[8]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
Benzene_fusion['Total Benzene in Air(ppm)'] = Benzene_fusion.apply(cond,axis = 1 );
Benzene_fusion['Count of Benzene Detects']  = Benzene_fusion.apply(cond2,axis = 1 );


# In[9]:


#Visual Tings 
dates = Benzene_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10)) 
plt.subplot(211)
plt.scatter(dates, Benzene_fusion['Total Benzene in Air(ppm)'])
plt.title('Total Benzene in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Benzene (ppm)')
plt.subplot(212)
plt.scatter(dates, Benzene_fusion['Count of Benzene Detects'])
plt.title('Benzene Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/Benzene.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[10]:


H_Sulfide_4909 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4909.csv')
H_Sulfide_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4910.csv')
H_Sulfide_4911 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4911.csv')
H_Sulfide_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4912.csv')
H_Sulfide_4913 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4913.csv')
H_Sulfide_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4914.csv')


# In[11]:


#Fusion for H_Sulfide 
All_H_Sulfide = [H_Sulfide_4909, H_Sulfide_4910, H_Sulfide_4911,H_Sulfide_4912,H_Sulfide_4913, H_Sulfide_4914 ];
H_Sulfide_fusion = pd.concat(All_H_Sulfide,axis=1,join= "inner");
fv
#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6']}
H_Sulfide_fusion = H_Sulfide_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
H_Sulfide_fusion = H_Sulfide_fusion.drop(['EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.H_Sulfide","3.feed_4912.H_Sulfide","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.H_Sulfide","3.feed_4914.H_Sulfide","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.H_Sulfide","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(H_Sulfide_fusion.columns.values)
H_Sulfide_fusion[cols] = H_Sulfide_fusion[cols].replace('Offline','-1', regex = True)
H_Sulfide_fusion[cols] = H_Sulfide_fusion[cols].replace('Offline','-1', regex = True)
H_Sulfide_fusion[cols] = H_Sulfide_fusion[cols].replace('Low Signal','-2', regex = True)
H_Sulfide_fusion[cols] = H_Sulfide_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  H_Sulfide_fusion.columns[0:]:
    H_Sulfide_fusion[col] = H_Sulfide_fusion[col].apply(pd.to_numeric, errors='coerce')

H_Sulfide_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_H_Sulfide.csv')


# In[12]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
H_Sulfide_fusion['Total H_Sulfide in Air(ppm)'] = H_Sulfide_fusion.apply(cond,axis = 1 );
H_Sulfide_fusion['Count of H_Sulfide Detects']  = H_Sulfide_fusion.apply(cond2,axis = 1 );


# In[13]:


#Visual Tings 
dates = H_Sulfide_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, H_Sulfide_fusion['Total H_Sulfide in Air(ppm)'], s =30)
plt.title('Total H_Sulfide in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('H_Sulfide (ppm)')
plt.subplot(212)
plt.scatter(dates, H_Sulfide_fusion['Count of H_Sulfide Detects'], s=30)
plt.title('H_Sulfide Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/H_Sulfide.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[14]:


Xylene_4909 =  pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Xylene/Xylene_4909.csv')
Xylene_4911 =  pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Xylene/Xylene_4911.csv')
Xylene_4913 =  pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Xylene/Xylene_4913.csv')


# In[15]:


#Fusion for Xylene 
All_Xylene = [Xylene_4909, Xylene_4911,Xylene_4913 ];
Xylene_fusion = pd.concat(All_Xylene,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
Xylene_fusion = Xylene_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
Xylene_fusion = Xylene_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.Xylene","3.feed_4912.Xylene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.Xylene","3.feed_4914.Xylene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Xylene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(Xylene_fusion.columns.values)
Xylene_fusion[cols] = Xylene_fusion[cols].replace('Offline','-1', regex = True)
Xylene_fusion[cols] = Xylene_fusion[cols].replace('Offline','-1', regex = True)
Xylene_fusion[cols] = Xylene_fusion[cols].replace('Low Signal','-2', regex = True)
Xylene_fusion[cols] = Xylene_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  Xylene_fusion.columns[0:]:
    Xylene_fusion[col] = Xylene_fusion[col].apply(pd.to_numeric, errors='coerce')

Xylene_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_Xylene.csv')


# In[16]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
Xylene_fusion['Total Xylene in Air(ppm)'] = Xylene_fusion.apply(cond,axis = 1 );
Xylene_fusion['Count of Xylene Detects']  = Xylene_fusion.apply(cond2,axis = 1 );


# In[17]:


#Visual Tings 
dates = Toluene_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, Toluene_fusion['Total Toluene in Air(ppm)'], s =30)
plt.title('Total Toluene in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Toluene (ppm)')
plt.subplot(212)
plt.scatter(dates, Toluene_fusion['Count of Toluene Detects'], s=30)
plt.title('Toluene Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/Toluene.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[18]:


Ammonia_4910= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Ammonia/Ammonia_4910.csv')
Ammonia_4912= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Ammonia/Ammonia_4912.csv')
Ammonia_4914= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Ammonia/Ammonia_4914.csv')


# In[19]:


#Fusion for Ammonia 
All_Ammonia = [Ammonia_4910, Ammonia_4912,Ammonia_4914 ];
Ammonia_fusion = pd.concat(All_Ammonia,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
Ammonia_fusion = Ammonia_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
Ammonia_fusion = Ammonia_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.Ammonia","3.feed_4912.Ammonia","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.Ammonia","3.feed_4914.Ammonia","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Ammonia","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(Ammonia_fusion.columns.values)
Ammonia_fusion[cols] = Ammonia_fusion[cols].replace('Offline','-1', regex = True)
Ammonia_fusion[cols] = Ammonia_fusion[cols].replace('Offline','-1', regex = True)
Ammonia_fusion[cols] = Ammonia_fusion[cols].replace('Low Signal','-2', regex = True)
Ammonia_fusion[cols] = Ammonia_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  Ammonia_fusion.columns[0:]:
    Ammonia_fusion[col] = Ammonia_fusion[col].apply(pd.to_numeric, errors='coerce')

Ammonia_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_Ammonia.csv')


# In[20]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
Ammonia_fusion['Total Ammonia in Air(ppm)'] = Ammonia_fusion.apply(cond,axis = 1 );
Ammonia_fusion['Count of Ammonia Detects']  = Ammonia_fusion.apply(cond2,axis = 1 );


# In[21]:


#Visual Tings 
dates = Ammonia_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, Ammonia_fusion['Total Ammonia in Air(ppm)'], s =30)
plt.title('Total Ammonia in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Ammonia (ppm)')
plt.subplot(212)
plt.scatter(dates, Ammonia_fusion['Count of Ammonia Detects'], s=30)
plt.title('Ammonia Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/Ammonia.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[22]:


Black_Carbon_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Black_Carbon/Black_Carbon_4910.csv')
Black_Carbon_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Black_Carbon/Black_Carbon_4912.csv')
Black_Carbon_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Black_Carbon/Black_Carbon_4914.csv')


# In[23]:


#Fusion for Black_Carbon 
All_Black_Carbon = [Black_Carbon_4910, Black_Carbon_4912,Black_Carbon_4914 ];
Black_Carbon_fusion = pd.concat(All_Black_Carbon,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
Black_Carbon_fusion = Black_Carbon_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
Black_Carbon_fusion = Black_Carbon_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.Black_Carbon","3.feed_4912.Black_Carbon","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.Black_Carbon","3.feed_4914.Black_Carbon","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Black_Carbon","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(Black_Carbon_fusion.columns.values)
Black_Carbon_fusion[cols] = Black_Carbon_fusion[cols].replace('Offline','-1', regex = True)
Black_Carbon_fusion[cols] = Black_Carbon_fusion[cols].replace('Offline','-1', regex = True)
Black_Carbon_fusion[cols] = Black_Carbon_fusion[cols].replace('Low Signal','-2', regex = True)
Black_Carbon_fusion[cols] = Black_Carbon_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  Black_Carbon_fusion.columns[0:]:
    Black_Carbon_fusion[col] = Black_Carbon_fusion[col].apply(pd.to_numeric, errors='coerce')

Black_Carbon_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_Black_Carbon.csv')


# In[24]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
Black_Carbon_fusion['Total Black_Carbon in Air(ppm)'] = Black_Carbon_fusion.apply(cond,axis = 1 );
Black_Carbon_fusion['Count of Black_Carbon Detects']  = Black_Carbon_fusion.apply(cond2,axis = 1 );


# In[25]:


#Visual Tings 
dates = Black_Carbon_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, Black_Carbon_fusion['Total Black_Carbon in Air(ppm)'], s =30)
plt.title('Total Black_Carbon in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Black_Carbon (ppm)')
plt.subplot(212)
plt.scatter(dates, Black_Carbon_fusion['Count of Black_Carbon Detects'], s=30)
plt.title('Black_Carbon Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/Black_Carbon.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[26]:


Ethylbenzene_4910= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Ethylbenzene/Ethylbenzene_4910.csv')
Ethylbenzene_4912= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Ethylbenzene/Ethylbenzene_4912.csv')
Ethylbenzene_4914= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Ethylbenzene/Ethylbenzene_4914.csv')


# In[27]:


#Fusion for Ethylbenzene 
All_Ethylbenzene = [Ethylbenzene_4910, Ethylbenzene_4912,Ethylbenzene_4914 ];
Ethylbenzene_fusion = pd.concat(All_Ethylbenzene,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
Ethylbenzene_fusion = Ethylbenzene_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
Ethylbenzene_fusion = Ethylbenzene_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.Ethylbenzene","3.feed_4912.Ethylbenzene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.Ethylbenzene","3.feed_4914.Ethylbenzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Ethylbenzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(Ethylbenzene_fusion.columns.values)
Ethylbenzene_fusion[cols] = Ethylbenzene_fusion[cols].replace('Offline','-1', regex = True)
Ethylbenzene_fusion[cols] = Ethylbenzene_fusion[cols].replace('Offline','-1', regex = True)
Ethylbenzene_fusion[cols] = Ethylbenzene_fusion[cols].replace('Low Signal','-2', regex = True)
Ethylbenzene_fusion[cols] = Ethylbenzene_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  Ethylbenzene_fusion.columns[0:]:
    Ethylbenzene_fusion[col] = Ethylbenzene_fusion[col].apply(pd.to_numeric, errors='coerce')

Ethylbenzene_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_Ethylbenzene.csv')


# In[28]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
Ethylbenzene_fusion['Total Ethylbenzene in Air(ppm)'] = Ethylbenzene_fusion.apply(cond,axis = 1 );
Ethylbenzene_fusion['Count of Ethylbenzene Detects']  = Ethylbenzene_fusion.apply(cond2,axis = 1 );


# In[29]:


#Visual Tings 
dates = Ethylbenzene_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, Ethylbenzene_fusion['Total Ethylbenzene in Air(ppm)'], s =30)
plt.title('Total Ethylbenzene in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Ethylbenzene (ppm)')
plt.subplot(212)
plt.scatter(dates, Ethylbenzene_fusion['Count of Ethylbenzene Detects'], s=30)
plt.title('Ethylbenzene Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/Ethylbenzene.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[30]:


r3_Methylpentane_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/3_Methylpentane/3_Methylpentane_4910.csv')
r3_Methylpentane_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/3_Methylpentane/3_Methylpentane_4912.csv')
r3_Methylpentane_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/3_Methylpentane/3_Methylpentane_4914.csv')


# In[31]:


#Fusion for r3_Methylpentane 
All_r3_Methylpentane = [r3_Methylpentane_4910, r3_Methylpentane_4912,r3_Methylpentane_4914 ];
r3_Methylpentane_fusion = pd.concat(All_r3_Methylpentane,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
r3_Methylpentane_fusion = r3_Methylpentane_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
r3_Methylpentane_fusion = r3_Methylpentane_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.r3_Methylpentane","3.feed_4912.r3_Methylpentane","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.r3_Methylpentane","3.feed_4914.r3_Methylpentane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.r3_Methylpentane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(r3_Methylpentane_fusion.columns.values)
r3_Methylpentane_fusion[cols] = r3_Methylpentane_fusion[cols].replace('Offline','-1', regex = True)
r3_Methylpentane_fusion[cols] = r3_Methylpentane_fusion[cols].replace('Offline','-1', regex = True)
r3_Methylpentane_fusion[cols] = r3_Methylpentane_fusion[cols].replace('Low Signal','-2', regex = True)
r3_Methylpentane_fusion[cols] = r3_Methylpentane_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  r3_Methylpentane_fusion.columns[0:]:
    r3_Methylpentane_fusion[col] = r3_Methylpentane_fusion[col].apply(pd.to_numeric, errors='coerce')

r3_Methylpentane_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_r3_Methylpentane.csv')


# In[32]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
r3_Methylpentane_fusion['Total r3_Methylpentane in Air(ppm)'] = r3_Methylpentane_fusion.apply(cond,axis = 1 );
r3_Methylpentane_fusion['Count of r3_Methylpentane Detects']  = r3_Methylpentane_fusion.apply(cond2,axis = 1 );


# In[33]:


#Visual Tings 
dates = r3_Methylpentane_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, r3_Methylpentane_fusion['Total r3_Methylpentane in Air(ppm)'], s =30)
plt.title('Total r3_Methylpentane in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('r3_Methylpentane (ppm)')
plt.subplot(212)
plt.scatter(dates, r3_Methylpentane_fusion['Count of r3_Methylpentane Detects'], s=30)
plt.title('r3_Methylpentane Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/r3_Methylpentane.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[34]:


N_Heptane_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Heptane/N_Heptane_4910.csv')
N_Heptane_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Heptane/N_Heptane_4912.csv')
N_Heptane_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Heptane/N_Heptane_4914.csv')


# In[35]:


#Fusion for N_Heptane 
All_N_Heptane = [N_Heptane_4910, N_Heptane_4912,N_Heptane_4914 ];
N_Heptane_fusion = pd.concat(All_N_Heptane,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
N_Heptane_fusion = N_Heptane_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
N_Heptane_fusion = N_Heptane_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.N_Heptane","3.feed_4912.N_Heptane","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.N_Heptane","3.feed_4914.N_Heptane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.N_Heptane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(N_Heptane_fusion.columns.values)
N_Heptane_fusion[cols] = N_Heptane_fusion[cols].replace('Offline','-1', regex = True)
N_Heptane_fusion[cols] = N_Heptane_fusion[cols].replace('Offline','-1', regex = True)
N_Heptane_fusion[cols] = N_Heptane_fusion[cols].replace('Low Signal','-2', regex = True)
N_Heptane_fusion[cols] = N_Heptane_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  N_Heptane_fusion.columns[0:]:
    N_Heptane_fusion[col] = N_Heptane_fusion[col].apply(pd.to_numeric, errors='coerce')

N_Heptane_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_N_Heptane.csv')


# In[36]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
N_Heptane_fusion['Total N_Heptane in Air(ppm)'] = N_Heptane_fusion.apply(cond,axis = 1 );
N_Heptane_fusion['Count of N_Heptane Detects']  = N_Heptane_fusion.apply(cond2,axis = 1 );


# In[37]:


#Visual Tings 
dates = N_Heptane_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, N_Heptane_fusion['Total N_Heptane in Air(ppm)'], s =30)
plt.title('Total N_Heptane in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('N_Heptane (ppm)')
plt.subplot(212)
plt.scatter(dates, N_Heptane_fusion['Count of N_Heptane Detects'], s=30)
plt.title('N_Heptane Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/N_Heptane.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[38]:


N_Hexane_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Hexane/N_Hexane_4910.csv')
N_Hexane_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Hexane/N_Hexane_4912.csv')
N_Hexane_4914= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Hexane/N_Hexane_4914.csv')


# In[39]:


#Fusion for N_Hexane 
All_N_Hexane = [N_Hexane_4910, N_Hexane_4912,N_Hexane_4914 ];
N_Hexane_fusion = pd.concat(All_N_Hexane,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
N_Hexane_fusion = N_Hexane_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
N_Hexane_fusion = N_Hexane_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.N_Hexane","3.feed_4912.N_Hexane","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.N_Hexane","3.feed_4914.N_Hexane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.N_Hexane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(N_Hexane_fusion.columns.values)
N_Hexane_fusion[cols] = N_Hexane_fusion[cols].replace('Offline','-1', regex = True)
N_Hexane_fusion[cols] = N_Hexane_fusion[cols].replace('Offline','-1', regex = True)
N_Hexane_fusion[cols] = N_Hexane_fusion[cols].replace('Low Signal','-2', regex = True)
N_Hexane_fusion[cols] = N_Hexane_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  N_Hexane_fusion.columns[0:]:
    N_Hexane_fusion[col] = N_Hexane_fusion[col].apply(pd.to_numeric, errors='coerce')

N_Hexane_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_N_Hexane.csv')


# In[40]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
N_Hexane_fusion['Total N_Hexane in Air(ppm)'] = N_Hexane_fusion.apply(cond,axis = 1 );
N_Hexane_fusion['Count of N_Hexane Detects']  = N_Hexane_fusion.apply(cond2,axis = 1 );


# In[41]:


#Visual Tings 
dates = N_Hexane_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, N_Hexane_fusion['Total N_Hexane in Air(ppm)'], s =30)
plt.title('Total N_Hexane in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('N_Hexane (ppm)')
plt.subplot(212)
plt.scatter(dates, N_Hexane_fusion['Count of N_Hexane Detects'], s=30)
plt.title('N_Hexane Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/N_Hexane.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[42]:


N_Octane_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Octane/N_Octane_4910.csv')
N_Octane_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Octane/N_Octane_4912.csv')
N_Octane_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Octane/N_Octane_4914.csv')


# In[43]:


#Fusion for N_Octane 
All_N_Octane = [N_Octane_4910, N_Octane_4912,N_Octane_4914 ];
N_Octane_fusion = pd.concat(All_N_Octane,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
N_Octane_fusion = N_Octane_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
N_Octane_fusion = N_Octane_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.N_Octane","3.feed_4912.N_Octane","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.N_Octane","3.feed_4914.N_Octane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.N_Octane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(N_Octane_fusion.columns.values)
N_Octane_fusion[cols] = N_Octane_fusion[cols].replace('Offline','-1', regex = True)
N_Octane_fusion[cols] = N_Octane_fusion[cols].replace('Offline','-1', regex = True)
N_Octane_fusion[cols] = N_Octane_fusion[cols].replace('Low Signal','-2', regex = True)
N_Octane_fusion[cols] = N_Octane_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  N_Octane_fusion.columns[0:]:
    N_Octane_fusion[col] = N_Octane_fusion[col].apply(pd.to_numeric, errors='coerce')

N_Octane_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_N_Octane.csv')


# In[44]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
N_Octane_fusion['Total N_Octane in Air(ppm)'] = N_Octane_fusion.apply(cond,axis = 1 );
N_Octane_fusion['Count of N_Octane Detects']  = N_Octane_fusion.apply(cond2,axis = 1 );


# In[45]:


#Visual Tings 
dates = N_Octane_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, N_Octane_fusion['Total N_Octane in Air(ppm)'], s =30)
plt.title('Total N_Octane in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('N_Octane (ppm)')
plt.subplot(212)
plt.scatter(dates, N_Octane_fusion['Count of N_Octane Detects'], s=30)
plt.title('N_Octane Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/N_Octane.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[46]:


PM_2_5_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/PM_2_5/PM_2_5_4910.csv')
PM_2_5_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/PM_2_5/PM_2_5_4912.csv')
PM_2_5_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/PM_2_5/PM_2_5_4914.csv')


# In[47]:


#Fusion for PM_2_5 
All_PM_2_5 = [PM_2_5_4910, PM_2_5_4912,PM_2_5_4914 ];
PM_2_5_fusion = pd.concat(All_PM_2_5,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
PM_2_5_fusion = PM_2_5_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
PM_2_5_fusion = PM_2_5_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.PM_2_5","3.feed_4912.PM_2_5","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.PM_2_5","3.feed_4914.PM_2_5","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.PM_2_5","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(PM_2_5_fusion.columns.values)
PM_2_5_fusion[cols] = PM_2_5_fusion[cols].replace('Offline','-1', regex = True)
PM_2_5_fusion[cols] = PM_2_5_fusion[cols].replace('Offline','-1', regex = True)
PM_2_5_fusion[cols] = PM_2_5_fusion[cols].replace('Low Signal','-2', regex = True)
PM_2_5_fusion[cols] = PM_2_5_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  PM_2_5_fusion.columns[0:]:
    PM_2_5_fusion[col] = PM_2_5_fusion[col].apply(pd.to_numeric, errors='coerce')

PM_2_5_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_PM_2_5.csv')


# In[48]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
PM_2_5_fusion['Total PM_2_5 in Air(ppm)'] = PM_2_5_fusion.apply(cond,axis = 1 );
PM_2_5_fusion['Count of PM_2_5 Detects']  = PM_2_5_fusion.apply(cond2,axis = 1 );


# In[49]:


#Visual Tings 
dates = PM_2_5_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, PM_2_5_fusion['Total PM_2_5 in Air(ppm)'], s =30)
plt.title('Total PM_2_5 in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('PM_2_5 (ppm)')
plt.subplot(212)
plt.scatter(dates, PM_2_5_fusion['Count of PM_2_5 Detects'], s=30)
plt.title('PM_2_5 Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/PM_2_5.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[50]:


r1_2_3_Trimethylbenzene_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_2_3_Trimethylbenzene/1_2_3_Trimethylbenzene_4910.csv')
r1_2_3_Trimethylbenzene_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_2_3_Trimethylbenzene/1_2_3_Trimethylbenzene_4912.csv')
r1_2_3_Trimethylbenzene_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_2_3_Trimethylbenzene/1_2_3_Trimethylbenzene_4914.csv')


# In[51]:


#Fusion for r1_2_3_Trimethylbenzene 
All_r1_2_3_Trimethylbenzene = [r1_2_3_Trimethylbenzene_4910, r1_2_3_Trimethylbenzene_4912,r1_2_3_Trimethylbenzene_4914 ];
r1_2_3_Trimethylbenzene_fusion = pd.concat(All_r1_2_3_Trimethylbenzene,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
r1_2_3_Trimethylbenzene_fusion = r1_2_3_Trimethylbenzene_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
r1_2_3_Trimethylbenzene_fusion = r1_2_3_Trimethylbenzene_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.r1_2_3_Trimethylbenzene","3.feed_4912.r1_2_3_Trimethylbenzene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.r1_2_3_Trimethylbenzene","3.feed_4914.r1_2_3_Trimethylbenzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.r1_2_3_Trimethylbenzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(r1_2_3_Trimethylbenzene_fusion.columns.values)
r1_2_3_Trimethylbenzene_fusion[cols] = r1_2_3_Trimethylbenzene_fusion[cols].replace('Offline','-1', regex = True)
r1_2_3_Trimethylbenzene_fusion[cols] = r1_2_3_Trimethylbenzene_fusion[cols].replace('Offline','-1', regex = True)
r1_2_3_Trimethylbenzene_fusion[cols] = r1_2_3_Trimethylbenzene_fusion[cols].replace('Low Signal','-2', regex = True)
r1_2_3_Trimethylbenzene_fusion[cols] = r1_2_3_Trimethylbenzene_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  r1_2_3_Trimethylbenzene_fusion.columns[0:]:
    r1_2_3_Trimethylbenzene_fusion[col] = r1_2_3_Trimethylbenzene_fusion[col].apply(pd.to_numeric, errors='coerce')

r1_2_3_Trimethylbenzene_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_r1_2_3_Trimethylbenzene.csv')


# In[52]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
r1_2_3_Trimethylbenzene_fusion['Total r1_2_3_Trimethylbenzene in Air(ppm)'] = r1_2_3_Trimethylbenzene_fusion.apply(cond,axis = 1 );
r1_2_3_Trimethylbenzene_fusion['Count of r1_2_3_Trimethylbenzene Detects']  = r1_2_3_Trimethylbenzene_fusion.apply(cond2,axis = 1 );


# In[53]:


#Visual Tings 
dates = r1_2_3_Trimethylbenzene_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, r1_2_3_Trimethylbenzene_fusion['Total r1_2_3_Trimethylbenzene in Air(ppm)'], s =30)
plt.title('Total r1_2_3_Trimethylbenzene in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('r1_2_3_Trimethylbenzene (ppm)')
plt.subplot(212)
plt.scatter(dates, r1_2_3_Trimethylbenzene_fusion['Count of r1_2_3_Trimethylbenzene Detects'], s=30)
plt.title('r1_2_3_Trimethylbenzene Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/r1_2_3_Trimethylbenzene.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[54]:


r1_2_4_Trimethylbenzene_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_2_4_Trimethylbenzene/1_2_4_Trimethylbenzene_4910.csv')
r1_2_4_Trimethylbenzene_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_2_4_Trimethylbenzene/1_2_4_Trimethylbenzene_4912.csv')
r1_2_4_Trimethylbenzene_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_2_4_Trimethylbenzene/1_2_4_Trimethylbenzene_4914.csv')


# In[55]:


#Fusion for r1_2_4_Trimethylbenzene 
All_r1_2_4_Trimethylbenzene = [r1_2_4_Trimethylbenzene_4910, r1_2_4_Trimethylbenzene_4912,r1_2_4_Trimethylbenzene_4914 ];
r1_2_4_Trimethylbenzene_fusion = pd.concat(All_r1_2_4_Trimethylbenzene,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
r1_2_4_Trimethylbenzene_fusion = r1_2_4_Trimethylbenzene_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
r1_2_4_Trimethylbenzene_fusion = r1_2_4_Trimethylbenzene_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.r1_2_4_Trimethylbenzene","3.feed_4912.r1_2_4_Trimethylbenzene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.r1_2_4_Trimethylbenzene","3.feed_4914.r1_2_4_Trimethylbenzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.r1_2_4_Trimethylbenzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(r1_2_4_Trimethylbenzene_fusion.columns.values)
r1_2_4_Trimethylbenzene_fusion[cols] = r1_2_4_Trimethylbenzene_fusion[cols].replace('Offline','-1', regex = True)
r1_2_4_Trimethylbenzene_fusion[cols] = r1_2_4_Trimethylbenzene_fusion[cols].replace('Offline','-1', regex = True)
r1_2_4_Trimethylbenzene_fusion[cols] = r1_2_4_Trimethylbenzene_fusion[cols].replace('Low Signal','-2', regex = True)
r1_2_4_Trimethylbenzene_fusion[cols] = r1_2_4_Trimethylbenzene_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  r1_2_4_Trimethylbenzene_fusion.columns[0:]:
    r1_2_4_Trimethylbenzene_fusion[col] = r1_2_4_Trimethylbenzene_fusion[col].apply(pd.to_numeric, errors='coerce')

r1_2_4_Trimethylbenzene_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_r1_2_4_Trimethylbenzene.csv')


# In[56]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
r1_2_4_Trimethylbenzene_fusion['Total r1_2_4_Trimethylbenzene in Air(ppm)'] = r1_2_4_Trimethylbenzene_fusion.apply(cond,axis = 1 );
r1_2_4_Trimethylbenzene_fusion['Count of r1_2_4_Trimethylbenzene Detects']  = r1_2_4_Trimethylbenzene_fusion.apply(cond2,axis = 1 );


# In[57]:


#Visual Tings 
dates = r1_2_4_Trimethylbenzene_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, r1_2_4_Trimethylbenzene_fusion['Total r1_2_4_Trimethylbenzene in Air(ppm)'], s =30)
plt.title('Total r1_2_4_Trimethylbenzene in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('r1_2_4_Trimethylbenzene (ppm)')
plt.subplot(212)
plt.scatter(dates, r1_2_4_Trimethylbenzene_fusion['Count of r1_2_4_Trimethylbenzene Detects'], s=30)
plt.title('r1_2_4_Trimethylbenzene Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/r1_2_4_Trimethylbenzene.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[58]:


r1_3_5_Trimethylbenzene_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_3_5_Trimethylbenzene/1_3_5_Trimethylbenzene_4910.csv')
r1_3_5_Trimethylbenzene_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_3_5_Trimethylbenzene/1_3_5_Trimethylbenzene_4912.csv')
r1_3_5_Trimethylbenzene_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_3_5_Trimethylbenzene/1_3_5_Trimethylbenzene_4914.csv')


# In[59]:


#Fusion for r1_3_5_Trimethylbenzene 
All_r1_3_5_Trimethylbenzene = [r1_3_5_Trimethylbenzene_4910, r1_3_5_Trimethylbenzene_4912,r1_3_5_Trimethylbenzene_4914 ];
r1_3_5_Trimethylbenzene_fusion = pd.concat(All_r1_3_5_Trimethylbenzene,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
r1_3_5_Trimethylbenzene_fusion = r1_3_5_Trimethylbenzene_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
r1_3_5_Trimethylbenzene_fusion = r1_3_5_Trimethylbenzene_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.r1_3_5_Trimethylbenzene","3.feed_4912.r1_3_5_Trimethylbenzene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.r1_3_5_Trimethylbenzene","3.feed_4914.r1_3_5_Trimethylbenzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.r1_3_5_Trimethylbenzene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(r1_3_5_Trimethylbenzene_fusion.columns.values)
r1_3_5_Trimethylbenzene_fusion[cols] = r1_3_5_Trimethylbenzene_fusion[cols].replace('Offline','-1', regex = True)
r1_3_5_Trimethylbenzene_fusion[cols] = r1_3_5_Trimethylbenzene_fusion[cols].replace('Offline','-1', regex = True)
r1_3_5_Trimethylbenzene_fusion[cols] = r1_3_5_Trimethylbenzene_fusion[cols].replace('Low Signal','-2', regex = True)
r1_3_5_Trimethylbenzene_fusion[cols] = r1_3_5_Trimethylbenzene_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  r1_3_5_Trimethylbenzene_fusion.columns[0:]:
    r1_3_5_Trimethylbenzene_fusion[col] = r1_3_5_Trimethylbenzene_fusion[col].apply(pd.to_numeric, errors='coerce')

r1_3_5_Trimethylbenzene_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_r1_3_5_Trimethylbenzene.csv')


# In[60]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
r1_3_5_Trimethylbenzene_fusion['Total r1_3_5_Trimethylbenzene in Air(ppm)'] = r1_3_5_Trimethylbenzene_fusion.apply(cond,axis = 1 );
r1_3_5_Trimethylbenzene_fusion['Count of r1_3_5_Trimethylbenzene Detects']  = r1_3_5_Trimethylbenzene_fusion.apply(cond2,axis = 1 );


# In[61]:


#Visual Tings 
dates = r1_3_5_Trimethylbenzene_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, r1_3_5_Trimethylbenzene_fusion['Total r1_3_5_Trimethylbenzene in Air(ppm)'], s =30)
plt.title('Total r1_3_5_Trimethylbenzene in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('r1_3_5_Trimethylbenzene (ppm)')
plt.subplot(212)
plt.scatter(dates, r1_3_5_Trimethylbenzene_fusion['Count of r1_3_5_Trimethylbenzene Detects'], s=30)
plt.title('r1_3_5_Trimethylbenzene Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/r1_3_5_Trimethylbenzene.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[62]:


r2_2_4_Trimethylpentane_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/2_2_4_Trimethylpentane/2_2_4_Trimethylpentane_4910.csv')
r2_2_4_Trimethylpentane_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/2_2_4_Trimethylpentane/2_2_4_Trimethylpentane_4912.csv')
r2_2_4_Trimethylpentane_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/2_2_4_Trimethylpentane/2_2_4_Trimethylpentane_4914.csv')


# In[63]:


#Fusion for r2_2_4_Trimethylpentane 
All_r2_2_4_Trimethylpentane = [r2_2_4_Trimethylpentane_4910, r2_2_4_Trimethylpentane_4912,r2_2_4_Trimethylpentane_4914 ];
r2_2_4_Trimethylpentane_fusion = pd.concat(All_r2_2_4_Trimethylpentane,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
r2_2_4_Trimethylpentane_fusion = r2_2_4_Trimethylpentane_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
r2_2_4_Trimethylpentane_fusion = r2_2_4_Trimethylpentane_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.r2_2_4_Trimethylpentane","3.feed_4912.r2_2_4_Trimethylpentane","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.pentane","3.feed_4913.r2_2_4_Trimethylpentane","3.feed_4914.r2_2_4_Trimethylpentane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.r2_2_4_Trimethylpentane","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(r2_2_4_Trimethylpentane_fusion.columns.values)
r2_2_4_Trimethylpentane_fusion[cols] = r2_2_4_Trimethylpentane_fusion[cols].replace('Offline','-1', regex = True)
r2_2_4_Trimethylpentane_fusion[cols] = r2_2_4_Trimethylpentane_fusion[cols].replace('Offline','-1', regex = True)
r2_2_4_Trimethylpentane_fusion[cols] = r2_2_4_Trimethylpentane_fusion[cols].replace('Low Signal','-2', regex = True)
r2_2_4_Trimethylpentane_fusion[cols] = r2_2_4_Trimethylpentane_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  r2_2_4_Trimethylpentane_fusion.columns[0:]:
    r2_2_4_Trimethylpentane_fusion[col] = r2_2_4_Trimethylpentane_fusion[col].apply(pd.to_numeric, errors='coerce')

r2_2_4_Trimethylpentane_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_r2_2_4_Trimethylpentane.csv')


# In[64]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
r2_2_4_Trimethylpentane_fusion['Total r2_2_4_Trimethylpentane in Air(ppm)'] = r2_2_4_Trimethylpentane_fusion.apply(cond,axis = 1 );
r2_2_4_Trimethylpentane_fusion['Count of r2_2_4_Trimethylpentane Detects']  = r2_2_4_Trimethylpentane_fusion.apply(cond2,axis = 1 );


# In[66]:


#Visual Tings 
dates = r2_2_4_Trimethylpentane_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, r2_2_4_Trimethylpentane_fusion['Total r2_2_4_Trimethylpentane in Air(ppm)'], s =30)
plt.title('Total r2_2_4_Trimethylpentane in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('r2_2_4_Trimethylpentane (ppm)')
plt.subplot(212)
plt.scatter(dates, r2_2_4_Trimethylpentane_fusion['Count of r2_2_4_Trimethylpentane Detects'], s=30)
plt.title('r2_2_4_Trimethylpentane Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/r2_2_4_Trimethylpentane.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[67]:


m_p_Xylene_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/m_p_Xylene/m_p_Xylene_4910.csv')
m_p_Xylene_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/m_p_Xylene/m_p_Xylene_4912.csv')
m_p_Xylene_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/m_p_Xylene/m_p_Xylene_4914.csv')


# In[68]:


#Fusion for m_p_Xylene 
All_m_p_Xylene = [m_p_Xylene_4910, m_p_Xylene_4912,m_p_Xylene_4914 ];
m_p_Xylene_fusion = pd.concat(All_m_p_Xylene,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
m_p_Xylene_fusion = m_p_Xylene_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
m_p_Xylene_fusion = m_p_Xylene_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.m_p_Xylene","3.feed_4912.m_p_Xylene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.m_p_Xylene","3.feed_4914.m_p_Xylene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.m_p_Xylene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(m_p_Xylene_fusion.columns.values)
m_p_Xylene_fusion[cols] = m_p_Xylene_fusion[cols].replace('Offline','-1', regex = True)
m_p_Xylene_fusion[cols] = m_p_Xylene_fusion[cols].replace('Offline','-1', regex = True)
m_p_Xylene_fusion[cols] = m_p_Xylene_fusion[cols].replace('Low Signal','-2', regex = True)
m_p_Xylene_fusion[cols] = m_p_Xylene_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  m_p_Xylene_fusion.columns[0:]:
    m_p_Xylene_fusion[col] = m_p_Xylene_fusion[col].apply(pd.to_numeric, errors='coerce')

m_p_Xylene_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_m_p_Xylene.csv')


# In[69]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
m_p_Xylene_fusion['Total m_p_Xylene in Air(ppm)'] = m_p_Xylene_fusion.apply(cond,axis = 1 );
m_p_Xylene_fusion['Count of m_p_Xylene Detects']  = m_p_Xylene_fusion.apply(cond2,axis = 1 );


# In[70]:


#Visual Tings 
dates = m_p_Xylene_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, m_p_Xylene_fusion['Total m_p_Xylene in Air(ppm)'], s =30)
plt.title('Total m_p_Xylene in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('m_p_Xylene (ppm)')
plt.subplot(212)
plt.scatter(dates, m_p_Xylene_fusion['Count of m_p_Xylene Detects'], s=30)
plt.title('m_p_Xylene Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/m_p_Xylene.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')


# In[71]:


o_Xylene_4910 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/o_Xylene/o_Xylene_4910.csv')
o_Xylene_4912 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/o_Xylene/o_Xylene_4912.csv')
o_Xylene_4914 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/o_Xylene/o_Xylene_4914.csv')


# In[72]:


#Fusion for o_Xylene 
All_o_Xylene = [o_Xylene_4910, o_Xylene_4912,o_Xylene_4914 ];
o_Xylene_fusion = pd.concat(All_o_Xylene,axis=1,join= "inner");

#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3']}
o_Xylene_fusion = o_Xylene_fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
o_Xylene_fusion = o_Xylene_fusion.drop(['EpochTime2', 'EpochTime3'], axis=1)

#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.o_Xylene","3.feed_4912.o_Xylene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.o_Xylene","3.feed_4914.o_Xylene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.o_Xylene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(o_Xylene_fusion.columns.values)
o_Xylene_fusion[cols] = o_Xylene_fusion[cols].replace('Offline','-1', regex = True)
o_Xylene_fusion[cols] = o_Xylene_fusion[cols].replace('Offline','-1', regex = True)
o_Xylene_fusion[cols] = o_Xylene_fusion[cols].replace('Low Signal','-2', regex = True)
o_Xylene_fusion[cols] = o_Xylene_fusion[cols].replace('In Calibration','-3', regex = True)

for col in  o_Xylene_fusion.columns[0:]:
    o_Xylene_fusion[col] = o_Xylene_fusion[col].apply(pd.to_numeric, errors='coerce')

o_Xylene_fusion.to_csv('/home/amos/Desktop/By_Pollutants/New_Moves_o_Xylene.csv')


# In[73]:


#Quick Maths
def cond (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + row[column]; 
    return total; 
def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
o_Xylene_fusion['Total o_Xylene in Air(ppm)'] = o_Xylene_fusion.apply(cond,axis = 1 );
o_Xylene_fusion['Count of o_Xylene Detects']  = o_Xylene_fusion.apply(cond2,axis = 1 );


# In[74]:


#Visual Tings 
dates = o_Xylene_fusion['EpochTime1']
dates =[pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10), frameon = False) 
plt.subplot(211)
plt.scatter(dates, o_Xylene_fusion['Total o_Xylene in Air(ppm)'], s =30)
plt.title('Total o_Xylene in the Air')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('o_Xylene (ppm)')
plt.subplot(212)
plt.scatter(dates, o_Xylene_fusion['Count of o_Xylene Detects'], s=30)
plt.title('o_Xylene Nonzero Detects in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Pollutants/o_Xylene.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')

