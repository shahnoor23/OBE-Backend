from rest_framework import generics, permissions, authentication, status, viewsets
from rest_framework.response import Response
from .serializers import InventoryFile_Serializer,ProfileSerializer,UserSerializer, AdminRegisterSerializer, ChairmanRegisterSerializer,  LoginSerializer, DepHeadRegisterSerializer, TeacherRegisterSerializer, StudentRegisterSerializer
from django.contrib.auth import get_user_model
from .models import User , InventoryFile , ProfileCheck
from .renderers import UserJSONRenderer
import os
from os import listdir
from os.path import isfile, join
from os import walk
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.parsers import JSONParser
import requests
import pandas as pd
import csv
import csv
import io



class InvertoryUpload(viewsets.ModelViewSet):
    queryset = InventoryFile.objects.all()
    serializer_class = InventoryFile_Serializer
    parser_classes = [MultiPartParser, FormParser]


class Profile(viewsets.ModelViewSet):

    queryset = ProfileCheck.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        target_dir = base_dir + '\inventory'
        onlyfiles = [f for f in listdir(
            target_dir) if isfile(join(target_dir, f))]
        for i in onlyfiles:
            filedir = target_dir + '\\' + i
            shop_inventory = pd.read_csv(filedir)
            profiles = [
                ProfileCheck(
                    name=row['name'],
                    email=row['email'],
                    address=row['address'],
                )
                for index, row in shop_inventory.iterrows()
            ]
            ProfileCheck.objects.bulk_create(profiles)

            os.remove(filedir)




# login  api


class LoginApi(generics.GenericAPIView):
   # renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response(serializer.data, status=status.HTTP_200_OK)


# Registartion api for admin account


class RegisterApi(generics.GenericAPIView):
    renderer_classes = (UserJSONRenderer,)
    serializer_class = AdminRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# Registration for Chairman api


class ChairmanRegisterApi(generics.CreateAPIView):
    serializer_class = ChairmanRegisterSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        data = ChairmanRegisterSerializer(data=request.data)
        if data.is_valid():
            user = User.objects.get(email=self.request.user)
            if user.is_admin == True:
                return self.create(request, *args, **kwargs)
            else:
                response = {"message": "Must be an Admin"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)


# Registration for Department Head api


class DepHeadRegisterApi(generics.CreateAPIView):
    serializer_class = DepHeadRegisterSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        data = DepHeadRegisterSerializer(data=request.data)
        if data.is_valid():
            user = User.objects.get(email=self.request.user)
            if user.is_chairman == True:
                return self.create(request, *args, **kwargs)
            else:
                response = {"message": "Must be a Chairman"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

# Registration for Teacher api


class TeacherRegisterApi(generics.CreateAPIView):
    serializer_class = TeacherRegisterSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        data = TeacherRegisterSerializer(data=request.data)
        if data.is_valid():
            user = User.objects.get(email=self.request.user)
            if user.is_depHead == True:
                return self.create(request, *args, **kwargs)
            else:
                response = {"message": "Must be a Department Head"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

# Registration for Student api


class StudentRegisterApi(generics.CreateAPIView):
    serializer_class = StudentRegisterSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        data = StudentRegisterSerializer(data=request.data)
        if data.is_valid():
            user = User.objects.get(email=self.request.user)
            if user.is_depHead == True:
                return self.create(request, *args, **kwargs)
            else:
                response = {"message": "Must be a Department Head"}
                return Response(response, status=status.HTTP_400_BAD_REQUEST)


"""
# view for department head list


class ManageAccountsDepartmentView(generics.ListAPIView):

    serializer_class = DepHeadRegisterSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        if user.is_chairman == True:
            return self.list(request, *args, **kwargs)
        else:
            response = {"message": "Must be a Chairman"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


# view update and delete through id for department head view


class DepartmentHeadAccountsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated,
                          ]
    queryset = User.objects.all()
    serializer_class = DepHeadRegisterSerializer

    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        if user.is_chairman == True:
            return self.retrieve(request, *args, **kwargs)
        else:
            response = {"message": "Must be a Chairman"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        if user.is_chairman == True:
            return self.update(request, *args, **kwargs)
        else:
            response = {"message": "Must be a Chairman"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user = User.objects.get(email=self.request.user)
        if user.is_chairman == True:
            return self.retrieve(request, *args, **kwargs)
        else:
            response = {"message": "Must be a Chairman"}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
"""
