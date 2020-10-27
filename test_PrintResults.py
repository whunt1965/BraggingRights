import HeatCheck as hc

coaches = [{"handle": "@Mickey", "score": 2, "mostpos": "I love Mickey", "mostneg": "I hate Mickey"},\
{"handle": "@Donald", "score": 0, "mostpos": "Donald is the Best", "mostneg": "I hate Donald"},\
{"handle": "@Goofy", "score": 9, "mostpos": "I love Goofy", "mostneg": "I hate Goofy"}]

def test_HC(capfd):
    resultHC = """*** Who's on the Hot Seat?! ***

    1: Donald (On the Hot Seat!)
        Score: 0
        Most Positive Tweet: Donald is the Best 
        Most Negative Tweet: I hate Donald

    2: Mickey
        Score: 2
        Most Positive Tweet: I love Mickey 
        Most Negative Tweet: I hate Mickey

    3. Goofy (Looks Safe! For now...)
        Score: 9
        Most Positive Tweet: I love Goofy 
        Most Negative Tweet: I hate Goofy

    """
    msg = "*** Who's on the Hot Seat?! ***"
    hc.printHeatCheck(msg, coaches)
    out, err = capfd.readouterr()
    assert out == resultHC

