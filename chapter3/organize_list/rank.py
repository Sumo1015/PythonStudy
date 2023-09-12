#sort()方法可以永久地修改列表元素的排列顺序
cars=['bmw','audi','subaru','toyota']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

#sorted()方法可以对列表进行临时排序 即要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们
cars=['bmw','audi','subaru','toyota']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))
print(sorted(cars,reverse=True))

print("\nHere is the original list again:")
print(cars)

#使用reverse方法可以倒着打印列表
cars=['bmw','audi','subaru','toyota']
print(cars)
cars.reverse()
print(cars)

#len()方法可以快速获得列表的长度
cars=['bmw','audi','subaru','toyota']
print(len(cars))