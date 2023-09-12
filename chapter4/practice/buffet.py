buffet=('cake','salad','sushi','cola','rice')
print("We provide five kinds of food:")
for buf in buffet:
    print(buf)

#下面这样修改元组中的元素是错误的
#buffet[2]='pizza'

buffet=('cake','pizza','sushi','steak','rice')
print("We provide five kinds of food:")
for buf in buffet:
    print(buf)