class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer_reading(self, mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You can not roll back an odoment!")

    def reaad_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

#在一个模块中存储多个类
#虽然同一个模块中的类应存在某些关联性，但可根据需要在一个模块中存储任意数量的类
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        if self.battery_size == 75:
            range=260
        elif self.battery_size == 100:
            range=315
        print(f"This car go about {range} miles on a full charge.")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        #初始化父类属性，再初始化子类特有属性
        super().__init__(make,model,year)
        self.battery=Battery()

    def discribe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery.")