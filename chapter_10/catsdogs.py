def print_file(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			print(contents)
	except FileNotFoundError:
		#print("The file " + filename + " was not found.")
		pass
		
		
filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	print_file(filename)
