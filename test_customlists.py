import CustomList as cl
from io import StringIO

myinput = StringIO('hello')

def test_input(monkeypatch):
    assert(cl.getCustomList()) == ['@hello']