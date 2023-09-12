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