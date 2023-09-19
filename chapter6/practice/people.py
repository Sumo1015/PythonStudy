people_0={}
people_0['first_name']='Yang'
people_0['last_name']='Bai'
people_0['age']=22
people_0['city']='Nanjing'
print(people_0)
print("\n")

people_1={
    'first_name':'Mo',
    'last_name':'Su',
    'age':22,
    'city':'Yangzhou',
    }
people_2={
    'first_name':'Yuan',
    'last_name':'Zhi',
    'age':22,
    'city':'Luoyang',
    }
people=[people_0,people_1,people_2]
for p in people:
    print(p)
