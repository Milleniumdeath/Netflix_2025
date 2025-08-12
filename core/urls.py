
from django.contrib import admin
from django.urls import path
from main.models import *
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('example/', ExampleAPIview.as_view()),
    path('actors/', ActorsAPIView.as_view()),
    path('movies/', MovieAPIView.as_view()),
    path('subscriptions/', SubscriptionAPIView.as_view()),
    path('movies/<int:pk>', MovieRetrieveUpdateDeleteAPIView.as_view()),
    path('subscriptions/<int:pk>', SubscriptionRetrieveAPIView.as_view()),
]
