
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from main.models import *
from main.views import *

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('review', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('example/', ExampleAPIview.as_view()),
    path('actors/', ActorsAPIView.as_view()),
    # path('movies/', MovieAPIView.as_view()),
    path('subscriptions/', SubscriptionAPIView.as_view()),
    path('movies/<int:pk>', MovieRetrieveUpdateDeleteAPIView.as_view()),
    path('subscriptions/<int:pk>', SubscriptionRetrieveAPIView.as_view()),
]
