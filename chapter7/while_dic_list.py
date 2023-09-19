#使用wile循环处理列表和字典
#for循环是一种遍历列表的有效方式，但不应在for循环中修改列表，否则将导致Python难以跟踪其中的元素
#要在遍历列表的同时对其进行修改，可使用while循环
#在列表之间移动元素
unconfirmed_users=['alice','brian','candace']
confirmed_users=[]
while unconfirmed_users:#验证每个用户，直到没有未验证用户为止 只要列表不为空就进入循环
    current_user=unconfirmed_users.pop()
    print(f"Verifying uer:{current_user.title()}")
    confirmed_users.append(current_user)
#显示所有已被验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#删除为特定值的所有列表元素
#remove()方法每次调用只删除一个指定值的元素，若列表中有多个值相同的待删除元素，则需通过循环判断来确保删除每个值
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#使用用户输入来填充字典
#可使用while循环提示用户输入任意多的信息，并将收集到的数据存储在一个字典中
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name?")
    response=input("Which mountain would you like to climb someday?")
    responses[name]=response
    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active=False
print("\n---Polling Results---")
for name,response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
