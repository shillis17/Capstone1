import pandas as pd
import scipy.stats as stats

df = pd.read_csv('../data/clean_data.csv')
df_genre = df.drop(['Unnamed: 0', 'QueryName', 'ReleaseDate', 'RequiredAge', 'DLCCount',\
       'Metacritic', 'RecommendationCount', 'SteamSpyOwners',\
       'SteamSpyPlayersEstimate', 'AchievementCount', 'ControllerSupport',\
       'IsFree', 'SubscriptionAvail', 'CategorySinglePlayer',\
       'CategoryMultiplayer', 'CategoryCoop', 'CategoryMMO',\
       'CategoryInAppPurchase', 'CategoryIncludeLevelEditor',\
       'CategoryVRSupport','PriceCurrency', 'PriceInitial', 'PriceFinal', 'Reviews'],axis=1)

df_indie = df[df.GenreIsIndie == True]
df_action = df[df.GenreIsAction == True]
df_adventure = df[df.GenreIsAdventure == True]
df_casual = df[df.GenreIsCasual == True]
df_strategy = df[df.GenreIsStrategy == True]
df_simulation = df[df.GenreIsSimulation == True]
df_rpg = df[df.GenreIsRPG == True]
df_earlyaccess = df[df.GenreIsEarlyAccess == True]
df_sports = df[df.GenreIsSports == True]
df_racing = df[df.GenreIsRacing == True]
df_mmo = df[df.GenreIsMassivelyMultiplayer == True]
df_ftp = df[df.GenreIsFreeToPlay == True]
'''
df_action['TotalRevenue'] = df_action['SteamSpyOwners']*df_action['PriceFinal']
df_indie['TotalRevenue'] = df_indie['SteamSpyOwners']*df_indie['PriceFinal']
df_adventure['TotalRevenue'] = df_adventure['SteamSpyOwners']*df_action['PriceFinal']
df_rpg['TotalRevenue'] = df_rpg['SteamSpyOwners']*df_rpg['PriceFinal']
df_strategy['TotalRevenue'] = df_strategy['SteamSpyOwners']*df_strategy['PriceFinal']
df_simulation['TotalRevenue'] = df_simulation['SteamSpyOwners']*df_simulation['PriceFinal']
df_casual['TotalRevenue'] = df_casual['SteamSpyOwners']*df_casual['PriceFinal']
df_ftp['TotalRevenue'] = df_ftp['SteamSpyOwners']*df_ftp['PriceFinal']
df_earlyaccess['TotalRevenue'] = df_earlyaccess['SteamSpyOwners']*df_earlyaccess['PriceFinal']
df_mmo['TotalRevenue'] = df_mmo['SteamSpyOwners']*df_mmo['PriceFinal']
df_racing['TotalRevenue'] = df_racing['SteamSpyOwners']*df_racing['PriceFinal']
df_sports['TotalRevenue'] = df_sports['SteamSpyOwners']*df_sports['PriceFinal']

data = {'mmo' : df_mmo['TotalRevenue'].mean(),
'action' : df_action['TotalRevenue'].mean(),
'adventure' : df_adventure['TotalRevenue'].mean(),
'rpg' : df_rpg['TotalRevenue'].mean(),
'strategy' : df_strategy['TotalRevenue'].mean(),
'racing' : df_racing['TotalRevenue'].mean(),
'simulation' : df_simulation['TotalRevenue'].mean(),
'sports' : df_sports['TotalRevenue'].mean(),
'earlyaccess' : df_earlyaccess['TotalRevenue'].mean(),
'indie' : df_indie['TotalRevenue'].mean(),
'casual' : df_casual['TotalRevenue'].mean(),
'ftp' : df_ftp['TotalRevenue'].mean()}

reviews = {'mmo' : [df_mmo[df_mmo['Metacritic']!=0]['Metacritic'].mean(),df_mmo['RecommendationCount'].mean()],
'action' : [df_action[df_action['Metacritic']!=0]['Metacritic'].mean(),df_action['RecommendationCount'].mean()],
'adventure' : [df_adventure[df_adventure['Metacritic']!=0]['Metacritic'].mean(),df_adventure['RecommendationCount'].mean()],
'rpg' : [df_rpg[df_rpg['Metacritic']!=0]['Metacritic'].mean(),df_rpg['RecommendationCount'].mean()],
'strategy' : [df_strategy[df_strategy['Metacritic']!=0]['Metacritic'].mean(),df_strategy['RecommendationCount'].mean()],
'racing' : [df_racing[df_racing['Metacritic']!=0]['Metacritic'].mean(),df_racing['RecommendationCount'].mean()],
'simulation' : [df_simulation[df_simulation['Metacritic']!=0]['Metacritic'].mean(),df_simulation['RecommendationCount'].mean()],
'sports' : [df_sports[df_sports['Metacritic']!=0]['Metacritic'].mean(),df_sports['RecommendationCount'].mean()],
'earlyaccess' : [df_earlyaccess[df_earlyaccess['Metacritic']!=0]['Metacritic'].mean(),df_earlyaccess['RecommendationCount'].mean()],
'indie' : [df_indie[df_indie['Metacritic']!=0]['Metacritic'].mean(),df_indie['RecommendationCount'].mean()],
'casual' : [df_casual[df_casual['Metacritic']!=0]['Metacritic'].mean(),df_casual['RecommendationCount'].mean()],
'ftp' : [df_ftp[df_ftp['Metacritic']!=0]['Metacritic'].mean(),df_ftp['RecommendationCount'].mean()]}

revenue = [35744.18,361600.91,974278.43,986870.04,1696986.56,1752667.90,\
           1822275.89,2261507.91,2988753.88,3006711.91,3391165.72,4318509.26]
metacritic = [71,71.49,71.04,81,74.98,70.67,72.75,72.11,73.37,71.32,71.56,73.72]
reccomendation = [14733,269,720,948,627,1047,762,821,1710,1073,1947,4791]
recc_rev_reg = stats.linregress(revenue,reccomendation)
crit_rev_reg = stats.linregress(revenue,metacritic)
'''
data = {'action' : [df_action['SteamSpyPlayersEstimate'].sum(),df_action['SteamSpyOwners'].sum()],
'indie' : [df_indie['SteamSpyPlayersEstimate'].sum(),df_indie['SteamSpyOwners'].sum()],
'adventure' : [df_adventure['SteamSpyPlayersEstimate'].sum(),df_adventure['SteamSpyOwners'].sum()],
'rpg' : [df_rpg['SteamSpyPlayersEstimate'].sum(),df_rpg['SteamSpyOwners'].sum()],
'strategy' : [df_strategy['SteamSpyPlayersEstimate'].sum(),df_strategy['SteamSpyOwners'].sum()],
'simulation' : [df_simulation['SteamSpyPlayersEstimate'].sum(),df_simulation['SteamSpyOwners'].sum()],
'casual' : [df_casual['SteamSpyPlayersEstimate'].sum(),df_casual['SteamSpyOwners'].sum()],
'ftp' : [df_ftp['SteamSpyPlayersEstimate'].sum(),df_ftp['SteamSpyOwners'].sum()],
'earlyaccess' : [df_earlyaccess['SteamSpyPlayersEstimate'].sum(),df_earlyaccess['SteamSpyOwners'].sum()],
'mmo' : [df_mmo['SteamSpyPlayersEstimate'].sum(),df_mmo['SteamSpyOwners'].sum()],
'racing' : [df_racing['SteamSpyPlayersEstimate'].sum(),df_racing['SteamSpyOwners'].sum()],
'sports' : [df_sports['SteamSpyPlayersEstimate'].sum(),df_sports['SteamSpyOwners'].sum()]}
print(data)