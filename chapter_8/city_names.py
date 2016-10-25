def city_country(city, country):
	formatted_string = city.title() + ", " + country.title()
	return formatted_string

print(city_country("Mumbai", "india"))
print(city_country('new york', 'usa'))
print(city_country('paris', 'france'))
