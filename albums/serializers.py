from dataclasses import field

from rest_framework import serializers

from .models import Album


class AlbumSerializer(serializers.ModelSerializer):
    songs_count = serializers.SerializerMethodField()
    total_duration = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ["id", "name", "musician_id", "songs_count", "total_duration"]
        read_only_fields = ["musician_id"]

    def get_songs_count(self, obj):
        return obj.songs.count()

    def get_total_duration(self, obj):
        return sum([song.duration for song in obj.songs.all()])
