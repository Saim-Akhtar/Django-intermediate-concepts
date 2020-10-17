from django.urls import path
from core.views import (
    regsiter_view, 
    index_view, 
    login_view, 
    logout_view, 
    auth_view, 
    premium_view,
    PremiumView,
    send_mail_tester
)

app_name = 'core'

urlpatterns = [
    path('',index_view,name='index'),
    path('register',regsiter_view,name='register'),
    path('login',login_view, name="login"),
    path('logout',logout_view, name='logout'),
    path('auth',auth_view,name="auth"),
    # path('premium',premium_view, name="premium"),
    path('premium',PremiumView.as_view(),name="premium"),
    path('mail',send_mail_tester, name='mail')
]