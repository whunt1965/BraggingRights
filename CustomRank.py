#Module provides a mechanism to rank custom searches and outputs results
import AppEngine as AE

def CustomRanker(api, client, customlist, tweetnumber=10):

    #Message to user. Processing takes a minute
    print("Processing data. This could take a moment...")
    print()

    #Retrieve sorted list of handles (with ranking and scores)
    handles = AE.getResults(api=api, client=client, userlist=customlist, tweetnumber=tweetnumber)

    #Reverse Order to get Most positive to least positive
    handles.reverse()

    #Print Ranking and analysis
    print("Your Ranking Results! (Most Positive to Least Positive)")
    print()
    i = 1
    for handle in handles:
        if i == 1:
            print("{}: {} (Most Positive!)".format(i, handle["handle"]))
        elif i == len(handles):
            print("{}: {} (Most Negative!)".format(i, handle["handle"]))
        else:
            print("{}: {}".format(i, handle["handle"]))
        print("     Score: {}".format(handle["score"]))
        print("     Most Positive Tweet: {}".format(handle["mostpos"].replace("\n", " ")))
        print("     Most Negative Tweet: {}".format(handle["mostneg"].replace("\n", " ")))
        i += 1
        print()
