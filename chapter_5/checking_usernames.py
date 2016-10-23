current_users = ['admin', 'aditya', 'josh', 'shantanu', 'anish']
new_users = ['aDItya', 'dan', 'mehak', 'niranjana', 'prad', 'JOSH']
for user in new_users:
	isGood = True
	for current_user in current_users:
		if current_user.lower() == user.lower():
			isGood = False
	if isGood:
		print(user + " is a valid username")
	else:
		print(user + ", Please enter a new username")
