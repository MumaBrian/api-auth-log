from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('get-details', views.UserDetailAPI.as_view()),
    path('register',views.RegisterUserAPIView.as_view()),
    path('list',views.ApiUserListView.as_view(),name='list'),

]
