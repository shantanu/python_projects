sandwich_orders = ['Godfadda', 'Pastrami', 'Griller #8', 'Pastrami', 'Pastrami', 'Jay Ray', 'Gobbler']
finished_sandwiches = []

print(sandwich_orders)
print("We don't have any Pastrami. Sucks.")

while 'Pastrami' in sandwich_orders:
	sandwich_orders.remove('Pastrami')
	
print(sandwich_orders)

while sandwich_orders:
	making_sandwich = sandwich_orders.pop()
	print("I made your " + making_sandwich)
	finished_sandwiches.append(making_sandwich)

print("\n\nThe following sandwiches were made")
for sandwich in finished_sandwiches:
	print(sandwich)

