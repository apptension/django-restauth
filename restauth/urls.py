from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

from . import views

user_patterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('token', obtain_jwt_token, name='jwt_token'),
    path('me', views.UserProfileView.as_view(), name='profile'),
    path('confirm', views.UserAccountConfirmationView.as_view(), name='confirmation'),
]


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    path('user/', include(user_patterns)),
]
