#Module provides a mechanism to rank custom searches and outputs results
import AppEngine as AE
import PrintResults as PR

def CustomRanker(api, client, customlist, tweetnumber=10):

    #Message to user. Processing takes a minute
    print("Processing data. This could take a moment...")
    print()

    #Retrieve sorted list of handles (with ranking and scores)
    handles = AE.getResults(api=api, client=client, userlist=customlist, tweetnumber=tweetnumber)

    #Reverse Order to get Most positive to least positive
    handles.reverse()

    #Print Results
    PR.PrintCustomRank(handles)
