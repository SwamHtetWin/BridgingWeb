my_foods = ['pizza','falafel','carrot cake']

friend_food = my_foods[:]
my_foods.append('cheese pizza')
friend_food.append('pineapple pizza')

print("My fav pizzas are:")
for pizza in my_foods:
    print(pizza)

print("My friend's fav pizza are:")
for pizza in friend_food:
    print(pizza)