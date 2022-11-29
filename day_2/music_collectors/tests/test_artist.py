import unittest
from models.artists import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist('Ghost', 1)

    def testArtistName(self):
        self.assertEqual('Ghost', self.artist.artist_name)