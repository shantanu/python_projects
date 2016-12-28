filename = "poll_answers.txt"

keep_going = True
while keep_going == True:
	response = input("Why do you like programming? ")
	
	
	with open(filename, 'a') as file_object:
		file_object.write(response + "\n")
	
	going_input = input("Keep going? (y/n)")
	if going_input == 'y':
		keep_going = True
	else:
		keep_going = False
	
	print(keep_going)


