def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())
			
def make_great(magicians):
	for counter in range(len(magicians)):
		magicians[counter] = 'the Great ' + magicians[counter]
	return magicians
	
magicians = ['david copperfield', 'harry houdini', 'chris angel']


show_magicians(magicians)

great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)

