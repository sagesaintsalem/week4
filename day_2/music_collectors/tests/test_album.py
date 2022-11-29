import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album('Meliora', 3, 2016, 1)


    def testHasTitle(self):
        self.assertEqual('Meliora', self.album.title)

    def testHasYear(self):
        self.assertEqual(2016, self.album.release_year)

    def testHasArtistId(self):
        self.assertEqual(3, self.album.artist_id)