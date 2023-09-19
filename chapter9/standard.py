#Python标准库是一组模块，我们可以使用标准库中的任何函数和类，只需在程序开头包含一条简单的import语句即可
#模块random
#randint()函数将两个整数作为参数，并随机返回一个位于这两个整数之间(含)的整数
from random import randint
print(randint(1,6))

#choice()函数将一个列表或元组作为参数，并随机返回其中的一个元素
from random import choice
players=['charles','martina','michael','florence','eli']
print(choice(players))