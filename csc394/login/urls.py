from django.urls import path
from . import views
from django.conf.urls import url

app_name = "login"

urlpatterns = [
   path('', views.login_index, name='login_index'),
   url('register',views.register, name='register'),
   url('signin', views.login_user, name='login_user'),
   url('dashboard',views.dashboard,name='dashboard'),
   url('logout',views.logout_user,name='logout_user'),
   url('taskview',views.taskView,name='taskview'),
 ]