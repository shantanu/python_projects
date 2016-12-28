while True:
	try:
		first_number = int(input("Enter first number: "))
		second_number = int(input("Enter second number: "))
	except ValueError:
		print("That is not a number!")
	else:
		print(first_number + second_number)
	
	cont = input("Try again? q to quit anything else to stay ")
	if (cont == 'q'):
		break
	
