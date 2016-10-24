
age = input("Please tell me your age, I will tell you how much to pay me ")
age = int(age)

while age != -1:
	price = 0
	if age < 3:
		price = 0
	elif age >= 3 and age < 12:
		price = 10
	else: #older than 12
		price = 15
		
	print("PAY ME: $" + str(price) + " NOW!!!!")
	age = input("\n\nPlease tell me your age, I will tell you how much to pay me. -1 to quit ")
	age = int(age)
	
