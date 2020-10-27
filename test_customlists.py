import CustomList as cl
from io import StringIO

myinput = StringIO('hello\n0\n')

def test_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', myinput)
    assert(cl.getCustomList()) == ['@hello']