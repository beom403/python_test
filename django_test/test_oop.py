from pprint import pprint

class Car():
# method overriding
# initialize method
    def __init__(self, name: str, **kwargs) -> None:
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.name = name
        self.color = kwargs.get('color')
        self.price = kwargs.get('price')

    def __str__(self):
        return f"{self.name} with {self.wheels} wheels"

# function vs method
# method is function that belongs class
# 1st argument of method is instance itself
    def start(self):
        print("I started")
        print(self.seats)


tucson = Car(name = 'tucson', color = 'green', price = 100)
print(tucson.color, tucson.price)
print(tucson)

# dir shows everythings of argument
# pprint(dir(Car))

# components of Car class
# ['__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  'doors',
#  'seats',
#  'start',
#  'wheels',
#  'windows']