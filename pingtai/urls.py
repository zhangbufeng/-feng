from django.urls import path,include
from . import views
app_name="pingtai"
urlpatterns = [
    path('', views.index,name="index"),
    path('getKeyword/', views.getKeyword,name="getKeyword"),
    path('<int:con_id>/detail/', views.detail,name="detail"),
    path('kaitong/', views.kaitong,name="kaitong"),
    path('links/', views.links, name='links'),

]
