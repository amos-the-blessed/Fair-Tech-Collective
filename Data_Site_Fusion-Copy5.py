
# coding: utf-8

# In[1]:


import pandas as pd 
import glob, os
from datetime import datetime


# In[2]:


# Fusing by Location(Toluene)
Tol_df01= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4901.csv')   
Tol_df02= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4902.csv')                   
Ben_df01= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4901.csv')  
Ben_df02= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4902.csv')
HyS_df01= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4901.csv')
HyS_df02= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4902.csv')


# In[3]:


#merger1=pd.merge(Tol_df01,_df01), on='EpochTime', how='inner')
#merger2= pd.merge(Tol_df02,Ben_df02, on="EpochTime", how='inner')
#merger3= pd.merge(HyS_df02,Tol_df02, on="EpochTime", how='inner')
Rodeo_sites = [Tol_df01,Tol_df02,Ben_df01,Ben_df02,HyS_df01, HyS_df02]
Rodeo_fusion= pd.concat(Rodeo_sites,axis=1, join= "inner")


# In[4]:


Rodeo_fusion.to_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Rodeo_fused.csv')
Rodeo_fusion.head(5)


# In[5]:


#Richmond Refinery 
Ben_NRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4911.csv') 
Tol_NRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4911.csv') 
HyS_NRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4911.csv') 
Ben_PRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4913.csv')
Tol_PRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4913.csv')
HyS_PRich= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4913.csv')


# In[6]:


Richmond_Refinery_sites= [Ben_NRich,Tol_NRich,HyS_NRich,Ben_PRich,Tol_PRich,HyS_PRich]
Richmond_Ref_fusion = pd.concat(Richmond_Refinery_sites,axis=1, join= "inner")
Richmond_Ref_fusion.to_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Richmond_Ref_fused.csv')


# In[7]:


Richmond_Ref_fusion.head(5)


# In[8]:


#Richmond_Community 
Ben_NRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4912.csv') 
Tol_NRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4912.csv') 
HyS_NRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4912.csv') 
Ben_PRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4914.csv')
Tol_PRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4914.csv')
HyS_PRichC= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4914.csv')


# In[9]:


Richmond_Community_sites= [Ben_NRichC,Tol_NRichC,HyS_NRichC,Ben_PRichC,Tol_PRichC,HyS_PRichC]
Richmond_Comm_fusion = pd.concat(Richmond_Community_sites,axis=1, join= "inner")
Richmond_Comm_fusion.to_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Richmond_Comm_fused.csv')


# In[10]:


Richmond_Comm_fusion.head(5)


# In[11]:


#Atchinson_Refinery
Ben_Atch_Ref= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4909.csv') 
Tol_Atch_Ref= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4909.csv') 
HyS_Atch_Ref= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4909.csv') 


# In[12]:


Atchinson_Ref = [Ben_Atch_Ref,Tol_Atch_Ref,HyS_Atch_Ref ]
Atchinson_Ref_fusion=pd.concat(Atchinson_Ref,axis=1, join= "inner")
Atchinson_Ref_fusion.to_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Atchinson_Ref.csv')


# In[13]:


Atchinson_Ref_fusion.head(5)


# In[14]:


#Atchinson_Community
Ben_Atch_Comm= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Benzene/Benzene_4910.csv') 
Tol_Atch_Comm= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Toluene/Toluene_4910.csv') 
HyS_Atch_Comm= pd.read_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Hydrogen_Sulfide/Hydrogen_Sulfide_4910.csv') 


# In[15]:


Atchinson_Comm = [Ben_Atch_Comm,Tol_Atch_Comm,HyS_Atch_Comm ]
Atchinson_Comm_fusion=pd.concat(Atchinson_Comm,axis=1, join= "inner")
Atchinson_Comm_fusion.to_csv('/home/amos/Desktop/Esdr/Analyzing_by_Polutants_2/Atchinson_Comm.csv')


# In[16]:


Atchinson_Comm_fusion.head(5)


# In[17]:


BenNRichComm = Richmond_Comm_fusion['3.feed_4912.Toluene']
BenNRichRef =  Richmond_Ref_fusion['3.feed_4911.Toluene']
abc =pd.concat([BenNRichComm, BenNRichRef], axis=1)
abc['3.feed_4912.Toluene'] = abc['3.feed_4912.Toluene'].replace('Offline', '-1', regex = True)
abc['3.feed_4912.Toluene'] = abc['3.feed_4912.Toluene'].replace('In Calibration', '-2', regex = True)
abc['3.feed_4912.Toluene'] = abc['3.feed_4912.Toluene'].replace('Low Signal', '-3', regex = True)
abc['3.feed_4911.Toluene'] = abc['3.feed_4911.Toluene'].replace('Offline', '-1', regex = True)
abc['3.feed_4911.Toluene'] = abc['3.feed_4911.Toluene'].replace('In Calibration', '-2', regex = True)
abc['3.feed_4911.Toluene'] = abc['3.feed_4911.Toluene'].replace('Low Signal', '-3', regex = True)
abc['3.feed_4912.Toluene'] = pd.to_numeric(abc['3.feed_4912.Toluene'])
abc['3.feed_4911.Toluene'] = pd.to_numeric(abc['3.feed_4911.Toluene'])


