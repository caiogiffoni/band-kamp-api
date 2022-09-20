# create_multiple_users.py

from albums.models import Album
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from musicians.models import Musician


class Command(BaseCommand):
    help = "Create 2 musicians with albuns"

    def add_arguments(self, parser):
        parser.add_argument(
            "-p",
            "--prefix",
            type=str,
            help="Define a username prefix",
        )

    def handle(self, *args, **kwargs):
        prefix = kwargs["prefix"]
        for i in range(2):
            if prefix:
                username = f"{prefix}_{get_random_string(5)}"
            else:
                username = get_random_string(5)
            i = Musician.objects.create(
                first_name=username,
                last_name=get_random_string(3),
                instrument=get_random_string(1),
            )
            Album.objects.create(
                name=f"The album {get_random_string(3)}", musician=i
            )
