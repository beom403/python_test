from test_oop import Car

class Convertible(Car):
    def take_off(self):
        print("take off!!")
    def __str__(self):
        return super().__str__() + f". {self.name} with no roof"


new_car = Convertible("mini_convertible")
print(new_car)