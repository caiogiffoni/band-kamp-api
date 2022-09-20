from django_filters import rest_framework as filters
from songs.models import Song


class SongFilter(filters.FilterSet):
    min_duration = filters.NumberFilter(
        field_name="duration", lookup_expr="gte"
    )
    max_duration = filters.NumberFilter(
        field_name="duration", lookup_expr="lte"
    )

    class Meta:
        model = Song
        fields = ["duration"]
