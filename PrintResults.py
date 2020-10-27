#Module Prints Results from each Rankings Query

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

#Print Misery Index and analysis
def PrintMiseryIndex(msg, teams):
    print(msg)
    print()
    i = 1
    for team in teams:
        if i == 1:
            print("{}: {} (Most Miserable!)".format(i, team["handle"]))
        elif i == len(teams):
            print("{}: {} (Least Miserable! For now...)".format(i, team["handle"]))
        else:
            print("{}: {}".format(i, team["handle"]))
        print("     Score: {}".format(team["score"]))
        print("     Most Positive Tweet: {}".format(team["mostpos"].replace("\n", " ")))
        print("     Most Negative Tweet: {}".format(team["mostneg"].replace("\n", " ")))
        i += 1
        print()


    #Print Custom Ranking and analysis
def PrintCustomRank(handles):
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