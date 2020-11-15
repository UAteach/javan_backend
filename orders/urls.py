from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('', views.ListOrder.as_view()),
    path('<int:pk>/', views.Order.as_view()),

    path('content/', views.ListOrderContent.as_view()),
    path('content/<int:pk>/', views.OrderContent.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
