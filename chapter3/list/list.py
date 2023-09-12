bicycles=['trek','cannondale','redline','specialized']
print(bicycles)

#访问列表元素 通过索引访问 索引从0开始
print(bicycles[0].title())
#通过将索引指定为-1 可让Python返回最后一个列表元素
print(bicycles[-1])

#修改列表元素时，通过指定列表名和要修改的元素的索引 再指定该元素的新值
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0]='ducati'
print(motorcycles)

#在列表中添加元素
#使用append()方法在列表末尾添加元素
motorcycles=[]
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#在列表中插入元素
#使用insert()方法可以在列表中任意位置插入元素 需要指定新元素的索引和值
motorcycles=['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

#从列表中删除元素
#使用del语句删除元素 知道元素在列表中的位置
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
#使用pop()方法删除元素
#pop()方法删除列表的末尾元素 并使我们能接着使用它
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycle=motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#弹出列表中任何位置的元素 通过在pop()方法中指出要弹出元素的索引来弹出任意位置的元素
motorcycles=['honda','yamaha','suzuki']
first_owned=motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}")

#根据值删除元素 使用remove()方法
#可以将待删除值赋值给变量，将变量置于remove()方法中来删除列表中对应值的元素，接着可以再通过变量访问该元素
#remove()方法每次调用只删除一个指定值的元素，若列表中有多个值相同的待删除元素，则需通过循环判断来确保删除每个值
motorcycles=['honda','yamaha','suzuki','ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)