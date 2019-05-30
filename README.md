# Capstone1
## Steam Game Genre Analysis


### Table of Contents
<!--ts-->
 * [Description](#description)
 * [Process](#process)
 * [Visualization](#visualization)
 * [Analysis](#analysis)
 * [Conclusion](#conclusion)
 * [Future](#future)
<!--te-->


# Capstone1
## Steam Game Genre Analysis


### Table of Contents
<!--ts-->
 * [Description](#description)
 * [Process](#process)
 * [Visualization](#visualization)
 * [Analysis](#analysis)
 * [Conclusion](#conclusion)
 * [Future](#future)
<!--te-->

### Description

I have researched the profitability of different genres of the games on the popular gaming platform Steam. The reason I have done this research is that lately, most large title games that have been released have fallen under the genres of Action or Adventure. This research is based on the question, are these genres more inclined to make more money than the other genres?

### Process

To begin my project, I looked for a suitable data set that contains the information I require, this information is the title of each game, genre(s), the number of owners, the number of players, and the cost of each game.

From this information, I can use the sample to estimate the amount of ‘player drop-off’ or players that own the game but no longer play the game, revenue from the game based on sales and price points of the game.

The data set I found and used for my project is called [Steam Game Data] (https://data.world/craigkelly/steam-game-data) from data.world. Using this dataset, I first put the data into a Pandas data-frame so I can get familiar with my data and see if there is any data in the data frame irrelevant to my project aim. During this step, I found that there were many columns that are not useful for my aim. After trimming the extraneous data from my data-frame I began to graph my results.

### Visualization
    These graphs were constructed using Python’s Matplotlib library.

The first step was to see the portions of genres that my data included to do this I constructed a bar graph to see the proportions of each genre.

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreFrequencyBar.png)


From this graph we can see that the Indie genre has the most games in it, however all the games in the indie genre are also in other genres (most games have more than just one genre) and the only requirement to be in the Indie genre is the game was made by an independent game developer I made the same proportion visualization graphs without the Indie genre showing a more accurate display of the proportions of the game genres.

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreFrequencyBarNoIndie.png)


From here it is easier to see that the genres Action, Adventure, and Casual contain the most games in this dataset. These simple graphs highlight the saturation of games in the Action and Adventure genres that were stated in my question.
From here I wanted to see more about the specific details in each genre. The first step was to find the costs of games in each genre. The next graph visualizes the cost of all games belonging to each genre.

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreGameCostsBar.png)

However, there is little use to the total cost of each genre as some genres contain many more games the smaller genres. The next visualization uses the mean cost for each game to account for the size gap in each of the genres to get a better understanding of the per game cost for the consumer of each genre.

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreGameCostsAvgBar.png)

What stands out the most to me from this last graph is the fact the Action and Adventure genres were not the top average cost but are more towards the bottom end despite being in the top 3 cost total for the genres.

From this point I wanted to find the revenue generated by each of the games, the first step to this is to analyze the number of people that purchased each of the games. 

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreSteamSpyOwners.png)

From this visualization, I could see that the Action genre has almost over two times the amount of sales of the other categories. After using the information from the previous graphs plotted the estimated revenue for each of the genres based on the sale price of the games multiplied by the number of purchases for each game.

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreRevenue.png)

Unsurprisingly, the graph does not appear to have changed much from the previous one since the genres that contain more games have made more revenue. To combat this, I wanted to find the average revenue per game for the genres to make a more fair comparison, as the aim for my research is done certain genres make more money per game than others. 

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreRevenueAverage.png)

Now I have used the means to make the graph this time we can see that the MMO genre makes the most revenue per game, followed by the Action and Adventure genres. According to this data, the Action and Adventure genres are inclined to make more money per game than most other genres.

### Analysis
    While the visuals are a great way to summarize my data I want to look more into specifics and draw conclusions about why the total revenue is greater for certain games.
    
From the data that was collected, I want to construct solid conclusions about my data supported by statistical analysis. The graphs show that the top 3 genres are MMO, Adventure, and Action. 

To analyze the data more closely I want to look at the exact numbers themselves to get a more in-depth understanding and increase my ability to more accurately draw conclusions about the data and explain the reasoning behind Action and Adventure having more potential revenue than the other genres.

The exact numbers for the amount of average revenue for each game is as follows

    MMO: 4,318,509.26
    Action: 3,391,165.72
    Adventure: 3,006,711.91
    RPG: 2,988,753.88
    Strategy: 2,261,507.91
    Racing: 1,822,275.89
    Simulation: 1,752,667.60
    Sports: 1,696,986.56
    Early Access: 986,870.04
    Indie: 974,278.43
    Casual: 361,600.91
    FTP: 35,744.18

Free to play is the least revenue making genre is understood as something is for anyone to access the basic game will not make as much money as a game that costs money to play, however the data only takes into account the money spent on the game traceable through Steam, meaning that the transactions that where handled by the Steam billing system. Many of these games have IAP or in-app purchases are through the game developers own website or billing system meaning that while the game is free and you can play it without spending money there is potential for more revenue than what is recorded in this data-set.

The Strategy, Racing, Simulation and Sports genres not being at the top of the list is also understandable as the genres are aimed at a smaller audience than Action, Adventure, RPG and MMO.
These games are made for people are into the genre, and people are not into sports will not enjoy playing a sports game or will be inclined to purchase such games. The RPG, Adventure, MMO, and Action genres are much broader in how a game is classified as their genre, leading to a broader audience and proportionally more sales.

The most surprising data was that casual gaming was so low on the revenue list as casual games have a lower cost to develop and are made for the broadest audience possible. 


For a more detailed insight into the specifics of the games, I investigated the average review scores for each of the genres to see if the genres with more revenue have higher reviews for their games usually meaning that the games are better received by the population. 

|Genre|Metacritic Score|Recommendations|Revenue|
|-------|--------------------|-----------------------|----------|
|MMO|73.72|4791|$4,318,509.26|
|Action|71.56|1947|$3,391,165.72|
|Adventure|71.32|1073|$3,006,711.91|
|RPG|73.37|1710|$2,988,753.88|
|Strategy|72.11|821|$2,261,507.91|
|Racing|72.75|762|$1,822,275.89|
|Simulation|70.67|1047|$1,752,667.90|
|Sports|74.98|627|$1,696,986.56|
|Early Access|81.00|948|$986,870.04|
|Indie|71.04|720|$974,278.43|
|Casual|71.49|269|$361,600.91|
|FTP|71.00|14733|$35,744.18|

From the table above the higher revenue games have, the more recommendations the game receives, however, there does not appear to be a pattern in the Metacritic scores, to get a closer view of the correlation I ran linear regression tests on the data to gain insight about the correlation of revenue to recommendations and Metacritic scores.

The correlation value for revenue to recommendations received was r = -0.25

The correlation value for revenue to Metacritic scores was r = -0.04

These low values mean that there is not a strong correlation between either of these measurements.


### Conclusion
    The data I obtained represents a population, meaning that the data frame represents the total games available on the Steam games store when the data was taken.

From the evidence of the data, the Action and Adventure make more money per game than most of the other genres. MMO being the top earning games was at first a surprise until I investigated more of the costs for MMO games. They are structured where it is common for the MMO itself to charge a monthly subscription fee for a player to continue accessing the game, while the Action and Adventure games are usually a onetime price up front (except for downloadable content). While this makes the MMO games gain more money over time it also increases the price of developing such games, causing the developers to need to regularly update and maintain servers for the games to be hosted on where a single player Action game does not require as frequent updates or the server costs associated with keeping the games online.

### Future

To further this project I hope to add more data to my data-set so I can keep this up to date with the current releases of games and predict if the genre that generates the most money change if developers will release more games that fall into different genres as time goes on and the genre popularity changes.

I would also like to continue more research to add to this project aimed towards how game development in the past has reacted to mass shifts in gaming popularity and attitude of the players towards genres. 

