from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,handler404,handler500



urlpatterns = [
    path('',include('my_tests.urls')),
    path('admin-site', admin.site.urls),
    path('admin/',include("my_tests.adminurl")),
]
