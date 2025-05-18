import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_initialization():
    customer = Customer("Alice")
    coffee = Coffee("Latte")
    order = Order(customer, coffee, 5.0)

    assert order.customer == customer
    assert order.coffee == coffee
    assert order.price == 5.0
    assert isinstance(order, Order)

def test_order_price_validation():
    customer = Customer("Bob")
    coffee = Coffee("Espresso")
    
    with pytest.raises(ValueError):  # Be specific if your Order class uses ValueError
        Order(customer, coffee, -2.0)
