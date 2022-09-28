from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views



router = DefaultRouter()
# router.register(r'cities',views.CityViewSet, basename="cities")
# router.register(r'regions',views.RegionViewSet, basename="regions")
# router.register(r'districts',views.DistrictViewSet, basename="districts")
# router.register(r'squares',views.SquareViewSet, basename="squares")
# router.register(r'stores',views.StoreViewSet, basename="stores")
# router.register(r'images',views.ImageViewSet, basename="images")
# router.register(r'users',views.UserViewSet, basename="users")




# app_name = ''
urlpatterns = [
    path('', views.base, name='base'),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.CustomAuthToken.as_view()),

   
]