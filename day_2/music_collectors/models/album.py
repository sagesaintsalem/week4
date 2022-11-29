class Album:
    def __init__(self, title, artist_id, release_year, genre, id = None):
        self.title = title
        self.artist_id = artist_id
        self.release_year = release_year
        self.genre = genre
        self.id = id