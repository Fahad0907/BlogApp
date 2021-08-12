"""SocialApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from blog.views import PostView, ProfileView, RegisterView, UserDataUpdate
route = routers.DefaultRouter()
route.register('', PostView, basename="postview")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
    path('profile/', ProfileView.as_view() ),
    path('login/', obtain_auth_token ),
    path('register/', RegisterView.as_view() ),
    path('updateuser/', UserDataUpdate.as_view() ),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)