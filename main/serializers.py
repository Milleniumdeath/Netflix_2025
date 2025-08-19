import datetime

from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

    def validate(self, data):
        error = ""

        if data.get('country') == 'North Korea' and data.get('gender') == 'female':
            error += "Shimoliy Korea davlati yoki shu davlat ayol aktyorlari kiritilishi taqiqlanadi! "

        if data.get('birthdate') and data.get('birthdate') < datetime.date.today() - datetime.timedelta(weeks=5200):
            error += "Ushbu davrda tug'ilgan aktyorlar mavjud emas!"

        if error:
            raise serializers.ValidationError(error.strip())

        return data


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_genre(self, value):
        if value.lower() in ['horror', 'retro']:
            raise serializers.ValidationError(
                "Ushbu janrdagi kinolar taqiqlanadi!"
            )
        return value
    def validate_year(self, value):
        if int(value) <1888:
            raise serializers.ValidationError(
                "Ushbu yilda film suratga olinmagan!"
            )
        return value
    def validate_actors(self, actors):
        if len(actors) < 3:
            raise serializers.ValidationError(
                "Aktyorlar soni 3tadan kam!"
            )
        return actors

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewSafeSerializer(serializers.ModelSerializer):
    user =  serializers.CharField(source='user.username', read_only=True)
    movie = serializers.CharField(source='movie.name', read_only=True)
    class Meta:
        model = Review
        fields = '__all__'