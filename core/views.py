from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken
from .models import ExtendedUser


# Needed for django group permissions...
class DjangoGroupCompatibleAPIView(APIView):
    queryset = ExtendedUser.objects.none()


class current_user(DjangoGroupCompatibleAPIView):
    def get(self, request):
        queryset = ExtendedUser.objects.none()
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserList(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserInformation(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def get(self, request, pk):
        user = ExtendedUser.objects.get(pk=pk)   
        serializer = UserSerializer(user)
        return Response(serializer.data)