def make_car(manufacturer, model_name, **car_info):
	"""Make a car given details about manufacturer, model, and others"""
	my_car = {}
	my_car['manufacturer'] = manufacturer
	my_car['model'] = model_name
	for key, value in car_info.items():
		my_car[key] = value
	return my_car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
