from django.contrib.auth.forms import UserCreationForm,UserChangeForm,SetPasswordForm
from .models import CustomUser

from django_recaptcha.fields import ReCaptchaField



class CustomUserCreationForm(UserCreationForm):
    captcha = ReCaptchaField()
    class Meta:
        model = CustomUser
        fields = ('email', 'name', 'password1', 'password2','captcha')

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ( 'name', 'avatar')
        # exclude =('password')

class Passwordchangform(SetPasswordForm):
    class Meta:
        model = CustomUser
        fields = ['new_password1','new_password2']

