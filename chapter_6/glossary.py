glossary = {
	'loop': 'Does thing over and over again',
	'if-statement': 'Checks if something is true',
	'list': 'A bunch of things in order',
	'dictionary': 'A bunch of key-value pairs',
	'python': 'A dope programming language',
	'java': 'is starting to look very verbose now',
	'c++': 'is also pretty complicated',
	'computer science': 'the best subject ever',
	}

for word in sorted(glossary.keys()):
	print(word)
	print("\t" + glossary[word])
	
