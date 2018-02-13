from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from . import views


user_patterns = [
    path('signup', views.SignUpView.as_view(), name='signup'),
]


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    path('user/', include(user_patterns)),
]
