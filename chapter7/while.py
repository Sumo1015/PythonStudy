#while循环不断执行 直到指定的条件不满足为止
curreent_number=1
while curreent_number<=5:
    print(curreent_number)
    curreent_number+=1

#可以使用while循环让程序在用户愿意时不断运行
prompt="\nTell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
message=""
while message!='quit':
    message=input(prompt)
    if message!='quit':
        print(message)

#使用标志的循环
active=True
prompt="\nTell me something,and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."
while(active):
    message=input(prompt)
    if message == 'quit':
        active=False
    else:
        print(message)

#使用break退出循环
#要立即退出while循环 不再运行循环中余下的代码 也不管条件测试的结果如何 可使用break语句
prompt="\nPlease enter the name of a city you have visited:"
prompt+="\n(Enter 'quit' when you finished.)"
while True:
    city=input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

#要返回循环开头，并根据条件测试结果决定是否继续循环，可使用continue语句
curreent_number=0
while curreent_number<10:
    curreent_number+=1
    if curreent_number%2 == 0:
        continue
    print(curreent_number)
