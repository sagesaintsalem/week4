from models.album import Album
from models.artists import Artist

import repos.album_repo as album_repo
import repos.artist_repo as artist_repo

album_repo.delete_all()
artist_repo.delete_all()

artist1 = artist_repo.create(Artist("Ghost"))
artist2 = artist_repo.create(Artist("Type O Negative"))
artist_repo.create(Artist("Skynd"))

print(artist_repo.select_all())

album1 = Album("Meliora", artist1.id, 2016, "occult rock")
album_repo.create(album1)
album2 = Album("Prequelle", artist1.id, 2018, 'occult rock')
album_repo.create(album2)
album3 = Album("October Rust", artist2.id, 1996, "goth rock")
album_repo.create(album3)

print(album_repo.select_all())
print(album_repo.get_album_by_artist(1))

