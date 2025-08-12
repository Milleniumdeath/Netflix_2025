from rest_framework import serializers
from .models import *

class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    country = serializers.CharField()
    gender = serializers.ChoiceField(Actor.GENDER.choices)
    birthdate = serializers.DateField()

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'