import json

def get_stored_number():
	filename = "favorite_number.json"
	try:
		with open(filename) as f_obj:
			number = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return number
	
def get_new_number():
	filename = "favorite_number.json"
	
	with open(filename, 'w') as f_obj:
		number = input("What is your favorite number? ")
		json.dump(number, f_obj)
	return number
	
def favorite_number():
	number = get_stored_number();
	if number:
		print("Welcome back! Your favorite number is " + number)
	else:
		number = get_new_number()
		print("We will remember that your favorite number is " + number)


favorite_number()
keep = input("Do you like your number? Enter 'n' to change: ")
if keep == 'n':
	get_new_number()
