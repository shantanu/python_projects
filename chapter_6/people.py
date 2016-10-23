
shantanu = {
	'first_name': 'shantanu',
	'last_name': 'laghate',
	'age': 17,
	'city': 'new brunswick'
	}

alex = {
	'first_name': 'alexander',
	'last_name': 'ren',
	'age': 18,
	'city': 'New York',
	}
	
sat = {
	'first_name': 'satyen',
	'last_name': 'gupta',
	'age': 18,
	'city': 'Chicago',
	}

trio = [shantanu, alex, sat]
for person in trio:
	full_name = person['first_name'] + " " + person['last_name']
	
	print("Name: \t" + full_name.title())
	print("Age: \t" + str(person['age']))
	print("City: \t" + person['city'].title())
	print("\n\n")
