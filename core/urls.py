
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny
from main.models import *
from main.views import *

router = DefaultRouter()
router.register('movies', MovieViewSet)
router.register('review', ReviewViewSet)



schema_view = get_schema_view(
   openapi.Info(
      title="BLOG API",
      default_version='v1',
      description="For learning about DRF",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="milleniumdeath90@gmail.com"),
      license=openapi.License(name="Codial License"),
   ),
   public=True,
   permission_classes=[AllowAny],
)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('example/', ExampleAPIview.as_view()),
    path('actors/', ActorsAPIView.as_view()),
    path('movies/', MovieSwaggerAPIView.as_view()),
    path('subscriptions/', SubscriptionAPIView.as_view()),
    path('movies/<int:pk>', MovieRetrieveUpdateDeleteAPIView.as_view()),
    path('subscriptions/<int:pk>', SubscriptionRetrieveAPIView.as_view()),
]
urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
