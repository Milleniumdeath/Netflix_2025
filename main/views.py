from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response

from .filters import *
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

##pagination ni o'zimiz o'zgartirishimiz mumkin bo'lgan klass
# class CustomPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 100
class MyCursorPagination(CursorPagination):
    page_size = 2
    ordering = '-id'   # yangidan eskiga qarab tartib

class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ['name',]
    ordering_fields = ['name', 'year']
    filterset_fields = ['name',]
    filterset_class = MovieFilter

    def get_serializer_class(self):
        if self.action == 'add_actor':
            return ActorSerializer
        return self.serializer_class

    @action (detail=True, methods=['get'])
    def actors(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        actors = movie.actors.all()
        serializer = ActorSerializer(actors, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='add-actor')
    def add_actor(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = ActorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            actor = serializer.instance
            movie.actors.add(actor)
            response = {
                "success": True,
                "data": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ExampleAPIview(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                description='Search by movie of name',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING

            ),
            openapi.Parameter(
                name='ordering',
                description='Ordering by name, year  ',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=['name', 'year', '-name', '-year'],
            ),

        ]
    )
    def get(self, request):
        movies = Movie.objects.all()
        search = request.GET.get('search')
        if search:
            movies = movies.filter(Q(name__icontains=search) | Q(genre__icontains=search))

        ordering = request.GET.get('ordering')
        if ordering:
            try:
                movies = movies.order_by(ordering)
            except Exception as e:
                return Response(
                    {
                        'success': False,
                        'error': 'Ordering only by title, views, created_at at with (asc, desc)'
                    }
                )
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
class ActorsAPIView(APIView):
    def get(self, request):
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
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

class MovieSwaggerAPIView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='search',
                description='Search by movie of name',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING

            ),
            openapi.Parameter(
                name='ordering',
                description='Ordering by name, year  ',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=['name', 'year',  '-name', '-year'],
            ),

        ]
    )
    def get(self, request):
        movies = Movie.objects.all()
        search = request.GET.get('search')
        if search:
            movies = movies.filter(Q(name__icontains=search) | Q(genre__icontains=search))

        ordering = request.GET.get('ordering')
        if ordering :
            try:
                movies = movies.order_by(ordering)
            except Exception as e:
                return Response(
                    {
                        'success': False,
                        'error': 'Ordering only by title, views, created_at at with (asc, desc)'
                    }
                )
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
    def validate_actors(self, value):
        if value.actor.count() >= 3:
            raise serializers.ValidationError(
                "Kamida 3 actor kiritish kerak"
            )
        return value



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

class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = MyCursorPagination
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ['user', 'movie' ]
    ordering_fields = ['rate', 'created_at']
    filterset_fields = ['user.username', ]
    filterset_class = ReviewFilter

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReviewSafeSerializer
        return self.serializer_class

