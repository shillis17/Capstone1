import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/clean_data.csv')
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


def graph(data,title,savePath):
    fig, axs = plt.subplots(figsize=(20,16))    
    plt.rcParams.update({'font.size': 22})
    plt.title(title)
    names = list(data.keys())
    values = list(data.values())
    axs.bar(names,values)
    plt.xticks(rotation=90)
    plt.savefig(savePath)
    
data = {'indie' : df_genre['GenreIsIndie'].sum(),
'action' : df_genre['GenreIsAction'].sum(),
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

graph(data,'Genre Frequency','images/GenreFrequencyBar.png')

data = {'indie' : df_indie['PriceFinal'].sum(),
'action' : df_action['PriceFinal'].sum(),
'adventure' : df_adventure['PriceFinal'].sum(),
'strategy' : df_strategy['PriceFinal'].sum(),
'simulation' : df_simulation['PriceFinal'].sum(),
'casual' : df_casual['PriceFinal'].sum(),
'rpg' : df_rpg['PriceFinal'].sum(),
'earlyaccess' : df_earlyaccess['PriceFinal'].sum(),
'sports' : df_sports['PriceFinal'].sum(),
'racing' : df_racing['PriceFinal'].sum(),
'mmo' : df_mmo['PriceFinal'].sum(),
'ftp' : df_ftp['PriceFinal'].sum()}

graph(data,'Genre Game Costs','images/GenreGameCostsBar.png')

data = {'sports' : df_sports['PriceFinal'].mean(),
'mmo' : df_mmo['PriceFinal'].mean(),
'simulation' : df_simulation['PriceFinal'].mean(),
'racing' : df_racing['PriceFinal'].mean(),
'earlyaccess' : df_earlyaccess['PriceFinal'].mean(),
'strategy' : df_strategy['PriceFinal'].mean(),
'rpg' : df_rpg['PriceFinal'].mean(),
'action' : df_action['PriceFinal'].mean(),
'adventure' : df_adventure['PriceFinal'].mean(), 
'indie' : df_indie['PriceFinal'].mean(),
'casual' : df_casual['PriceFinal'].mean(),
'ftp' : df_ftp['PriceFinal'].mean()}

graph(data,'Genre Game Costs Average','images/GenreGameCostsAvgBar.png')

data = {'action' : df_action['SteamSpyOwners'].sum(),
'indie' : df_indie['SteamSpyOwners'].sum(),
'adventure' : df_adventure['SteamSpyOwners'].sum(),
'rpg' : df_rpg['SteamSpyOwners'].sum(),
'strategy' : df_strategy['SteamSpyOwners'].sum(),
'simulation' : df_simulation['SteamSpyOwners'].sum(),
'casual' : df_casual['SteamSpyOwners'].sum(),
'ftp' : df_ftp['SteamSpyOwners'].sum(),
'earlyaccess' : df_earlyaccess['SteamSpyOwners'].sum(),
'mmo' : df_mmo['SteamSpyOwners'].sum(),
'racing' : df_racing['SteamSpyOwners'].sum(),
'sports' : df_sports['SteamSpyOwners'].sum()}

graph(data,'Genre Game Owners','images/GenreSteamSpyOwners.png')

data = {'action' : df_action['SteamSpyPlayersEstimate'].sum(),
'indie' : df_indie['SteamSpyPlayersEstimate'].sum(),
'adventure' : df_adventure['SteamSpyPlayersEstimate'].sum(),
'rpg' : df_rpg['SteamSpyPlayersEstimate'].sum(),
'strategy' : df_strategy['SteamSpyPlayersEstimate'].sum(),
'simulation' : df_simulation['SteamSpyPlayersEstimate'].sum(),
'casual' : df_casual['SteamSpyPlayersEstimate'].sum(),
'ftp' : df_ftp['SteamSpyPlayersEstimate'].sum(),
'earlyaccess' : df_earlyaccess['SteamSpyPlayersEstimate'].sum(),
'mmo' : df_mmo['SteamSpyPlayersEstimate'].sum(),
'racing' : df_racing['SteamSpyPlayersEstimate'].sum(),
'sports' : df_sports['SteamSpyPlayersEstimate'].sum()}

graph(data,'Genre Game players','images/GenreSteamSpyPlayers.png')

data = {'action' : df_action['TotalRevenue'].sum(),
'indie' : df_indie['TotalRevenue'].sum(),
'strategy' : df_strategy['TotalRevenue'].sum(),
'rpg' : df_rpg['TotalRevenue'].sum(),
'adventure' : df_adventure['TotalRevenue'].sum(),
'simulation' : df_simulation['TotalRevenue'].sum(),
'earlyaccess' : df_earlyaccess['TotalRevenue'].sum(),
'casual' : df_casual['TotalRevenue'].sum(),
'racing' : df_racing['TotalRevenue'].sum(),
'sports' : df_sports['TotalRevenue'].sum(),
'mmo' : df_mmo['TotalRevenue'].sum(),
'ftp' : df_ftp['TotalRevenue'].sum()}

graph(data,'Genre Revenue','images/GenreRevenue.png')

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

graph(data,'Genre Revenue Average','images/GenreRevenueAverage.png')