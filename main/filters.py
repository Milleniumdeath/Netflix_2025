
from .models import *
import django_filters

class MovieFilter(django_filters.FilterSet):
    start_year = django_filters.NumberFilter(field_name="year", lookup_expr='gte')
    end_year = django_filters.NumberFilter(field_name="year", lookup_expr='lte')

    class Meta:
        model = Movie
        fields = ['name', 'start_year', 'end_year']

class ReviewFilter(django_filters.FilterSet):
    min_rate = django_filters.NumberFilter(field_name="rate", lookup_expr='gte')
    max_rate = django_filters.NumberFilter(field_name="rate", lookup_expr='lte')

    class Meta:
        model = Review
        fields = ['min_rate', 'max_rate']