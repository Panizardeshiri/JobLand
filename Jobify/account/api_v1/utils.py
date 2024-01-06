from rest_framework_simplejwt.tokens import RefreshToken
from datetime import timedelta

class customRefreshToken(RefreshToken):
    lifetime = timedelta(minutes=5)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    return str(refresh), str(access)