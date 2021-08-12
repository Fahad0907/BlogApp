from decimal import Context
from django.db.models import query
from django.shortcuts import render
from rest_framework import serializers
from rest_framework import response
from rest_framework.authtoken.models import Token
from rest_framework.serializers import Serializer
from blog.serializer import PostSerializer
from rest_framework import viewsets, views
from blog.models import Post, Profile
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializer import UserSerializer, profileSerializer
# Create your views here.

class PostView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication, ]
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

class ProfileView(views.APIView):
    permission_classes = [IsAuthenticated,]
    authentication_classes = [TokenAuthentication, ]
    def get(self, request):
        user = request.user
        query = Profile.objects.get(user = user)
        serializer = profileSerializer(query)
        
        return Response({'userdata' : serializer.data})
    def put(sekf, request):
        obj = Profile.objects.get(user=request.user)
        serializer = profileSerializer(obj, data=request.data,context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response({"message " : "Request is gotten"})
    

class RegisterView(views.APIView):
    def post(self, request):
        serializers = UserSerializer(data= request.data)
        if serializers.is_valid():
            
            serializers.save()
            return Response({'error': False, 'message' : 'usersuccess full', 'data' : serializers.data})
        return Response({'error': True, 'message' : 'A user with that username already exist'})

class UserDataUpdate(views.APIView):
    permission_classes =[IsAuthenticated, ]
    authentication_classes = [TokenAuthentication, ]
    def put(self, request):
        user = request.user
        data = request.data
        obj = User.objects.get(username = user)
        obj.first_name = data['first_name']
        obj.last_name = data['last_name']
        obj.email = data['email']
        obj.save()
        return Response({"message " : "Request is gotten"})
