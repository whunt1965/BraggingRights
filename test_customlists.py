import CustomList as cl
from io import StringIO

myinput = StringIO('hello', '0')

def test_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', myinput)
    assert(cl.getCustomList()) == ['@hello']