from django.urls import path
from django.conf.urls import url
from .views import FileUploadView
from accounts.views import login
from accounts.views import register
from accounts.views import logout
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^feedback/$',views.feedback,name='feedback'),
    url(r'^upload/$', FileUploadView.as_view(), name='file-upload'),
    path('register',register,name='register'),
    path('login',login,name='login'),
    path('logout',logout,name='logout')
    
]
