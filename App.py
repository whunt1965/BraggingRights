#Main module. Used to record user input and run correct ranking program

import init_api as ia
import HeatCheck as HC
import MiseryIndex as MI
import CustomList as CL
import CustomRank as CR

api, client = ia.init_api() #init Tweepy API and Google NLP client

print("Welcome to BraggingRights!")
modulechoice = 0 #module selection indicator

#Prompt user for input and choose correct program
while True:
    choice1 = input("Do you want to run a MiseryIndex (1), Hot Seat Check (2), or Custom Ranking (3)")
    if choice1 == "1":
        modulechoice = 1
        print("You chose Misery Index!")
        break
    elif choice1 == "2":
        modulechoice = 2
        print("You chose Hot Seat Check!")
        break
    elif choice1 == "3":
        modulechoice = 3
        print("You chose Custom Ranking!")
        break
    else:
        print("Invalid Input! Please try again")

if modulechoice == 1: #Misery Index
    while True:
        choice2 = input("Do you want to run a MiseryIndex on the SEC Football teams (1) or a custom list (2)?")
        if choice2 == "1":
            MI.MiseryIndex(api=api, client=client, tweetnumber=10)
            break
        elif choice2 == "2":
            customlist = CL.getCustomList()
            MI.MiseryIndex(api=api, client=client, tweetnumber=10, customlist=customlist)
            break
        else:
            print("Invalid Input! Please try again")
elif modulechoice ==2: #Hot seat check
    while True:
        choice2 = input("Do you want to run a Hot Seat Check on SEC Football coaches (1) or a custom list (2)?")
        if choice2 == "1":
            HC.HeatCheck(api=api, client=client, tweetnumber=10)
            break
        elif choice2 == "2":
            customlist = CL.getCustomList()
            HC.HeatCheck(api=api, client=client, tweetnumber=10, customlist=customlist)
            break
        else:
            print("Invalid Input! Please try again")    
else: #Custom Rank
    customlist = CL.getCustomList()
    CR.CustomRanker(api=api, client=client, tweetnumber=10, customlist=customlist)


