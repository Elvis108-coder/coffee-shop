import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import pytest
from coffee import Coffee

def test_coffee_name():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_setter_validation():
    coffee = Coffee("Espresso")
    with pytest.raises(Exception):
        coffee.name = ""
