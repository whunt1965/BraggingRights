import PrintResults as PR

results = [{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"},\
{"handle": "@Mickey", "score": 2, "mostpos": "I love Mickey", "mostneg": "I hate Mickey"},\
{"handle": "@Goofy", "score": 9, "mostpos": "I love Goofy", "mostneg": "I hate Goofy"}]

def test_HC(capfd):
    resultHC = """*** Who's on the Hot Seat?! ***

1: @Donald (On the Hot Seat!)
     Score: 0
     Most Positive Tweet: Donald is the Best
     Most Negative Tweet: I hate Donald

2: @Mickey
     Score: 2
     Most Positive Tweet: I love Mickey
     Most Negative Tweet: I hate Mickey

3: @Goofy (Looks Safe! For now...)
     Score: 9
     Most Positive Tweet: I love Goofy
     Most Negative Tweet: I hate Goofy

"""
    msg = "*** Who's on the Hot Seat?! ***"
    PR.printHeatCheck(msg, results)
    out, err = capfd.readouterr()
    assert out == resultHC

def testMI(capfd):

    resultMI = """*** Misery Index!! ***

1: @Donald (Most Miserable!)
     Score: 0
     Most Positive Tweet: Donald is the Best
     Most Negative Tweet: I hate Donald

2: @Mickey
     Score: 2
     Most Positive Tweet: I love Mickey
     Most Negative Tweet: I hate Mickey

3: @Goofy (Least Miserable! For now...)
     Score: 9
     Most Positive Tweet: I love Goofy
     Most Negative Tweet: I hate Goofy

"""
    msg = "*** Misery Index!! ***"
    PR.PrintMiseryIndex(msg, results)
    out, err = capfd.readouterr()
    assert out == resultMI


newresults = [{"handle": "@Goofy", "score": 9, "mostpos": "I love Goofy", "mostneg": "I hate Goofy"},\
{"handle": "@Mickey", "score": 2, "mostpos": "I love Mickey", "mostneg": "I hate Mickey"},\
{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"},]

def testCR(capfd):
    resultCR = """Your Ranking Results! (Most Positive to Least Positive)

1: @Goofy (Most Positive!)
     Score: 9
     Most Positive Tweet: I love Goofy
     Most Negative Tweet: I hate Goofy

2: @Mickey
     Score: 2
     Most Positive Tweet: I love Mickey
     Most Negative Tweet: I hate Mickey

3: @Donald (Most Negative!)
     Score: 0
     Most Positive Tweet: Donald is the Best
     Most Negative Tweet: I hate Donald

"""

    PR.PrintCustomRank(newresults)
    out, err = capfd.readouterr()
    assert out == resultCR