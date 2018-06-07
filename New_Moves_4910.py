
# coding: utf-8

# In[13]:


import pandas as pd 
import datetime 
import matplotlib.pyplot as plt


# In[2]:


#Getting the Data 
Benzene = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4910.csv')
Ammonia = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Ammonia/Ammonia_4910.csv')
Black_Carbon = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Black_Carbon/Black_Carbon_4910.csv')
Ethylbenzene =  pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Ethylbenzene/Ethylbenzene_4910.csv')
Hydrogen_Sulfide = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4910.csv')
r3_Methylpentane = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/3_Methylpentane/3_Methylpentane_4910.csv')
N_Heptane = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Heptane/N_Heptane_4910.csv')
N_Hexane = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Hexane/N_Hexane_4910.csv')
N_Octane = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/N_Octane/N_Octane_4910.csv')
PM_2_5 = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/PM_2_5/PM_2_5_4910.csv')
Toluene = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4910.csv')
r1_2_3_Trimethylbenzene = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_2_3_Trimethylbenzene/1_2_3_Trimethylbenzene_4910.csv')
r1_2_4_Trimethylbenzene = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_2_4_Trimethylbenzene/1_2_4_Trimethylbenzene_4910.csv')
r1_3_5_Trimethylbenzene = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/1_3_5_Trimethylbenzene/1_3_5_Trimethylbenzene_4910.csv')
r2_2_4_Trimethylpentane = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/2_2_4_Trimethylpentane/2_2_4_Trimethylpentane_4910.csv')
m_p_Xylene = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/m_p_Xylene/m_p_Xylene_4910.csv')
o_Xylene = pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/o_Xylene/o_Xylene_4910.csv')


# In[3]:


#Concatinating All Polutant together 
#Merging the Data 
R4910_All_Pollutants = [Ammonia,Benzene,Black_Carbon,Ethylbenzene,Hydrogen_Sulfide,r3_Methylpentane,
N_Heptane,
N_Hexane,
N_Octane,
PM_2_5,
Toluene,
r1_2_3_Trimethylbenzene,
r1_2_4_Trimethylbenzene,
r1_3_5_Trimethylbenzene,
r2_2_4_Trimethylpentane,
m_p_Xylene,
o_Xylene]
R4910_Pollutant_Fusion = pd.concat(R4910_All_Pollutants,axis=1,join= "inner")
#Richmond_Total_Fusion.to_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/All_Richmond_fused.csv')


# In[4]:


#Test to see if Data nerged and for future tests as well 
R4910_Pollutant_Fusion.head(4)


# In[5]:


#Cleaning the Data 
# Removing the Repetitve Epoch Times 
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6', 'EpochTime7', 'EpochTime8', 'EpochTime9', 'EpochTime10', 'EpochTime11', 'EpochTime12', 'EpochTime13', 'EpochTime14', 'EpochTime15', 'EpochTime16', 'EpochTime17']}
R4910_Pollutant_Fusion = R4910_Pollutant_Fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
R4910_Pollutant_Fusion = R4910_Pollutant_Fusion.drop(['EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6', 'EpochTime7', 'EpochTime8', 'EpochTime9', 'EpochTime10', 'EpochTime11', 'EpochTime12','EpochTime13', 'EpochTime14', 'EpochTime15', 'EpochTime16', 'EpochTime17'], axis=1)


# In[6]:


#Cleaning the Data
#Removing offline, callibration etc 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.Toluene","3.feed_4912.Toluene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.Toluene","3.feed_4914.Toluene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Toluene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = list(R4910_Pollutant_Fusion.columns.values)
R4910_Pollutant_Fusion[cols] = R4910_Pollutant_Fusion[cols].replace('Offline','-1', regex = True)
R4910_Pollutant_Fusion[cols] = R4910_Pollutant_Fusion[cols].replace('Offline','-1', regex = True)
R4910_Pollutant_Fusion[cols] = R4910_Pollutant_Fusion[cols].replace('Low Signal','-2', regex = True)
R4910_Pollutant_Fusion[cols] = R4910_Pollutant_Fusion[cols].replace('In Calibration','-3', regex = True)


# In[7]:


for col in  R4910_Pollutant_Fusion.columns[0:]:
    R4910_Pollutant_Fusion[col] = R4910_Pollutant_Fusion[col].apply(pd.to_numeric, errors='coerce')


# In[8]:


R4910_Pollutant_Fusion.tail(5)


# In[9]:


R4910_Pollutant_Fusion.to_csv('/home/amos/Desktop/By_Location/New_Moves_4910.csv')


# In[11]:


def cond2 (row): 
    total = 0
    for column in cols[1:]: 
        if row[column]> 0 : 
            total = total + 1; 
    return total; 
        
R4910_Pollutant_Fusion['Pollutant Detects in 4910']  = R4910_Pollutant_Fusion.apply(cond2,axis = 1 );


# In[15]:


#Visual Tings 
dates = R4910_Pollutant_Fusion['EpochTime1']
dates = [pd.to_datetime(d, unit ='s') for d in dates]
plt.figure(1)
plt.figure(figsize=(20,10)) 
plt.scatter(dates,R4910_Pollutant_Fusion['Pollutant Detects in 4910'])
plt.title('Counts of Pollutant Detects in Location 4910 in Time')
plt.xlabel('Date')
plt.xticks(rotation=90)
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('/home/amos/Desktop/By_Location/R4910_Pollutant.png')
plt.close()
#plt.show(block = False)
get_ipython().magic(u'matplotlib inline')

