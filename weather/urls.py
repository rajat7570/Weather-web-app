from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_w, name='list_w'),
    path('add_city/', views.add_city, name='add_city'),
    path('delete_city/<int:pk>/', views.delete_city, name='delete_city'),
]