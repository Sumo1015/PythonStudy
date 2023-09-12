people=['Eric','Linda','Steve','Marry','Frank']
favorite_number={
    'Eric':7,
    'Linda':22,
    'Steve':9,
    'Marry':12,
    'Frank':32,
    }
for i in range(0,5):
    name=people[i]
    print(f"{name.title()}'s favorite number is {favorite_number.get(name)}.\n")
