#在Python中，字典用放在花括号{}中的一系列键值对表示
#字典中可包含任意数量的键值对
alien_0={'color':'green','points':5}
#当访问字典中与键先滚脸的值时，可一次指定字典名和放在方括号内的键
print(alien_0['color'])
#然而，使用方括号和键的形式获取相关联的值时，若键不存在，Python会显示traceback 指出存在键值错误
#使用get()方法则可以有效避免这一问题
#使用get()方法时，其第一个参数用来指定键，必不可少
#使用get()方法时，第二个参数可选，用来指定当键不存在时返回的值
alien_0={'color':'green','points':5}
speed_value=alien_0.get('speed','No speed value assigned!')
print(speed_value)

#要在字典中添加键值对，可一次指定字典名、用放括号括起来的键和相关联的值
alien_0={'color':'green','points':5}
print(alien_0)
alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

#在空字典中添加键值对有时候可提供便利，而有时候必须这样做
#为此，可使用一对空花括号定义一个字典，再分行添加各个键值对
alien_0={}
alien_0['color']='green'
alien_0['points']=5
print(alien_0)

#要删除字典中的某一键值对时，可使用del语句将对应键值对彻底删除
#使用del语句时，必须指定字典名和要删除的键

alien_0={'color':'green','points':5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
language=favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

#遍历字典
#使用for循环遍历字典时，可以声明两个变量，用于存储键值对中的键和值
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }
for key,value in user_0.items():
    print(f"Key:{key}")
    print(f"Value:{value}\n")

#遍历字典中的所有键
#在不要使用字典中的值时，可以使用方法keys()遍历字典中的所有键
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in favorite_languages.keys():
    print(name.title())
#遍历字典时，会默认遍历所有的键
for name in favorite_languages:
    print(name.title())

friends=['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language=favorite_languages.get(name).title()
        print(f"\t{name.title()},I see you love {language}!")

#keys()方法并非只能用来遍历，实际上，它返回一个列表，其中包含字典的所有键
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll!")

#可使用sorted()方法来获得按特定顺序排列的键列表的副本
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for taking the poll.")

#可使用values()方法来返回一个值列表。不包含任何键
#这样获得的值列表中也许会含有重复的元素 若想要获得不重复的元素 可使用set()方法
#set()方法会让Python找出其中独一无二的元素，并使用这些元素来创建一个集合
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
for language in set(favorite_languages.values()):
    print(language.title())

#可使用一对花括号直接创建集合，并在其中用逗号分隔元素

#嵌套
#有时，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这种行为称为嵌套
#字典列表 即列表元素是字典
alien_0={'color':'green','points':5}
alien_1={'color':'yellow','points':10}
alien_2={'color':'red','points':15}
aliens=[alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)

aliens=[]
for alien_number in range(30):
    new_alien={'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"Total number of aliens:{len(aliens)}")

#在字典中存储列表
#每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
    }
print(f"You ordered a {pizza.get('crust')}-crust pizza "
      f"with the following toppings:")
for topping in pizza.get('toppings'):
    print(topping)

#在字典中存储字典
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton',
        },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris',
        },
    }
for username,userinfo in users.items():
    print(f"Username:{username.title()}")
    full_name=f"{userinfo.get('first')} {userinfo.get('last')}"
    location=f"{userinfo.get('location')}"
    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation:{location.title()}")