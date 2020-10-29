# BraggingRights
BraggingRights is an application leveraging the capabilities of the Tweepy Twitter API library and the Google NLP API to allow users to produce ranked lists of Twitter handles by retrieving real tweets tagging these handles and running sentiment analysis on the tweets. Users can select a set of pre-defined programs/lists of Twitter handles or run their own custom searches. The application then produces a ranked list of the queried handles (with scores assigned based on sentiment analysis) as well as the most positive and most negative tweets for each handle.

## Overview
Although it may only be played in the fall, for real fans, college football is a year-round topic of conversation. So why should bragging rights be limited to just during the season? And moreover, shouldn’t we be able to brag not only about how our team is performing on the field, but also about the strength of our fanbase and the support of our coaches?

BraggingRights provides a mean to settle the important questions which pervade the incessant debates of college football fans. Which fanbase supports their team the most? Which coach is on the hot seat? Using the unmatched reach of Twitter and the power sentiment analysis tools of the Google Natural Language Process API, Bragging Rights gives you the real-time insight you need to prove just how strong your team’s program really is.

But what if you’re not into college football? We get it. BraggingRights also lets users retrieve custom Rankings by taking in a list of user-supplied Twiter handles and producing a definitive ranking of the results (from most positive to least) based on the sentiment of the tweets tagging this handle. Whatever the motivations behind your ranking, BraggingRights has your answers.

## Application Features and Capabilities
* **Misery Index** – The tide of fanbase sentiment rises and falls week to week (or even day to day) as teams win or lose, programs undergo shake-ups, and players come and go. But is your fanbase more miserable than your rival's? Misery Index aggregates tweets tagging a team's official handle and provides an overall ranking of sentiment (ranging from most miserable to most positive) using scores derived from Google's sentiment analysis tool. The ranking provides the most positive and least positive tweets for each team handle, so you can see what others are saying. Users can select the pre-defined list of SEC teams or enter their own list of team handles. 

*	**Hot Seat Check** – Which coach is on the hot seat? Hot Seat. Check collects and performs sentiment analysis on tweets tagging a team's coach provides a ranking ranging from "On the Hot Seat" to "Safe. For now..." as well as the most and least positive tweets tagging that coach. Users leverahe the pre-defined list of SEC coaches or enter their own custom list of twitter handles. 

*	**Custom Rank** – Custom rank gives users the flexibility to create their own custom searches. Users simply input the Twitter handles they want to rank and get a ranked list of these handles (based on sentiment scores) along with the most positive and most negative tweets tagging this handle.

## Description of Modules
* **App.py** – The main method of the application. Selects the correct program (Misery Index, Hot Seat Check, or Custom Rank) to run based on user input.

*	**Init_api.py** – A module which initializes and returns a Twitter (though Tweepy) API object and a Google NLP client object utilized by other parts of the program to fetch data and perform sentiment analysis. This module handles all the necessary authorizations for using these API’s.

*	**config.py** – A module which allows a user to define their Twitter API keys to use throughout the program.

*	**CustomList.py** – This module allows a user to input a custom list of search terms and returns a list that can be used by the MiseryIndex.py, HeatCheck.py, or CustomRank.py modules. 

*	**MiseryIndex.py** – This module supports the MiseryIndex feature of the app (which allows users to either simply select the built-in list of SEC football teams or enter their own custom list). The MiseryIndex module handles the appropriate function calls (to AppEngine.py) and calls its print method (in PrintResults.py) to print the ranked results (from most miserable (negative) to least miserable (positive)) along with most positive and negative tweets for each handle. Due to access constraints, only 10 tweets for each handle are fetched for this query (though this can easily be modified in App.py).

*	**HeatCheck.py** – This module supports the Hot Seat Check feature of the app (which allows users to either simply select the built-in list of SEC football coaches or enter their own custom list). The HeatCheck module handles the appropriate function calls (to AppEngine.py) and calls its print method (in PrintResults.py) to print the ranked results (from “On the Hot Seat” (most negative) to “Safe” (most positive)) along with most positive and negative tweets for each handle. Due to access constraints, only 10 tweets for each handle are fetched for this query (though this can easily be modified in App.py).

* **CustomRank.py** – This module handles the appropriate function calls (to AppEngine.py) and calls its print method (in PrintResults.py) to print the ranked results (from most positive to most negative) along with most positive and negative tweets for each result based on a user-defined list of Twitter handles to search. Due to access constraints, only 10 tweets for each handle are fetched for this query (though this can easily be modified in App.py).

* **PrintResults.py** - This module handles the output for the application by parsing and printing the results from a "Misery Index," "Hot Seat Check," or "Custom Rank."

