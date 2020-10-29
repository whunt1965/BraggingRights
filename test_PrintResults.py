import PrintResults as PR


#Heat Check Tests****

HCresults1 = [{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"},\
{"handle": "@Mickey", "score": 2, "mostpos": "I love Mickey", "mostneg": "I hate Mickey"},\
{"handle": "@Goofy", "score": 9, "mostpos": "I love Goofy", "mostneg": "I hate Goofy"}]

def test_HC1(capfd):
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
    PR.printHeatCheck(msg, HCresults1)
    out, err = capfd.readouterr()
    assert out == resultHC


HCresults2 = [{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"}]

def test_HC2(capfd):
    resultHC = """*** Who's on the Hot Seat?! ***

1: @Donald (On the Hot Seat!)
     Score: 0
     Most Positive Tweet: Donald is the Best
     Most Negative Tweet: I hate Donald

"""
    msg = "*** Who's on the Hot Seat?! ***"
    PR.printHeatCheck(msg, HCresults2)
    out, err = capfd.readouterr()
    assert out == resultHC

HCresults3 = [{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"},\
{"handle": "@Mickey", "score": 2, "mostpos": "I love Mickey", "mostneg": "I hate Mickey"}]

def test_HC3(capfd):
    resultHC = """*** Who's on the Hot Seat?! ***

1: @Donald (On the Hot Seat!)
     Score: 0
     Most Positive Tweet: Donald is the Best
     Most Negative Tweet: I hate Donald

2: @Mickey (Looks Safe! For now...)
     Score: 2
     Most Positive Tweet: I love Mickey
     Most Negative Tweet: I hate Mickey

"""
    msg = "*** Who's on the Hot Seat?! ***"
    PR.printHeatCheck(msg, HCresults3)
    out, err = capfd.readouterr()
    assert out == resultHC


# Misery Index Tests****

MIresults1 = [{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"},\
{"handle": "@Mickey", "score": 2, "mostpos": "I love Mickey", "mostneg": "I hate Mickey"},\
{"handle": "@Goofy", "score": 9, "mostpos": "I love Goofy", "mostneg": "I hate Goofy"}]

def testMI1(capfd):

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
    PR.PrintMiseryIndex(msg, MIresults1)
    out, err = capfd.readouterr()
    assert out == resultMI


MIresults2 = [{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"}]

def testMI2(capfd):

    resultMI = """*** Misery Index!! ***

1: @Donald (Most Miserable!)
     Score: 0
     Most Positive Tweet: Donald is the Best
     Most Negative Tweet: I hate Donald

"""
    msg = "*** Misery Index!! ***"
    PR.PrintMiseryIndex(msg, MIresults2)
    out, err = capfd.readouterr()
    assert out == resultMI


MIresults3 = [{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"},\
{"handle": "@Mickey", "score": 2, "mostpos": "I love Mickey", "mostneg": "I hate Mickey"}]

def testMI3(capfd):

    resultMI = """*** Misery Index!! ***

1: @Donald (Most Miserable!)
     Score: 0
     Most Positive Tweet: Donald is the Best
     Most Negative Tweet: I hate Donald

2: @Mickey (Least Miserable! For now...)
     Score: 2
     Most Positive Tweet: I love Mickey
     Most Negative Tweet: I hate Mickey

"""
    msg = "*** Misery Index!! ***"
    PR.PrintMiseryIndex(msg, MIresults3)
    out, err = capfd.readouterr()
    assert out == resultMI



# Custom Rank Tests****

CRresults1 = [{"handle": "@Goofy", "score": 9, "mostpos": "I love Goofy", "mostneg": "I hate Goofy"},\
{"handle": "@Mickey", "score": 2, "mostpos": "I love Mickey", "mostneg": "I hate Mickey"},\
{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"},]

def testCR1(capfd):
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

    PR.PrintCustomRank(CRresults1)
    out, err = capfd.readouterr()
    assert out == resultCR


CRresults2 = [{"handle": "@Goofy", "score": 9, "mostpos": "I love Goofy", "mostneg": "I hate Goofy"}]

def testCR2(capfd):
    resultCR = """Your Ranking Results! (Most Positive to Least Positive)

1: @Goofy (Most Positive!)
     Score: 9
     Most Positive Tweet: I love Goofy
     Most Negative Tweet: I hate Goofy

"""

    PR.PrintCustomRank(CRresults2)
    out, err = capfd.readouterr()
    assert out == resultCR


CRresults3 = [{"handle": "@Goofy", "score": 9, "mostpos": "I love Goofy", "mostneg": "I hate Goofy"},\
{"handle": "@Mickey", "score": 2, "mostpos": "I love Mickey", "mostneg": "I hate Mickey"}]

def testCR3(capfd):
    resultCR = """Your Ranking Results! (Most Positive to Least Positive)

1: @Goofy (Most Positive!)
     Score: 9
     Most Positive Tweet: I love Goofy
     Most Negative Tweet: I hate Goofy

2: @Mickey (Most Negative!)
     Score: 2
     Most Positive Tweet: I love Mickey
     Most Negative Tweet: I hate Mickey

"""

    PR.PrintCustomRank(CRresults3)
    out, err = capfd.readouterr()
    assert out == resultCR