# In[18]:


P1=abc.loc[(abc['3.feed_4912.Toluene'] == 0) & (abc['3.feed_4911.Toluene'] == 0)]
P2=abc.loc[(abc['3.feed_4912.Toluene'] != 0 ) & (abc['3.feed_4911.Toluene'] == 0 )]
P3 = abc.loc[(abc['3.feed_4912.Toluene'] == 0 ) & (abc['3.feed_4911.Toluene'] != 0 )]
P4 = abc.loc[(abc['3.feed_4912.Toluene'] != 0) & (abc['3.feed_4911.Toluene']  != 0)]


# In[19]:


BenNRichComm_2 = Richmond_Comm_fusion['3.feed_4914.Toluene']
BenNRichRef_2 =  Richmond_Ref_fusion['3.feed_4913.Toluene']
dfe =pd.concat([BenNRichComm_2, BenNRichRef_2], axis=1)
dfe['3.feed_4914.Toluene'] = dfe['3.feed_4914.Toluene'].replace('Offline', '-1', regex = True)
dfe['3.feed_4914.Toluene'] = dfe['3.feed_4914.Toluene'].replace('In Calibration', '-2', regex = True)
dfe['3.feed_4914.Toluene'] = dfe['3.feed_4914.Toluene'].replace('Low Signal', '-3', regex = True)
dfe['3.feed_4913.Toluene'] = dfe['3.feed_4913.Toluene'].replace('Offline', '-1', regex = True)
dfe['3.feed_4913.Toluene'] = dfe['3.feed_4913.Toluene'].replace('In Calibration', '-2', regex = True)
dfe['3.feed_4913.Toluene'] = dfe['3.feed_4913.Toluene'].replace('Low Signal', '-3', regex = True)
dfe['3.feed_4914.Toluene'] = pd.to_numeric(dfe['3.feed_4914.Toluene'])
dfe['3.feed_4913.Toluene'] = pd.to_numeric(dfe['3.feed_4913.Toluene'])


# In[20]:


S1=dfe.loc[(dfe['3.feed_4914.Toluene'] == 0) & (dfe['3.feed_4913.Toluene'] == 0)]
S2=dfe.loc[(dfe['3.feed_4914.Toluene'] != 0 ) & (dfe['3.feed_4913.Toluene'] == 0 )]
S3 = dfe.loc[(dfe['3.feed_4914.Toluene'] == 0 ) & (dfe['3.feed_4913.Toluene'] != 0 )]
S4 = dfe.loc[(dfe['3.feed_4914.Toluene'] != 0) & (dfe['3.feed_4913.Toluene']  != 0)]


# In[21]:


BenNAtchComm_2 = Atchinson_Comm_fusion['3.feed_4910.Toluene']
BenNAtchRef_2 =  Atchinson_Ref_fusion['3.feed_4909.Toluene']
rep =pd.concat([BenNAtchComm_2 , BenNAtchRef_2], axis=1)
rep['3.feed_4909.Toluene'] = rep['3.feed_4909.Toluene'].replace('Offline', '-1', regex = True)
rep['3.feed_4909.Toluene'] = rep['3.feed_4909.Toluene'].replace('In Calibration', '-2', regex = True)
rep['3.feed_4909.Toluene'] = rep['3.feed_4909.Toluene'].replace('Low Signal', '-3', regex = True)
rep['3.feed_4910.Toluene'] = rep['3.feed_4910.Toluene'].replace('Offline', '-1', regex = True)
rep['3.feed_4910.Toluene'] = rep['3.feed_4910.Toluene'].replace('In Calibration', '-2', regex = True)
rep['3.feed_4910.Toluene'] = rep['3.feed_4910.Toluene'].replace('Low Signal', '-3', regex = True)
rep['3.feed_4909.Toluene'] = pd.to_numeric(rep['3.feed_4909.Toluene'])
rep['3.feed_4910.Toluene'] = pd.to_numeric(rep['3.feed_4910.Toluene'])


# In[22]:


T1=rep.loc[(rep['3.feed_4910.Toluene'] == 0) & (rep['3.feed_4909.Toluene'] == 0)]
T2=rep.loc[(rep['3.feed_4910.Toluene'] != 0 ) & (rep['3.feed_4909.Toluene'] == 0 )]
T3 = rep.loc[(rep['3.feed_4910.Toluene'] == 0 ) & (rep['3.feed_4909.Toluene']  != 0 )]
T4 = rep.loc[(rep['3.feed_4910.Toluene'] != 0) & (rep['3.feed_4909.Toluene']  != 0)]


# In[23]:


print (P1.size)
print (P2.size)
print (P3.size)
print (P4.size)


# In[24]:


print (T1.size)
print (T2.size)
print (T3.size)
print (T4.size)


# In[25]:


print (S1.size)
print (S2.size)
print (S3.size)
print (S4.size)

