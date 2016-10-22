#Sorting in Alphabetical Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

#Sorting Reverse Order
cars.sort(reverse = True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the original list:')
print(cars)

#Using sorted(list) to get a temporarily sorted list
print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the reversely sorted list')
print(sorted(cars, reverse = True))

print('\nHere is the original list again')
print(cars)

#Printing a list in Reverse Order

print("\n")
print (cars)

cars.reverse()
print (cars)
