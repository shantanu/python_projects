rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'ganges': 'india',
	}
	
for river, country in rivers.items():
	print("The " + river.title() + " runs through " + country.title())

print("\nThe major rivers are;")
for river in rivers.keys():
	print(river.title())

print("\nThe countries these rivers run through are:")
for country in rivers.values():
	print(country.title())
	
