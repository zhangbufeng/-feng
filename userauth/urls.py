from django.urls import path,include
from . import views
app_name="userauth"
urlpatterns = [
    path('login/', views.login,name="login"),
    path('regist/', views.regist,name="regist"),
    path('loginout/', views.loginout,name="loginout"),
]