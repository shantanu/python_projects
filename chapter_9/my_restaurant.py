from restaurant import Restaurant

restaurant_1 = Restaurant('Hunan Spring', 'chinese')
restaurant_1.describe_restaurant()
restaurant_1.get_number_served()

restaurant_1.number_served = 50
restaurant_1.get_number_served()

restaurant_1.set_number_served(100)
restaurant_1.get_number_served()

restaurant_1.increment_number_served(50)
restaurant_1.get_number_served()
