from collections import OrderedDict

glossary = OrderedDict()


glossary['loop'] = 'Does thing over and over again'
glossary['if-statement'] = 'Checks if something is true'
glossary['list'] = 'A bunch of things in order'
glossary['dictionary'] = 'A bunch of key-value pairs'


for key, value in glossary.items():
	print(key.title() + " : " + value)
