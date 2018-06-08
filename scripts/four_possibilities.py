
import pandas as pd 
# Putting the data into dataframes. 
#Richmond Refinery 
Ben_NRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4911.csv') 
Tol_NRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4911.csv') 
HyS_NRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4911.csv') 
Ben_PRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4913.csv')
Tol_PRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4913.csv')
HyS_PRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4913.csv')
#Richmond_Community 
Ben_NRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4912.csv') 
Tol_NRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4912.csv') 
HyS_NRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4912.csv') 
Ben_PRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4914.csv')
Tol_PRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4914.csv')
HyS_PRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4914.csv')

# In[4]:

#Concatinating All Polutant sensor readings for Richmond together 
Richmond_All_sites = [Ben_NRich,Ben_NRichC,Tol_NRich,Tol_NRichC,HyS_NRich,HyS_NRichC,Ben_PRich,Ben_PRichC,Tol_PRich,Tol_PRichC,HyS_PRich,HyS_PRichC]
Richmond_Total_Fusion = pd.concat(Richmond_All_sites,axis=1,join= "inner")
#Richmond_Total_Fusion.to_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/All_Richmond_fused.csv')

Richmond_Total_Fusion.head(4)
# In[5]:

#Data Cleaning: The data ususally contains some text - the following lines replaces the text 
#replacements = {'Offline':'-1','In Calibration': '-2', 'Low Signal':'-3'}
#"3.feed_4911.Toluene","3.feed_4912.Toluene","Type","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.Toluene","3.feed_4914.Toluene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Toluene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide
cols = ["3.feed_4911.Benzene","3.feed_4912.Benzene","3.feed_4911.Toluene","3.feed_4912.Toluene","3.feed_4911.Hydrogen_Sulfide","3.feed_4914.Benzene","3.feed_4913.Toluene","3.feed_4914.Toluene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Toluene","3.feed_4913.Hydrogen_Sulfide","3.feed_4914.Hydrogen_Sulfide"]
Richmond_Total_Fusion[cols] = Richmond_Total_Fusion[cols].replace('Offline','-1', regex = True)
Richmond_Total_Fusion[cols] = Richmond_Total_Fusion[cols].replace('Offline','-1', regex = True)
Richmond_Total_Fusion[cols] = Richmond_Total_Fusion[cols].replace('Low Signal','-2', regex = True)
Richmond_Total_Fusion[cols] = Richmond_Total_Fusion[cols].replace('In Calibration','-3', regex = True)

# After cleaning the data- coerce the data to make sure all was numeric. 

for col in  Richmond_Total_Fusion.columns[0:]:
    Richmond_Total_Fusion[col] = Richmond_Total_Fusion[col].apply(pd.to_numeric, errors='coerce')

# In[7]:
#Because headers all had title EopchTime - to differentiate the headers the following the lines helped with that.
d = {'EpochTime': ['EpochTime1', 'EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6', 'EpochTime7', 'EpochTime8', 'EpochTime9', 'EpochTime10', 'EpochTime11', 'EpochTime12']}
Richmond_Total_Fusion = Richmond_Total_Fusion.rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c).rename(columns=lambda c: d[c].pop(0) if c in d.keys() else c)     
Richmond_Total_Fusion = Richmond_Total_Fusion.drop(['EpochTime2', 'EpochTime3', 'EpochTime4', 'EpochTime5', 'EpochTime6', 'EpochTime7', 'EpochTime8', 'EpochTime9', 'EpochTime10', 'EpochTime11', 'EpochTime12'], axis=1)
# In[9]:
df =Richmond_Total_Fusion
df1= Richmond_Total_Fusion

# In[56]:
df1.to_csv('/home/amos/Desktop/Esdr/fusion.csv')
# In[30]:
test = Richmond_Total_Fusion.loc[(Richmond_Total_Fusion['3.feed_4911.Hydrogen_Sulfide'] != 0 )]
# In[31]:
test.tail(6)

# In[10]:

#Defining the 4 possibilities

df = df.loc[(df['3.feed_4911.Benzene'] == 0) & (df['3.feed_4912.Benzene']== 0) & 
            (df['3.feed_4911.Toluene']== 0) & (df['3.feed_4912.Toluene']== 0) & 
            (df['3.feed_4911.Hydrogen_Sulfide']== 0) & (df['3.feed_4912.Hydrogen_Sulfide']== 0) & 
            (df['3.feed_4913.Benzene']== 0) & (df['3.feed_4914.Toluene']== 0) & 
            (df['3.feed_4913.Hydrogen_Sulfide']== 0) & (df['3.feed_4913.Toluene']== 0) &
            (df['3.feed_4914.Hydrogen_Sulfide']== 0) & (df['3.feed_4913.Toluene']== 0) ]


# In[11]:


df.to_csv('/home/amos/Desktop/Esdr/zerofusion.csv')


# In[53]:


test = df.loc[(df['3.feed_4911.Benzene'] > 0) | (df['3.feed_4912.Benzene']> 0) |
            (df['3.feed_4911.Toluene'] > 0) |(df['3.feed_4912.Toluene'] > 0) | 
            (df['3.feed_4911.Hydrogen_Sulfide'] > 0) | (df['3.feed_4912.Hydrogen_Sulfide'] > 0)| 
            (df['3.feed_4913.Benzene'] > 0) | (df['3.feed_4914.Toluene']> 0) or 
            (df['3.feed_4913.Hydrogen_Sulfide']== 0) | (df['3.feed_4913.Toluene']== 0) |
            (df['3.feed_4914.Hydrogen_Sulfide']== 0) | (df['3.feed_4913.Toluene']== 0) ]


# In[1]:


df

