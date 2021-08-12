from django.db import models
from django.db.models import fields
from rest_framework import serializers
from blog.models import Post, Profile
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
User = get_user_model()

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('id', 'username', 'email', 'password','first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True , 'required' : True}}
        
    def create(self, validated_data,*args, **kwargs):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        Profile.objects.create(user=user)
        return user
        

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = UserSerializer(instance.user).data
        return data

    def validate(self, obj):
        obj['user'] = self.context['request'].user
        return obj


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = profileSerializer(instance.user.profile).data
        return data

    def validate(self, obj):
        obj['user'] = self.context['request'].user
        return obj