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