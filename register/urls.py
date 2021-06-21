from django.urls import path
from . import views


app_name = 'register'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('index/', views.Index.as_view(), name='index'),
    path('mypage/', views.Mypage.as_view(), name='mypage'),

]