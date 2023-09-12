#一个简单例子
#每条if语句的核心都是一个值为true或false的表达式，这种表达式称为条件测试
#Python根据条件测试的值为true或false来决定是否执行if语句中的代码
#在Python中检查是否相等时区分大小写
#在Python的条件表达式中使用and和or检查多个条件 表示且和或
cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())

#要判断特定的值是否包含在列表中 可使用关键字in
requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

#要判断特定值不包含在列表中，可使用关键字not in
banned_users=['andrew','carolina','david']
user='marie'

if user not in banned_users:
    print(f"{user.title()},you can post a response if you wish.")

#布尔表达式
#布尔表达式其实是条件测试的别名，与条件表达式一样，布尔表达式的结果要么是true，要么是false
#布尔值通常用于记录题哦啊见

#if-elif-else结构
age=12
if age<4:
    print("Your admission cost is $0.")
elif age<18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

#用if语句判断列表是否为空 若列表不为空 则执行if语句后面的代码
