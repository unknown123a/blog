from django.contrib.auth.tokens import PasswordResetTokenGenerator


# class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
#     def _make_hash_value(self, user, timestamp):
#         return str(user.pk) + str(timestamp) + str(user.is_active)

# # Create an instance of the token generator
# account_activation_token = AccountActivationTokenGenerator()

import logging
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.tokens import PasswordResetTokenGenerator

# Set up logging
logger = logging.getLogger(__name__)

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        """
        Generate a hash value for the token.
        """
        return f"{user.pk}{timestamp}{user.is_active}"

    def check_token(self, user, token):
        """
        Check if the token is valid and has not expired.
        """
        # First, validate the token using Django's built-in method
        if not super().check_token(user, token):
            logger.error("Token is invalid.")
            return False

        # Get the timestamp stored in Django's token system
        timestamp = self._num_seconds(self._today())  # Current time in seconds
        token_creation_time = self._num_seconds(user.last_login or user.date_joined)  # Use login or joined date

        # Set expiration time (2 minutes = 120 seconds)
        expiration_time = 120  

        # Compare timestamps
        if (timestamp - token_creation_time) > expiration_time:
            logger.error("Token has expired.")
            return False

        return True

    def _num_seconds(self, dt):
        """
        Convert a datetime object to seconds since the epoch.
        """
        return int(dt.timestamp())

    def _today(self):
        """
        Return the current time with timezone support.
        """
        return timezone.now()

# Create an instance of the token generator
account_activation_token = AccountActivationTokenGenerator()
