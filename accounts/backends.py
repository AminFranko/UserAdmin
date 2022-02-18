from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import User

class SettingsBackend(BaseBackend):

    def authenticate(self, request, email=None, username=None, password=None):
        # login_valid = (settings.ADMIN_LOGIN == email)
        # pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if username and password:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                
                return None
            return user
        elif email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
               
                return None
            return user

        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None