# Simple module to see which coach is on the hot seat! 

import AppEngine as AE
import tweepy

#Retrieves SEC coaches from my Custom Twitter List
def getCoaches(api):
    coachlist = []
    listmems = api.list_members(list_id = 1309497099856343040) #id for my Custom SEC Coach list
    for user in listmems:
        coachlist.append("@" + str(user.screen_name))
    return coachlist

def HeatCheck(api, client, customlist = None, tweetnumber = 10):
    #number of tweets fetched per coach
    tweetnumber = 10

    #default message
    msg = "*** Who's on the Hot Seat?! ***"

    #Message to user. Processing takes a minute
    print("Processing data. This could take a moment...")
    print()

    #If user didn't choose custom list, fetch SEC coach list
    if not customlist:
        customlist = getCoaches(api)
        msg = "*** Who's on the Hot Seat in the SEC?! "
    
    #Retrieve sorted list of coaches (with ranking and scores)
    coaches = AE.getResults(api=api, client=client, userlist=customlist, tweetnumber=tweetnumber)
    printHeatCheck(msg, coaches)

#Print Heat Check and analysis
def printHeatCheck(msg, coaches):
    print(msg)
    print()
    i = 1
    for coach in coaches:
        if i == 1:
            print("{}: {} (On the Hot Seat!)".format(i, coach["handle"]))
        elif i == len(coaches):
            print("{}: {} (Looks Safe! For now...)".format(i, coach["handle"]))
        else:
            print("{}: {}".format(i, coach["handle"]))
        print("     Score: {}".format(coach["score"]))
        print("     Most Positive Tweet: {}".format(coach["mostpos"].replace("\n", " ")))
        print("     Most Negative Tweet: {}".format(coach["mostneg"].replace("\n", " ")))
        i += 1
        print()


