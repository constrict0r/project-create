# Sample Test passing with pytest

from amanita import amanita

def test_enjoy(capfd):

    amanita.enjoy()
    out, err = capfd.readouterr()
    assert "___.....___" in out
