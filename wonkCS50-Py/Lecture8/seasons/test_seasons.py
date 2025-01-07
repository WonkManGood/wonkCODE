from seasons import inflect
import pytest

def test_inflect():
    assert inflect('1999-09-09') == 'Thirteen million, two hundred seventy-three thousand, nine hundred twenty minutes'
    with pytest.raises(SystemExit):
        inflect('1999-9-9')
