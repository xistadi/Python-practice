#импортирование всего подуля
from car import *
from electrical_car import ElectricCar

a4 = Car("audi", "a4", 2016)
print(a4.description_name())

tesla = ElectricCar("tesla", "model s", 2017)
tesla.battery.description_battery()