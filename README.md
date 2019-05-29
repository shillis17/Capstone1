# Capstone1
## Steam Game Genre Analysis

### Description

I have chosen to research the profitability of different genres of the games on the popular gaming platform Steam. The reason that I have chosen to do this research is that lately the majority of large title games that have been released have fallen under the genres of action or adventure. This research is based on the question, are these genres more inclined to make more money than the other genres?

### Process

To begin my project I looked for a suitable data set that contains the information that I require, this information is the title of each game, genre(s), number of owners, number of players, and the cost of each game.

From this information I am able to use the sample to estimate the amount of ‘player drop-off’ or players that own the game but no longer play the game, revenue from the game based on sales and price points of the game.

The data set that I found and used for my project is called [Steam Game Data](https://data.world/craigkelly/steam-game-data) from data.world. Using this data-set I first put the data into a Pandas data-frame so that I can get familiar with my data and see if there is any data in the data-frame that is irrelevant to my project objective. During this step I found that there were many columns that are not useful for my objective. After trimming the extraneous data from my data-frame I began to graph my results.

### Visualization
	These graphs were constructed using Python’s MatPlotLib library.

The first step was to see the portions of genres that my data included to do this I constructed a bar graph and a pie chart to easily see the proportions of each genre.

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreFrequencyBar.png)
![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreFrequencyPie.png)

From these graphs we can see that the Indie genre has the most games in it, however all the games in the indie genre are also in other genres (most games have more than just one genre) and the only requirement to be in the Indie genre is the game was made by an independent game developer I made the same proportion visualization graphs without the Indie genre showing a more accurate display of the proportions of the game genres.

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreFrequencyBarNoIndie.png)
![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreFrequencyPieNoIndie.png)

From here it is easier to see that the genres Action, Adventure, and Casual contain the most games in this data-set. These simple graphs highlight the saturation of games in the Action and Adventure genres that was stated in my question.
From here I wanted to see more about the specific details in each genre. The first step was to find the costs of games in each genre. The next graph visualizes the cost of all games belonging to each genre.

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreGameCostsBar.png)

However there is very little use to the total cost of each genre as some genres contain many more games the smaller genres. The next visualization uses the mean cost for each game to account for the size gap in each of the genres to get a better understanding of the per game cost for the consumer of each genre.

![alt text](https://github.com/shillis17/Capstone1/blob/master/images/GenreGameCostsAvgBar.png)
