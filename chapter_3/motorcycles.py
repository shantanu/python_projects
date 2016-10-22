#Lists work
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#You can add items to a list using .append()
motorcycles.append('ducati')
print(motorcycles)

#Building lists dynamically
motorcycles = []
print(motorcycles)

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#Insertion at a specific index with .insert()
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Deletion with the del statement
del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#Deletion with return with .pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")


#Using .pop(index) to pop at an index
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#Removal by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)


motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

