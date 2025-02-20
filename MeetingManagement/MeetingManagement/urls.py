
from django.contrib import admin

from django.urls import path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),


#  admin page banaue

    path('Admin/Home', views.ADMIN_HOME, name='admin_home'),

]