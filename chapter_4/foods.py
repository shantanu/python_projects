my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('canoli')
friend_foods.append('ice cream')
my_foods.append('chinese')
my_foods.append('pasta')
my_foods.append('lol')

print("My favorite goods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)



print("\n\nThe first three items in the list are:")
print(my_foods[:3])

print("\nThree items from the middle of the list are:")
print(my_foods[2:5])

print("\nThree items from the end of the list are:")
print(my_foods[-3:])

for food in my_foods:
	print(food)
