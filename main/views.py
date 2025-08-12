from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.generics import get_object_or_404
class ExampleAPIview(APIView):
    def get(self, request):
        return Response(
            "Bu DRF dagi 1-darsda yozildi"
        )
class ActorsAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            Actor.objects.create(
                name = serializer.data.get('name'),
                country = serializer.data['country'],
                gender = serializer.data['gender'],
                birthdate = serializer.data['birthdate'],
            )
            return Response(serializer.data, status=201)
        return Response(serializer.errors)

class MovieAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "success": True,
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "success": False,
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class MovieRetrieveUpdateDeleteAPIView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SubscriptionAPIView(APIView):

    def get(self, request):
        subscriptons = Subscription.objects.all()
        serializer = SubscriptionSerializer(subscriptons, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "success": True,
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "success": False,
            "data": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class SubscriptionRetrieveAPIView(APIView):
    def get(self, request, pk):
        subcription = get_object_or_404(Subscription, pk=pk)
        serializer = SubscriptionSerializer(subcription)
        return Response(serializer.data)
    def delete(self, request, pk):
        subcription = get_object_or_404(Subscription, pk=pk)
        subcription.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, pk):
        subcription = get_object_or_404(Subscription, pk=pk)
        serializer = SubscriptionSerializer(subcription, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
