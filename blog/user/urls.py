from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('login_for_medal/',views.login_for_medal,name='login_for_medal'),
    path('register/',views.register,name='register'),
    path('loginout/',views.loginout,name='loginout'),
    path('user_info/',views.user_info,name='user_info'),
    path('change_nickname/',views.change_nickname,name='change_nickname'),
    path('bind_email/',views.bind_email,name='bind_email'),
    path('change_password/',views.change_password,name='change_password'),
    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('send_verification_code/',views.send_verification_code,name='send_verification_code'),
]