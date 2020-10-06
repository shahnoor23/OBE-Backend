from .models import PEO, CourseAssign
from rest_framework import viewsets, permissions, generics
from Chairman_Framework.serializers import VisionSerializer, PEOSerializer, MissionSerializer, PLOSerializer, CoursesSerializer, CLOSerializer, CognitiveSerializer, PsychomotorSerializer, AffectiveSerializer, CourseAssignSerializer
from Accounts.serializers import DepHeadRegisterSerializer
from Accounts.models import User
from django.db.models.functions import Concat
from django.db.models import Value
from Accounts.permissions import IsChairmanUser, IsLoggedInUserOrAdmin, IsTeacherUser

# Department Head Account View Set


class DepartmentHeadViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.filter(department)
    #a = request.user.department
    #queryset = User.objects.select_related('department')
    # queryset = SELECT department FROM accounts_user INNER JOIN accounts_user ON (self.department = accounts_user.department)
    # def department(request):
     #  dep = request.user.department
    # def sample_view(self, request):
     #current_user = self.request.user.department
    #queryset1 = User.objects.filter()
    # def get_queryset(self):
     #   return self.request.user.department
    #queryset = self.request.user.department
    #queryset2 = User.objects.filter()
    #queryset2 = queryset.filter(queryset=current_user.department)
    #q2 = self.request.user.department
    #intersection = queryset1 & q2
    def get_queryset(self):
        queryset = User.objects.filter(is_depHead=True)
        queryset1 = queryset.filter(
            department=self.request.user.department, university=self.request.user.university)
    #queryset = user.objects.filter(is_depHead=True)
        return queryset1
    serializer_class = DepHeadRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(department=self.request.user.department,
                        university=self.request.user.university)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]


# PEO VIEWSET only operations performed by chairman


class PEOViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PEOSerializer
    # queryset = PEO.objects.all()

    def get_queryset(self):
        return self.request.user.peo.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]

# VISION VIEW SET


class VisionViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = VisionSerializer

    def get_queryset(self):
        return self.request.user.vision.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]


# MISSION VIEW SET
class MissionViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = MissionSerializer

    def get_queryset(self):
        return self.request.user.mission.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]

# plo viewset


class PLOViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PLOSerializer

    def get_queryset(self):
        return self.request.user.plo.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]

# clo viewset


class CLOViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CLOSerializer

    def get_queryset(self):
        return self.request.user.clo.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]


# courses viewset


class CoursesViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CoursesSerializer

    def get_queryset(self):
        return self.request.user.courses.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]


# CognitiveViewSet
class CognitiveViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CognitiveSerializer

    def get_queryset(self):
        return self.request.user.cognitive.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]


# Psychomotor view


class PsychomotorViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PsychomotorSerializer

    def get_queryset(self):
        return self.request.user.psychomotor.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]

# Affective view


class AffectiveViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = AffectiveSerializer

    def get_queryset(self):
        return self.request.user.affective.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]

# courses assign viewset


class CoursesAssignViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CourseAssignSerializer
    queryset = CourseAssign.objects.all()

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsChairmanUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsChairmanUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]


# only assigned courses to teachers can be viewed by particular teacher

class ViewAssignedCoursesToTeacher(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = CourseAssignSerializer

    def get_queryset(self):
        user = self.request.user
        return CourseAssign.objects.filter(teacher_name=user)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsTeacherUser]
        return [permission() for permission in permission_classes]
