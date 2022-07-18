from django import views
from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView,ApiUserListView
app_name = 'api'

urlpatterns = [
    path('details', UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
    path('list',ApiUserListView.as_view(),name='list'),

]
