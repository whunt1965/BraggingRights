# BraggingRights
BraggingRights is an application leveraging the capabilities of the Tweepy Twitter API library and the Google NLP API to allow users to produce ranked lists of Twitter handles by retrieving real tweets tagging these handles and running sentiment analysis on the tweets. Users can select a set of pre-defined programs/lists of Twitter handles or run their own custom searches. The application then produces a ranked list of the queried handles (with scores assigned based on sentiment analysis and magnitude) as well as the most positive and most negative tweets for each handle.

## Overview
Although it may only be played in the fall, for real fans, college football is a year-round topic of conversation. So why should bragging rights be limited to just during the season? And moreover, shouldn’t we be able to brag not only about how our team is performing on the field, but also about the strength of our fanbase and the support of our coaches?

BraggingRights provides a mean to settle the important questions which pervade the incessant debates of college football fans. Which fanbase supports their team the most? Which coach is on the hot seat? Using the unmatched reach of Twitter and the power sentiment analysis tools of the Google Natural Language Process API, Bragging Rights gives you the real-time insight you need to prove just how strong your team’s program really is.

But what if you’re not into college football? We get it. BraggingRights also lets users retrieve custom Rankings by taking in a list of user-supplied Twiter handles and producing a definitive ranking of the results (from most positive to least) based on the sentiment of the tweets tagging this handle. Whatever the motivations behind your ranking, BraggingRights has your answers.

## Application Features and Capabilities

## Description of Modules
* **App.py** – The main method of the application. Selects the correct program to run based on user input.

*	**Init_api.py** – A module which initializes and returns a Twitter (though Tweepy) API object and a Google NLP client object utilized by other parts of the program to fetch data and perform sentiment analysis. This module handles all the necessary authorizations for using these API’s.

*	**CustomList.py** – This module allows a user to input a custom list of search terms and returns a list that can be used by the MiseryIndex.py, HeatCheck.py, or CustomRank.py modules. 

*	**MiseryIndex.py** – This module supports the MiseryIndex feature of the app (which allows users to either simply select the built-in list of SEC football teams or enter their own custom list). The MiseryIndex module handles the appropriate function calls (to AppEngine.py) and prints the ranked results (from most miserable (negative) to least miserable (positive)) along with most positive and negative tweets for each handle. Due to access constraints, only 10 tweets for each handle are fetched for this query (though this can easily be modified in App.py).

*	**HeatCheck.py** – This module supports the Hot Seat Check feature of the app (which allows users to either simply select the built-in list of SEC football coaches or enter their own custom list). The HeatCheck module handles the appropriate function calls (to AppEngine.py) and prints the ranked results (from “On the Hot Seat” (most negative) to “Safe” (most positive)) along with most positive and negative tweets for each handle. Due to access constraints, only 10 tweets for each handle are fetched for this query (though this can easily be modified in App.py).

* **CustomRank.py** – This module handles the appropriate function calls (to AppEngine.py) and prints the ranked results (from most positive to most negative) along with most positive and negative tweets for each result based on a user-defined list of Twitter handles to search. Due to access constraints, only 10 tweets for each handle are fetched for this query (though this can easily be modified in App.py).

* **AppEngine.py** – This module provides a common processing unit for the various programs (MiseryIndex, Hot Seat Check, Custom Ranking) which handles:
  * Creating a dictionaries for each handle (allowing a score, most positive tweet, and most negative tweet to be associated with each handle) and placing these into a list of dictionaries
  * Calling the calc_score() function on each handle in the list of dictionaries. This function fetches 10 tweets (though this number can be changed in app.py) for each handle, performs sentiment analysis on each one, and returns the overall sentiment score (the sum of (sentiment score *sentiment magnitude) for each tweet), the most positive tweet, and the most negative tweet. 
  * Sorts the list of dictionaries in ascending order by score (from most negative to most positive) and returns this list to the calling module (MiseryIndex.py, HeatCheck.py, or CustomRank.py). 

## Use Cases

## How to Run

## Acknowledgements
