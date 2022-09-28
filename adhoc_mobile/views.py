import http
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
# from adhoc_mobile.models import City, Region, District, Square, Store, Image
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

# from adhoc_mobile.serializers import CitySerializer, RegionSerializer, DistrictSerializer, SquareSerializer, ImageSerializer, UserSerializer

# from adhoc_mobile.serializers import  UserSerializer



def base(request):
    return HttpResponse("Welcome to ADHOC Mobile")

    



# class CityViewSet(viewsets.ModelViewSet):
#     queryset= City.objects.all()
#     serializer_class=CitySerializer
#     permission_classes = ( permissions.AllowAny,)
#     permission_classes_by_action = {
#         'create': permission_classes,
#         'list': permission_classes,
#         'retrieve': permission_classes,
#         'update': permission_classes,
#         'destroy': permission_classes,
        
#     }


# class RegionViewSet(viewsets.ModelViewSet):
#     queryset= Region.objects.all()
#     serializer_class= RegionSerializer
#     permission_classes = ( permissions.AllowAny,)
#     permission_classes_by_action = {
#         'create': permission_classes,
#         'list': permission_classes,
#         'retrieve': permission_classes,
#         'update': permission_classes,
#         'destroy': permission_classes,
        
#     }



# class DistrictViewSet(viewsets.ModelViewSet):
#     queryset= District.objects.all()
#     serializer_class=DistrictSerializer
#     permission_classes = ( permissions.AllowAny,)
#     permission_classes_by_action = {
#         'create': permission_classes,
#         'list': permission_classes,
#         'retrieve': permission_classes,
#         'update': permission_classes,
#         'destroy': permission_classes,
        
#     }


# class SquareViewSet(viewsets.ModelViewSet):
#     queryset= Square.objects.all()
#     serializer_class=SquareSerializer
#     permission_classes = ( permissions.AllowAny,)
#     permission_classes_by_action = {
#         'create': permission_classes,
#         'list': permission_classes,
#         'retrieve': permission_classes,
#         'update': permission_classes,
#         'destroy': permission_classes,
        
#     }




# class StoreViewSet(viewsets.ModelViewSet):
#     queryset= Store.objects.all()
#     serializer_class=StoreSerializer
#     permission_classes = ( permissions.AllowAny,)
#     permission_classes_by_action = {
#         'create': permission_classes,
#         'list': permission_classes,
#         'retrieve': permission_classes,
#         'update': permission_classes,
#         'destroy': permission_classes,
        
#     }



# class ImageViewSet(viewsets.ModelViewSet):
#     queryset= Image.objects.all()
#     serializer_class=ImageSerializer
#     permission_classes = ( permissions.AllowAny,)
#     permission_classes_by_action = {
#         'create': permission_classes,
#         'list': permission_classes,
#         'retrieve': permission_classes,
#         'update': permission_classes,
#         'destroy': permission_classes,
        
#     }


# class UserViewSet(viewsets.ModelViewSet):
#     queryset= User.objects.all()
#     serializer_class=UserSerializer
   
#     permission_classes = ( permissions.AllowAny,)
#     permission_classes_by_action = {
#         'create': permission_classes,
#         'list': permission_classes,
#         'retrieve': permission_classes,
#         'update': permission_classes,
#         'destroy': permission_classes,
        
#     }

    
    
    
    
    
    
class CustomAuthToken(ObtainAuthToken):
    

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                        context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'password': user.password,
            'is_superuser': user.is_superuser,
            'last_login': user.last_login,
            
            
        })