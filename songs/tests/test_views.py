from albums.models import Album
from django.urls import reverse
from model_bakery import baker
from musicians.models import Musician
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.views import status
from songs.models import Song


class ProductViewTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.song_1_data = {"name": "Before the Beginning", "duration": 548}

        cls.album = baker.make("Album")
        cls.song = baker.make("Song", album=cls.album)

        cls.base_url_create_song = reverse(
            "create_song",
            args=[
                cls.album.musician.id,
                cls.album.id,
            ],
        )

    def test_can_create_song(self):
        response = self.client.post(
            self.base_url_create_song, data=self.song_1_data
        )

        expected_status_code = status.HTTP_201_CREATED
        result_status_code = response.status_code

        self.assertEqual(len(response.data.keys()), 4)

        self.assertEqual(expected_status_code, result_status_code)
        self.assertIn("id", response.data)
        self.assertEqual(response.data["name"], self.song_1_data["name"])
        self.assertEqual(
            response.data["duration"], self.song_1_data["duration"]
        )
        self.assertIn("album_id", response.data)

        expected_return_fields = (
            "id",
            "name",
            "duration",
            "album_id",
        )

        result_return_fields = tuple(response.data.keys())

        self.assertTupleEqual(expected_return_fields, result_return_fields)

    def test_can_list_songs(self):
        response = self.client.get(self.base_url_create_song)

        expected_status_code = status.HTTP_200_OK
        result_status_code = response.status_code

        self.assertEqual(expected_status_code, result_status_code)

        self.assertEqual(len(response.data["results"]), 1)

        self.assertEqual(expected_status_code, result_status_code)
        expected_return_fields = (
            "id",
            "name",
            "duration",
            "album_id",
        )

        result_return_fields = tuple(response.data["results"][0].keys())

        self.assertTupleEqual(expected_return_fields, result_return_fields)

    def test_can_not_create_product_with_no_body(self):
        response = self.client.post(self.base_url_create_song, data={})

        expected_status_code = status.HTTP_400_BAD_REQUEST
        result_status_code = response.status_code

        self.assertEqual(len(response.data.keys()), 2)

        self.assertEqual(expected_status_code, result_status_code)
        expected_return_fields = (
            "name",
            "duration",
        )

        for field in expected_return_fields:
            self.assertEqual(response.data[field], ["This field is required."])

        result_return_fields = tuple(response.data.keys())

        self.assertTupleEqual(expected_return_fields, result_return_fields)
