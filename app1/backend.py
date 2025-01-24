# app1/backend.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailAuthBackend(ModelBackend):
    """
    Custom authentication backend that authenticates users based on their email.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            print("No username or password provided")
            return None

        try:
            user_model = get_user_model()
            print(f"Attempting to authenticate user with email: {username}")
            
            user = user_model.objects.get(email=username)
            print(f"User found: {user}")

            if not user.is_active:
                print("User is inactive")
                return None  # User is inactive, cannot log in

            if user.check_password(password):
                print("Password is correct")
                return user  # Authentication successful
            else:
                print("Password is incorrect")
                return None  # Invalid password
        except user_model.DoesNotExist:
            print(f"No user found with email: {username}")
            return None
