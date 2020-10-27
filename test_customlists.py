import CustomList as cl
from io import StringIO

myinput = StringIO('hello')

def test_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', myinput)
    monkeypatch.setattr('sys.stdin', 0)
    assert(cl.getCustomList()) == ['@hello']