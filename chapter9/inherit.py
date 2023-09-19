class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def update_odometer_reading(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can not roll back an odoment!")

    def reaad_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles


#将实例用作属性
#在实际代码模拟实物时，由于类的细节很多，属性和方法清单以及文件都越来越长
#在这种情况下，可将这些属性和方法提取出来，作为一个独立的类，可以将大型类拆分成多个协同工作的小类
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


my_tesla=ElectricCar('tesla','model s',2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
