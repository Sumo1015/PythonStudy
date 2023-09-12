#要在字符串中添加制表符，可以使用字符组合\t
print("\tPython")

#要在字符串中添加换行符，可以使用字符组合\n】
print("Languages:\nPython\nC++\nJavaScript")

#strip()方法可以暂时删除字符串开头和末尾的空白
#lstrip()方法可以暂时删除字符串开头（左边）的空白
#rstrip()方法可以暂时删除字符串末尾（右边）的空白
#若想永久地删除字符串中开头和末尾的空白，必须在删除后将其再次关联到变量
name="python "
print(name)
print(name.rstrip())
print(name)
name=name.rstrip()
print(name)