import pandas as pd

#Clean my dataframe, remove uneeded information from the dataframe so the data is more fucused.
df = pd.read_csv('data/games-features.csv')
df = df.drop(['QueryID','ResponseID','ResponseName',\
              'DemoCount','DeveloperCount',\
              'MovieCount','PackageCount',\
              'PublisherCount','ScreenshotCount',\
              'SteamSpyOwnersVariance','SteamSpyPlayersVariance',\
              'AchievementHighlightedCount','FreeVerAvail',\
              'PlatformWindows','PlatformLinux',\
              'PlatformMac','PCReqsHaveMin','PCReqsHaveRec',\
              'LinuxReqsHaveMin','LinuxReqsHaveRec',\
              'MacReqsHaveMin','MacReqsHaveRec','SupportEmail',\
              'SupportURL', 'AboutText','Background',\
              'ShortDescrip','DetailedDescrip','DRMNotice',\
              'ExtUserAcctNotice','HeaderImage','LegalNotice',\
              'SupportedLanguages', 'Website', 'PCMinReqsText',\
               'PCRecReqsText','LinuxMinReqsText','LinuxRecReqsText',\
              'MacMinReqsText','MacRecReqsText','CategoryIncludeSrcSDK'],axis=1)

#Remove duplicate columns
df = df.drop_duplicates()
#Remove games that are no longer for sale and remove the column
df = df[df.PurchaseAvail != False]
df = df.drop(['PurchaseAvail'],axis=1)
#Remove any non games as it will effect data of games
df = df[df.GenreIsNonGame != True]
df = df.drop(['GenreIsNonGame'],axis=1)
#Save dataframe for easy access in the future
df.to_csv('data/clean_data.csv')