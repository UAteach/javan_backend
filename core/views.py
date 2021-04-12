import os
import pandas as pd

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.exceptions import ParseError

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


class FileUploadView(APIView):
    permission_classes = (permissions.AllowAny,)
    parser_classes = ( MultiPartParser, FormParser, )

    def post(self, request):
        if 'file' not in request.data:
            raise ParseError("No file provided")

        csv_file = request.data['file']

        ext = os.path.splitext(csv_file.name)[1].lower()
        print(ext)
        if ext != '.csv':
            raise ParseError("Improper file type provided")

        #df = pd.read_csv(csv_file)
        df = pd.read_csv(csv_file, sep=',')
        DEFAULT_PASSWORD = 'UTCH123$'
        results = {
            'added_users': [],
            'errors': []
        }

        ####################### 
        # Replace this bit...

       


        # dupes = df[["email" or "username"]].duplicated(keep = False) 
        # not_dupes = df[~dupes]


        email_bools = df["email"].duplicated(keep = False) 
        not_dupes_incom = df[~email_bools]
        un_bools = not_dupes_incom["username"].duplicated(keep = False)
        not_dupes = not_dupes_incom[~un_bools]

        #for i in range(0, len(not_dupes['username'])):

        for index, row in not_dupes.iterrows():
            if not (ExtendedUser.objects.filter(username=row['username']).exists() or ExtendedUser.objects.filter(email=row['email']).exists()):
                ExtendedUser.objects.create(username=row['username'],
                                            first_name=row['first_name'],
                                            last_name=row['last_name'],
                                            classification=0,
                                            email=row['email'],
                                            password=DEFAULT_PASSWORD)
                results['added_users'].append(row['username'])
            else:
                results['errors'].append(row['username'])

        #print(df)
        print(results)

        # not_dupes = list(not_dupes['username']) 
        

        # ###############################

        

        # if not ExtendedUser.objects.filter(username='rrau').exists():
        #     ExtendedUser.objects.create(username='rrau',
        #                                 first_name='ryan',
        #                                 last_name='rau',
        #                                 classification=0,
        #                                 email='ryanrau@uark.edu',
        #                                 password=DEFAULT_PASSWORD)
        #     results['added_users'].append('rrau')
        # else:
        #     ExtendedUser.objects.filter(username='rrau').delete()
        #     results['errors'].append('failed to add rrau')

        #######################

        return Response(results, status=status.HTTP_200_OK)
