class Dog:
    #前面一个下划线的方法是 protect方法
    #前面两个下划线是private方法/属性
    #前后各两个下划线代表是特殊方法
    #特殊方法__len__() __init__() __item__()(重载了索引运算符) __str__() __call__()(重载函数对象)
    #函数装饰器

    #类中的函数称为方法
    #_init()是一个特殊方法，每当你使用定义的类创建一个实例后都会自动地调用这个方法
    #以self为前缀的变量可供类中的所有方法使用，可以通过类的任何实例来访问
    def __init__(self,name,age):
        self.name=name
        self.age=age
        #创建实例时，有些属性无需通过形参来定义，可在方法__init__()中为其指定默认值
        self.default=0
    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

    def update_age(self,age):
        self.age=age

my_dog=Dog('Willie',6)
#要访问实例的属性，可使用句点表示法
#要调用方法，可指定实例的名称和要调用的方法，并用句点分隔
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
#修改属性时可以通过实例访问属性直接修改，也可以通过调用方法修改
my_dog.age=10
print(f"My dog is {my_dog.age} years old.")
my_dog.update_age(12)
print(f"My dog is {my_dog.age} years old.")


