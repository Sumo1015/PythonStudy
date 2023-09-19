#使用关键字def定义函数
def greet_user1():
    print("Hello!")

def greet_user2(username):#username为形参(parameter)
    print(f"Hello,{username}")

greet_user1()
greet_user2("jessie")#"jessie"为实参(argument)

#关键字实参
#关键字实参是传递给函数的名称值对，即直接在实参中将名称和值关联起来
#使用关键字实参时，务必准确指定函数定义中的形参名
def describe_pet1(animal_type,pet_name):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet1(animal_type='hamster',pet_name='harry')

#默认值
#编写函数时，可给每个形参指定默认值，在调用函数中给形参提供了实参时，Python将使用指定的实参值，否则，将使用形参的默认值
#在形参指定默认值后，可在函数调用中省略相应的实参
def describe_pet2(pet_name,animal_type='dog'):
    print(f"I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name}")
describe_pet2(pet_name='willie')

#在函数中，可使用return语句将值返回到调用函数的代码行
def get_formatted_name1(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
musician=get_formatted_name1('jimi','hendrix')
print(musician)

#可选实参
#有时，需要将实参变为可选的，这样使用函数的人就能只在必要时提供额外信息，可使用默认值来让实参变为可选的
#可给形参指定一个空的默认值，并在用户没有提供实参值时不使用这个实参
def get_formatted_name2(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
        return full_name.title()
    else:
        full_name=f"{first_name} {last_name}"
        return full_name.title()
musician1=get_formatted_name2('john','hooker','lee')
musician2=get_formatted_name2('jimi','hendrix')
print(musician1)
print(musician2)

#返回字典
#None表示变量没有值，可将None视为占位值。在条件测试中，None相当于False
def build_person(first_name,last_name,age=None):
    if age:
        person={'first':first_name,'last':last_name,'age':age}
        return person

    else:
        person = {'first': first_name, 'last': last_name}
        return person
musician1=build_person('jimi','hendrix')
musician2=build_person('jimi','hendrix',27)
print(musician1)
print(musician2)

#传递列表
#将列表传递给函数后，函数就能直接访问其内容
#若需要在函数中对原始列表进行修改，可以直接将原始列表作为实参传递进函数中
#若想要保留原始列表的内容，可以将列表的副本传递进函数中 用”列表名[:]“表示原始列表的副本
def f(list):
    for l in list:
        print(l)
        list.remove(l)

list=[1,2,3,4,5]
f(list[:])
print(list)

#传递任意数量的实参
#有时候，预先不知道需要接受多少个实参，Python允许函数从调用语句中收集任意数量的实参
#"*形参名"中的星号让Python创建一个空元组，并将收到的所有值都封装到这个元组中
def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')

#结合使用位置实参和任意数量实参
#如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后

#使用任意数量的关键字实参
#使用双星号创建空字典，并将收到的所有名称值对都放到这个字典中
#在这个函数中，可以访问这个字典中的名称值对
#在这个函数中，不管额外提供多少个键值对，它都能正确地处理

def build_profile(first,last,**userinfo):
    userinfo['first_name']=first
    userinfo['last_name']=last
    return userinfo
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

