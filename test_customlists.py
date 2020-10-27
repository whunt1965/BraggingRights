import CustomList as cl
import StringIO

myinput = StringIO('hello')

def test_input(monkeypatch):
    assert(cl.getCustomList()) == ['@hello']