from django.contrib import admin
from django.urls import path,include,re_path
from . import views
app_name='self'
urlpatterns = [
    path('', views.index,name='index'),
    path('selfinfo/', views.selfinfo,name='selfinfo'),
    path('liuyan/', views.liuyan,name='liuyan'),
    path('lianjie/', views.lianjie,name='lianjie'),
    path('loginout/', views.loginout,name='loginout'),
    path('guanli/', views.guanli,name='guanli'),
    path('upload/', views.upload,name='upload'),
    path('img/', views.img,name='img'),
    path('passed/', views.passed,name='passed'),
    path('article/', views.article,name='article'),#管理文章
    path('addArticle/', views.addArticle,name='addArticle'),#添加文章
]
