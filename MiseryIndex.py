# Simple test POC to see which team is the most miserable!

import AppEngine as AE
import PrintResults as PR
import tweepy

#Retrieves SEC coaches from my Custom Twitter List
def getTeams(api):
    teamlist = []
    listmems = api.list_members(list_id = 1310690360302206976) #id for my Custom SEC Team list
    for user in listmems:
        teamlist.append("@" + str(user.screen_name))
    return teamlist

def MiseryIndex(api, client, customlist = None, tweetnumber = 10):
    #number of tweets fetched per team
    tweetnumber = tweetnumber

    #default message
    msg = "*** Misery Index!! ***"

    #Message to user. Processing takes a minute
    print("Processing data. This could take a moment...")
    print()

    #If user didn't choose custom list, fetch SEC team list
    if not customlist:
        customlist = getTeams(api)
        msg = "*** Who's the most miserable fanbase in the SEC?! "
    
    #Retrieve sorted list of teams (with ranking and scores)
    teams = AE.getResults(api=api, client=client, userlist=customlist, tweetnumber=tweetnumber)

    PR.PrintMiseryIndex(msg, teams) #Print results



