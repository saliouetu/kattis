import pytest
from abc import *

def test_abc() :
    assert abc([1, 5, 3], "CBA") == "5 3 1"
    