for value in range(1, 5):
	print(value)

#Using the list() function to turn range() into a list
numbers = list(range(1, 6))
print(numbers)

#Even numbers by incrementing by 2
even_numbers = list(range(2, 11, 2))
print (even_numbers)

#Generating a list of squares
squares = []
for value in range(1, 11):
	squares.append(value**2)
	
print(squares)
