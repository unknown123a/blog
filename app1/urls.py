
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path




urlpatterns = [
    path('',views.home,name='home_page'),
    path('reg/',views.register,name="reg_page"),
    path('lg_p/',views.login_page,name="login_page"),
    path('lp_up',views.update_acc,name='update_acc'),
    path('resend_acc_link',views.resend_acc,name="resend_acc"),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('cng_pswrd',views.cng_pswrd,name='cng_pass'),


    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='app1/password_reset.html'), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='app1/password_reset_sent.html'), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='app1/password_reset_form.html'), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(template_name='app1/password_reset_done.html'), name="password_reset_complete"),


    
]

    # Password reset




