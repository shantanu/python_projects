def make_album(artist_name, album_title, tracks=''):
	album = {'name': artist_name.title(), 'title': album_title.title()}
	if tracks:
		album['tracks'] = tracks
	return album
	
print(make_album('the beatles', 'Abbey Road'))
print(make_album('galantis', 'pharmacy'))
print(make_album('pink floyd', 'dark side of the moon', 10))

	
while True:
	print("Give me the album information you want to store")
	print("Enter 'q' at any time to quit")
	
	title = input("Album title: ")
	if title == 'q':
		break
	artist = input("Album artist: ")
	if artist == 'q':
		break
	
	print(make_album(artist, title))
	
