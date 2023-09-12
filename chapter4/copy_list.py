#要复制列表，可以创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引
my_food=['pizza','falafel','carrot cake']
friend_food=my_food[:]
my_food.append('cannoli')
friend_food.append('ice cream')

print("My favorite food are:")
print(my_food)
print("My friend's favoritr food are:")
print(friend_food)