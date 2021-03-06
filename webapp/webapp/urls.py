"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('configurations/', include('configurations.urls')),
    path('recording/', include('recording.urls')),
    path('maps/', include('maps.urls')),
    path('admin/', admin.site.urls),
    path('onboard',views.onboard),
    path('onboard2',views.onboard2),
    path('onboard3',views.onboard3),
    path('landing',views.landing),
    path('my_info',views.my_info),
    path('contacts',views.contacts),
    path('',views.index)
]
