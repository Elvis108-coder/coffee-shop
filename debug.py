from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

o1 = c1.create_order(coffee1, 3.5)
o2 = c1.create_order(coffee2, 4.0)
o3 = c2.create_order(coffee1, 5.5)

print(c1.coffees())
print(coffee1.customers())
print(Coffee("Americano").average_price())
print(Customer.most_aficionado(coffee1).name)
