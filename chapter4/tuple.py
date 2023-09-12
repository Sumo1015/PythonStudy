#不可变的列表被称为元组
#元组使用圆括号来标识
#定义元组后，就可以使用索引来访问其元素，就像访问列表元素一样
#例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它们是不可修改的：
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

#严格来说，元组是由逗号标识的，若定义只包含一个元素的元组，必须在这个元素后面加上逗号
m=(3,)

#像遍历列表元素一样，也可以使用for循环来遍历元组中的所有值
dimensions=(200,50)
for dimension in dimensions:
    print(dimension)

#虽然不能修改元组的元素，但可以给存储元组的变量赋值
dimensions=(200,50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions=(400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
