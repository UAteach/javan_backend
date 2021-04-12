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

        df = pd.read_csv(csv_file, sep=',')
        DEFAULT_PASSWORD = 'UTCH123$'
        results = {
            'added_users': [],
            'duplicated_users_errors': [],
            'user_creation_errors': []
        }

        ######## START OF making a list of non-dupes
        
        # taking the CSV file and storing the non-dupes
        # in a series (not_dupes) which will be iterated
        # through and added to the website by code further down

        email_bools = df["email"].duplicated(keep = False) 
        not_dupes_incom = df[~email_bools]
        un_bools = not_dupes_incom["username"].duplicated(keep = False)
        not_dupes = not_dupes_incom[~un_bools]
        
        ####### END OF making a list of non-dupes

        ####### START OF appending dupes to 'duplicated_users_errors'

        # taking the duplicated users in the CSV file and appending
        # them to 'duplicated_users_errors'
        
        dupes_un = df[df.duplicated(subset=['username'], keep=False)]
        dupes_em = df[df.duplicated(subset=['email'], keep=False)]
        dupes = pd.concat([dupes_un, dupes_em])
        dupes = dupes.sort_index()

        for index, row in dupes.iterrows():
             results['duplicated_users_errors'].append(row['username'])
        
        ####### END OF appending dupes to 'duplicated_users_errors'
       
        ####### START OF adding users to the site

        # iterates through the non-dupe series and 
        # checks to make sure the users arent already
        # in the website. Appends successfully uploaded 
        # users to 'added_users', appends unsuccessfully 
        # uploaded users to 'user_creation_errors' 
       
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
                results['user_creation_errors'].append(row['username'])
        
        ####### END OF adding users to the site

        #print(df)
        print(results)

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
