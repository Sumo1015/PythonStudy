my_pizza=['black pepper beef','colorful fruit','orleans roast chicken']
friend_pizza=my_pizza[:]
my_pizza.append('durian cheese')
friend_pizza.append('hawaiian style')
print("My favorite pizzas are:")
for pizza in my_pizza:
    print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza.title())