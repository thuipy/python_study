from dog import Dog
# from car import Car,ElectricCar
import car as c

my_dog = Dog('willie', 6)
print(my_dog.name)

my_new_car = c.Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = c.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print(my_tesla.read_odometer.__doc__)


def add(a, b):
    """xiangjia

    good
    """
    return a + b


print(my_tesla.__init__.__doc__)
print(add.__doc__)
