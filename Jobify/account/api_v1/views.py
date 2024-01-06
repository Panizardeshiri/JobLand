from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework import status
from .serializers import *
from ..models.accounts import *
from .utils import *
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated

class RegisterUserView(APIView):
     serializer_class = RegisterUserSerializer

     def post(self,request):
          serializer = self.serializer_class(data = request.data)
          serializer.is_valid(raise_exception=True)
          user = User(username = serializer.validated_data['username'],
                      email = serializer.validated_data['email'],
                      gender = serializer.validated_data['gender'],
                      user_type = serializer.validated_data['user_type'],
                      )
          user.set_password(serializer.validated_data['password'])
          user.save()
          created_user = User.objects.get(email=user.email)
          refresh_token,access_token =get_tokens_for_user(created_user)
          return Response({'status':status.HTTP_201_CREATED,
                           'message':'User is Successfully Registered.',
                           'refresh_token':refresh_token,
                           'access_token':access_token})


class LoginUserView(TokenObtainPairView):
     serializer_class = LoginUserSerializer



class LogoutUserView(APIView):
     serializer_class = LogoutUserSerializer
     permission_classes = (IsAuthenticated, )
     def post(self, request):
          serializer = self.serializer_class(data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response('User is Successfully Logged out.')


class ProfileListView(APIView):
     serializer_class = ProfileListSerializer
     # permission_classes = [IsAuthenticated, ]

     def get(self,request,id):
          # user = request.user
          print(request.user)
          profile = Profile.objects.get(user_id=id)
          serializer = self.serializer_class(profile)
         
          return Response(serializer.data)
# Qq