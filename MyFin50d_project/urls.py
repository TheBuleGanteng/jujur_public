"""
URL configuration for MyFin50d project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path
from utils.views import readiness_check #This is done to allow readiness_check (defined in utils/views.py) access to the root url

urlpatterns = [
    #path('brokerage/', include('brokerage.urls')),
    path('', include(('users.urls', 'users'), namespace='users')),
    path("admin/", admin.site.urls),
    path('csp/', include('csp.urls', namespace='csp')),
    path('readiness_check/', readiness_check, name='readiness_check'),
    path('utils/', include(('utils.urls', 'utils'), namespace='utils')),
]
