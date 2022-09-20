import uuid
from sqlite3 import IntegrityError

from django.db.utils import IntegrityError
from django.test import TestCase
from model_bakery import baker
from songs.models import Song


class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.album_1 = baker.make("Album")
        cls.song_1 = baker.make("Song", album=cls.album_1)

    def test_many_to_one_relationship_is_made(self):
        print("executando test_many_to_one_relationship_is_made")

        self.assertEqual(self.song_1.album, self.album_1)

    def test_many_to_one_relationship_with_users(self):
        print("executando test_many_to_one_relationship_with_users")
        album_2 = baker.make("Album")
        self.song_1.album = album_2
        self.song_1.save()

        self.assertEqual(self.song_1.album, album_2)
