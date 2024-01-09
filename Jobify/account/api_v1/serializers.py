from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenBlacklistSerializer
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from ..models.accounts import *
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from ..models.profiles import *
user = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField( write_only=True,required=True, validators=[validate_password])
    password2 = serializers.CharField( write_only=True,required=True,)

    class Meta:
        model = User
        fields = ('username','email','gender','user_type','password','password2')

    
    def validate(self,attrs):
       if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':'Password does not match!'})
       
       return attrs


class LoginUserSerializer(TokenObtainPairSerializer):
     
     def validate(self, attrs):
        user = User.objects.filter(email=attrs.get('email'))
        if not user:
            raise serializers.ValidationError({'error':"No active account found with the given credentials"})

        try:
            data = super().validate(attrs)
            data['username'] = self.user.username
            data['is_active'] = self.user.is_active
            message = {'status':status.HTTP_202_ACCEPTED,
                       'message':'User is Successfully Logged in.'}

            return data,message
        except:
            raise serializers.ValidationError("Invalid password")


class LogoutUserSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()  

    def validate(self, attrs):
        self.token = attrs['refresh_token']
        return attrs
    
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')


class AddressSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Address
    #     # fields = ('state','city','street','alley','plaque','postal_code','extra_comment')
    #     fields = '__all__'

    class Meta:
        model = Address
        exclude = ('user', )
        
    def create(self, validated_data):
        user = self.context.get('request').user
        validated_data['user_id'] = user.id
        address = Address.objects.create(**validated_data)
        Profile.objects.get(user= user).address.add(address)
        return address







class EditProfileSerializer(serializers.ModelSerializer):
    # images = serializers.CharField(source="get_profile_images")
    # skills =serializers.StringRelatedField(many=True)
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio',"skill")

    
    def update(self,instance,validated_data):
        print('&*()',validated_data)
        user = self.context.get('request').user
        user_profile = Profile.objects.get(user=user)
        user_profile.skill.add(validated_data['skill'])
        profile = Profile.objects.update(**validated_data)
        
        return profile

        

class ProfileListSerializer(serializers.ModelSerializer):
    images = serializers.CharField(source="get_profile_images")
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'description', 'images',)