from rest_framework.views import APIView
from rest_framework.response import Response
from ..api.serializer import UserRegistrationSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework import status
from mail_templated import EmailMessage
from ..utils.user_auth import *
from ..utils.user_token import custome_refresh_token as ctoken
from ..utils.user_email import EmailThreading

User = get_user_model()

class UserRegistrationApiView(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request, *args, **kwargs):       
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # send email to created user
        refresh_token, access_token = ctoken.get_tokens_for_user(user)

        if user.email:
            verification_refresh_token, verification_access_token = ctoken.get_token_for_email_verification(user)
            print('_____________', verification_access_token, '______________', verification_refresh_token)
            verification_email = EmailMessage('emails/email_varification.html', 
                                        {'token':verification_access_token}, 
                                        'kaka.mehrsam@gmail.com', 
                                        [user.email])
            
            EmailThreading(verification_email).start()
        return Response({
            'message':"sign up successfully",
            'refresh_token' : refresh_token,
            'access_token' : access_token,
        },status=status.HTTP_201_CREATED)
