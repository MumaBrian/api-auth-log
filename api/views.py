from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
# Create your views here.


#get user details using token authentication
class UserDetailAPI(APIView):
    # authentication_classes=(TokenAuthentication,)
    # permission_classes=(AllowAny,)
    pagination_class=PageNumberPagination

    def get(self,request,*args, **kwargs):
        user=User.objects.get(id=request.user.id)
        serializer=UserSerializer(user)
        return Response(serializer.data)

#register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes=(AllowAny,)
    serializer_class=RegisterSerializer


class ApiUserListView(ListAPIView):
    queryset=User.objects.get_queryset().order_by('id')
    serializer_class=UserSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(AllowAny,)
    pagination_class=PageNumberPagination


    