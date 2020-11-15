from django.urls import path
from .views import current_user, UserList, UserInformation

urlpatterns = [
    path('current_user/', current_user.as_view()),
    
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserInformation.as_view())
]
