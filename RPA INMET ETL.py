#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# criar os DataFrames para as tabelas
df1 = pd.read_excel('C:\\Python\\Base_Temperatura.xlsx')
df2 = pd.read_csv('C:\\Python\\dados_inmet.csv', na_values='', delimiter=';' ,decimal=',')


# In[3]:


# renomear as colunas da segunda tabela
df2 = df2.rename(columns={
    'Pressao Ins. (hPa)': 'PRE_INST',
    'Pressao Max. (hPa)': 'PRE_MAX',
    'Radiacao (KJ/m²)': 'RAD_GLO',
    'Pto Orvalho Ins. (C)': 'PTO_INT',
    'Temp. Min. (C)': 'TEM_MIN',
    'Pto Orvalho Max. (C)': 'PTO_MAX',
    'Dir. Vento (m/s)': 'VEM_DIR',
    'Chuva (mm)': 'CHUVA',
    'Pressao Min. (hPa)': 'PRE_MIN',
    'Umi. Max. (%)': 'UMD_MAX',
    'Vel. Vento (m/s)': 'VEN_VEL',
    'Pto Orvalho Min. (C)': 'PTO_MIN',
    'Temp. Max. (C)': 'TEM_MAX',
    'Raj. Vento (m/s)': 'VEM_RAJ',
    'Temp. Ins. (C)': 'TEM_INS',
    'Umi. Ins. (%)': 'UMD_INS',
    'Hora (UTC)': 'HR_MEDICAO',
    'Umi. Min. (%)':'UMD_MIN',
    'Data':'DT_MEDICAO'
})


# In[4]:


# converter a coluna de data para o formato yyyy-mm-dd
df2['DT_MEDICAO'] = pd.to_datetime(df2['DT_MEDICAO'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')


# In[5]:


# criar as novas colunas no df2 com os valores desejados
df2 = df2.assign(DC_NOME='Ribas do Rio Pardo', LV_LATITUDE=-20.46666666, UF='MS', VL_LONGITUDE=-53.76305555, CD_ESTACAO='A756')


# In[6]:


# concatenar as duas tabelas
df_concat = pd.concat([df1, df2], axis=0, ignore_index=True)


# In[7]:


# salvar a tabela concatenada no arquivo original
df_concat.to_excel('C:\\Python\\Base_Temperatura.xlsx', index=False)

