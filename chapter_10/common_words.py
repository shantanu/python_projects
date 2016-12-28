def count_word(filename, word):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
			count = contents.lower().count(word.lower())
			print("The file " + filename + " contains the word " + word +  " " + str(count) + " number of times")
	except FileNotFoundError:
		print(filename + " was not found")

filenames = ['uck_finn.txt', 'alice.txt', 'siddhartha.txt']
for filename in filenames:
	count_word(filename, "the")