* **AppEngine.py** – This module provides a common processing unit for the various programs (MiseryIndex, Hot Seat Check, Custom Ranking) which handles:
  * Creating a dictionaries for each handle (allowing a score, most positive tweet, and most negative tweet to be associated with each handle) and placing these into a list of dictionaries
  * Calling the calc_score() function on each handle in the list of dictionaries. This function fetches 10 tweets (though this number can be changed in app.py) for each handle, performs sentiment analysis on each one, and returns the overall sentiment score (the sum of (sentiment_score x sentiment_magnitude) for each tweet), the most positive tweet, and the most negative tweet. 
  * Sorts the list of dictionaries in ascending order by score (from most negative to most positive) and returns this list to the calling module (MiseryIndex.py, HeatCheck.py, or CustomRank.py). 

## Use Cases
**College Football Fans**

As a college football fan, I know my fanbase is stronger that our conference rival’s fanbase. With Bragging Rights, I can prove it! By simply running a query on my football conference of interest, I get a definitive ranking of how supportive my fanbase is on Twitter compared to all other teams in my conference. I can also get an analysis of which coaches are on the “hot seat” and use that to further bolster my argument.

What if I want to compare teams from outside my conference? Simple. I simply choose the “custom” mode, enter the handles of all the teams I want to compare, and wait for the results to roll in!

**College Football Recruits**

Today’s college football recruits have access to more information about potential schools than ever before. But how do they make the right choice? Sure, win/loss records and on-campus visits can give the recruit an understanding of a team’s potential and the facilities they can access, but what about the fanbase? Are they passionate? Supportive? Down-right mean? And what about the coach? If I commit now, will he/she still have a job next year?

BraggingRights provides an answer to these important questions. A recruit can look at an all teams or coaches in an entire conference or choose the “custom” option to filter the search to a few top teams or coaches. 

**Sports Writers**

Everyone loves a good team/coach “ranking” article and BraggingRights makes it easy. A journalists can simply input the handles of the teams/coaches they wish to analyze, get the results, and use them to create an interesting article that fanbases can devour. Moreover, since BraggingRights provides the most positive/negative tweets associated with each handle, a journalist has easy access to real tweets they can simply find on Twitter and include directly in their article.

**Anyone Looking for Bragging Rights…**

Anyone looking to rank companies, people, or products (essentially, any entity with a Twitter handle) can use BraggingRights’ Custom Ranking feature to quickly get a ranking based on tweet sentiment about that handle. Users can simply choose the “Custom Ranking” option, input the list of handles they wish to search, and have a ranked list (along with most positive and negative tweets) delivered back to them.


## Set Up and Running the Program
### Install Python3 
This program executes Python scripts, and therefore users will need Python3 to run it. Information for installing Python3 can be found [here](https://www.python.org/downloads/)
### Get Access to the Google NLP API
A [Google Cloud Platform](https://cloud.google.com) account is required to use the Google NLP API. Users should be sure to carefully follow the steps for setting up authorization prior to attempting to utilize this program. 
### Get Access to the Twitter API and Install Tweepy
A [Twitter Developer](https://developer.twitter.com/) account is required to use the Twitter API. In addition, users will need to follow the instructions to install Tweepy (available on the [Tweepy GitHub Repository](https://github.com/tweepy/tweepy)). To utilize the programs in this repository, users will need to add their own Twitter credentials (consumer key/secret and access key/secret) in the text blocks indicated in the config.py file.
### Clone the Repo and Run BraggingRights
Clone the repo to your local machine by clicking on the *code* button in the repo and follow the instructions from GitHub. Be sure to add your Twitter credentials to the config.py file!
### Run the Program
After following the set-up steps above, navigate to the directory on your machine which contains the cloned repo and run the program on the command line by entering *python3 app.py*

## Acknowledgements
This program was made possible through a number of open-source and class-provided resources, including:
* https://drive.google.com/file/d/1dNahyZnwgqwUUdbV5I0u68b8pQADBiWi/view  - An example document provided by Professor Osama Alshaykh and used as a reference to get started using the Twitter API.
* https://cloud.google.com/natural-language/docs/reference/libraries  - Used to learn how to use the Google NLP API
* http://docs.tweepy.org/en/latest/ - Used for reference for various Tweepy API functions 
* https://stackoverflow.com/questions/38872195/tweepy-exclude-retweets/38976513 - Used to learn how to filter retweets out of Twitter searches
* https://stackoverflow.com/questions/62152814/twitter-list-id - Used as a reference for retrieving custom Twitter Lists through the Twitter API



