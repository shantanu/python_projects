def sandwich_items(*items):
	print("\nMaking a sandwich with the following:")
	for item in items:
		print("- " + item)

sandwich_items("lettuce", "bacon", "tomato")
sandwich_items("chesse", "veggie burger", "ketchup", "hot sauce")
sandwich_items("cheeseburger")
