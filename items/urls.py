from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListItem.as_view()),
    path('<int:pk>/', views.Item.as_view()),
]