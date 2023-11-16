
from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

class EmailRefreshToken(RefreshToken):
    lifetime = timedelta(minutes=2)

class EmailAccessToken(AccessToken):
    lifetime = timedelta(minutes=2)

    
class CustomToken(RefreshToken):
    
    def get_token_for_email_verification(self, user):
        refresh = EmailRefreshToken.for_user(user)
        access = EmailAccessToken.for_user(user)
        return str(refresh), str(access)

    # this part should move to utils.py
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        access = refresh.access_token
        return str(refresh), str(access)

custome_refresh_token = CustomToken()

