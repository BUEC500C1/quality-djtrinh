import pytest

def pass_string(s):
    return s

def test_pass():
    assert pass_string("s") == "s"
