import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('data/clean_data.csv')
df_genre = df.drop(['Unnamed: 0', 'QueryName', 'ReleaseDate', 'RequiredAge', 'DLCCount',\
       'Metacritic', 'RecommendationCount', 'SteamSpyOwners',\
       'SteamSpyPlayersEstimate', 'AchievementCount', 'ControllerSupport',\
       'IsFree', 'SubscriptionAvail', 'CategorySinglePlayer',\
       'CategoryMultiplayer', 'CategoryCoop', 'CategoryMMO',\
       'CategoryInAppPurchase', 'CategoryIncludeLevelEditor',\
       'CategoryVRSupport','PriceCurrency', 'PriceInitial', 'PriceFinal', 'Reviews'],axis=1)

data = {'action' : df_genre['GenreIsAction'].sum(),
'adventure' : df_genre['GenreIsAdventure'].sum(),
'casual' : df_genre['GenreIsCasual'].sum(),
'strategy' : df_genre['GenreIsStrategy'].sum(),
'simulation' : df_genre['GenreIsSimulation'].sum(),
'rpg' : df_genre['GenreIsRPG'].sum(),
'earlyaccess' : df_genre['GenreIsEarlyAccess'].sum(),
'sports' : df_genre['GenreIsSports'].sum(),
'racing' : df_genre['GenreIsRacing'].sum(),
'mmo' : df_genre['GenreIsMassivelyMultiplayer'].sum(),
'ftp' : df_genre['GenreIsFreeToPlay'].sum()}

fig1, axs = plt.subplots(figsize=(16,14))
plt.title('Genre Frequency')
names = list(data.keys())
values = list(data.values())
axs.bar(names,values)
plt.xticks(rotation=90)
plt.savefig('images/GenreFrequencyBar.png')

fig1, axs = plt.subplots(figsize=(14,14))
plt.title('Genre Proportions')
names = list(data.keys())
values = list(data.values())
axs.pie(values)
axs.legend(loc='right',bbox_to_anchor=(1.05, .5),labels=names)
plt.savefig('images/GenreFrequencyPie.png')