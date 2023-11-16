import re
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from rest_framework.serializers import ValidationError


def _error(message):
    raise ValidationError({
        'error':{
            'detail': message
        }
    })

phone_pattern = "^([0]{1}[0-9]{3}[0-9]{3}[0-9]{4})|([\+]{1}[1-9]{1}[0-9]{2}[0-9]{3}[0-9]{6})"
email_regex = '^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$'

class UserUtils():
    def __init__(self) -> None:
        self.phone_pattern = "^([0]{1}[0-9]{3}[0-9]{3}[0-9]{4})|([\+]{1}[1-9]{1}[0-9]{2}[0-9]{3}[0-9]{6})"
        self.email_pattern = '^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+$'

    def normilize_phone(self, phone):
        phone = phone.strip()
        if '+' in phone:
            return phone
        return '+98'+ phone[1:]
            

    def check_pattern(self, pattern, var):
        res = re.fullmatch(pattern, var)
        return res
    
    def username_validation(self, username):
        if not self.check_pattern(self.email_pattern, username):
            if not self.check_pattern(self.phone_pattern, username):
                _error('Enter correct email address or phone number!')

    def detect_username(self, username):
        username = username.strip()
        if self.check_pattern(self.email_pattern, username):
            email = username
            phone = None
        else:
            email = None        
            if self.check_pattern(self.phone_pattern, username):
                phone = self.normilize_phone(username)
        user_data = {
            'username': username,
            'phone': phone,
            'email': email
        }
        return user_data


              
user_utils = UserUtils()

