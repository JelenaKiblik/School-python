"""Test for "Find the shortest way back in a taxicab geometry"."""


import pytest
import shortest_way_back
import random
def test_shortest_way_back():
    """First test."""
    pass


def empty_path():
    """Test empty path."""
    assert shortest_way_back("") == ""


def lower_case_correct():
    """Test lower case"""
    assert shortest_way_back("sss") == False
