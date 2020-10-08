from django.contrib import admin
from django.urls import path,include
# from django.conf.urls import url,handler404,handler500

# handler404 = "my_tests.views.views_404"
# handler500 = "my_tests.views.views_404"

urlpatterns = [
    path('',include('my_tests.urls')),
    path('admin-site', admin.site.urls),
    path('admin/',include("my_tests.adminurl")),
]
