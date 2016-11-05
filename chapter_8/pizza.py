def make_pizza(size, *toppings):
	"""Print a list of toppins that have been requested"""
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
	
