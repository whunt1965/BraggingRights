import CustomList as cl
from io import StringIO

myinput0 = StringIO('0\n')
myinput1 = StringIO('hello\n0\n')
myinputmany = StringIO('Obama\nBush1\nBush2\nClinton\n0\n')

def test_input0(monkeypatch):
    monkeypatch.setattr('sys.stdin', myinput0)
    assert(cl.getCustomList()) == []

def test_input1(monkeypatch):
    monkeypatch.setattr('sys.stdin', myinput1)
    assert(cl.getCustomList()) == ['@hello']


def test_inputmany(monkeypatch):
    monkeypatch.setattr('sys.stdin', myinputmany)
    assert(cl.getCustomList()) == ['@Obama', '@Bush1','@Bush2','@Clinton']