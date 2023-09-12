#处理列表的部分元素时，Python称之为切片
#要创建切片，可指定要使用的第一个元素和最后一个元素的索引 仍然遵循左闭右开
players=['charles','martina','michael','florence','eli']
print(players[0:3])
#如果没有指定第一个索引，Python将自动从表头开始
print(players[:4])
#如果没有指定终止索引，终止索引默认为表尾
print(players[2:])
#负数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任意切片
print(players[-3:])

#如果要遍历列表的部分元素 可在for循环中使用切片
players=['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

