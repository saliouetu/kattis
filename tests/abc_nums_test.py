import pytest
from abc_nums import *

def test_abc_nums() :
    assert abc([1, 5, 3], "CBA") == "5 3 1"
    