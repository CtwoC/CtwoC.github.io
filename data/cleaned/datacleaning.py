#%%
import pandas as pd

#%%
df_2015 = pd.read_csv("2015.csv")
df_2016 = pd.read_csv("2016.csv")
df_2017 = pd.read_csv("2017.csv")
df_2018 = pd.read_csv("2018.csv")
df_2019 = pd.read_csv("2019.csv")
df_2020 = pd.read_csv("2020.csv")
# %%
df = pd.DataFrame(columns = ['Country', '2020', '2015','2016','2017','2018','2019'])
df[['Country','2020']]=df_2020[['Country name','Ladder score']]
df = df.set_index('Country')
# %%
for index, row in df_2015.iterrows():
    if row['Country'] in df_2020['Country name'].tolist():
        country = row['Country']
        df.loc[country,'2015'] = df_2015.loc[index,'Happiness Score']

#%%
for index, row in df_2016.iterrows():
    if row['Country'] in df_2020['Country name'].tolist():
        country = row['Country']
        df.loc[country,'2016'] = df_2016.loc[index,'Happiness Score']

#%%
for index, row in df_2017.iterrows():
    if row['Country'] in df_2020['Country name'].tolist():
        country = row['Country']
        df.loc[country,'2017'] = df_2017.loc[index,'Happiness.Score']

#%%
for index, row in df_2018.iterrows():
    if row['Country or region'] in df_2020['Country name'].tolist():
        country = row['Country or region']
        df.loc[country,'2018'] = df_2018.loc[index,'Score']

#%%
for index, row in df_2019.iterrows():
    if row['Country or region'] in df_2020['Country name'].tolist():
        country = row['Country or region']
        df.loc[country,'2019'] = df_2019.loc[index,'Score']


# %%
df = df.fillna(0)
# %%
df.to_csv('cleaned.csv')
# %%
