#使用range()方法可以生成一系列数
#在使用range()方法时，生成的数范围遵循左闭右开
for value in range(1,5):
    print(value)

#若要创建数字列表，可使用list()方法将range()的结果直接转换为列表
#将range()方法作为list()方法的参数，输出将是一个数字列表
numbers=list(range(1,6))
print(numbers)

#对数字列表执行简单的统计计算
#可使用min()、max()、sum()方法对数字列表求最小、最大、总和
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#列表解析
#列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
squares=[value**2 for value in range(1,11)]
print(squares)