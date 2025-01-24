
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('reg/',views.register,name="reg_page"),
    path('lg_p',views.login_page,name="login_page")
]