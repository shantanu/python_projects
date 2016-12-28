name = input("Please give me your name: ")
filename = "guest.txt"

with open(filename, 'w') as file_object:
	file_object.write(name)

with open("guest_book.txt", 'a') as file_object:
	file_object.write(name + "\n")
	
print("Welcome, " + name)
