from rest_framework import serializers
from django.core import exceptions
import django.contrib.auth.password_validation as validators
from ..models import (Adress, Profile)
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenBlacklistSerializer
from django.contrib.auth import get_user_model
from django.conf import settings
import re
from rest_framework.response import Response
from decimal import Decimal
from ..utils.user_auth import user_utils, _error




User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=250, write_only=True)
    class Meta:
        model = User
        fields =[ 'username', 'password', 'password1']
    


    def validate(self, attrs):

        user_utils.username_validation( attrs['username'] )

        if attrs.get('password') != attrs.get('password1'):
            _error('Password does not match')
        try:
            validators.validate_password(password=attrs.get('password'))
        
        except exceptions.ValidationError as e:
            raise _error( list(e.messages) )
        
        return super(UserRegistrationSerializer, self).validate(attrs)
    def create(self, validated_data):

        user_data = user_utils.detect_username(validated_data['username'])
        print(50*"$", user_data)

        if user_data['email']:
            user = User.objects.create( 
                    username=validated_data['username'],            
                    email = user_data['email']
                )
        else: 
            user = User.objects.create(
                username = validated_data['username'],
                phone = user_data['phone']
            )

        user.set_password(validated_data['password'])
        user.save()
        return user
