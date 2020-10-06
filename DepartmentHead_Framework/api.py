from Accounts.serializers import TeacherRegisterSerializer, StudentRegisterSerializer
from rest_framework import viewsets, permissions, generics
from Accounts.permissions import IsDepartmentHeadUser, IsChairmanUser, IsTeacherUser
from Accounts.models import User
# Teacher Account View Set


class TeacherViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.filter(is_teacher=True)
    def get_queryset(self):
        queryset = User.objects.filter(is_teacher=True)
        queryset1 = queryset.filter(department=self.request.user.department, university=self.request.user.university )
        return queryset1
    serializer_class = TeacherRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(department=self.request.user.department, university=self.request.user.university)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsDepartmentHeadUser]
           
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsDepartmentHeadUser]
            
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsDepartmentHeadUser]
        return [permission() for permission in permission_classes]



#Teacher view by Chairman

class TeacherViewByChairman(viewsets.ModelViewSet):
    #queryset = User.objects.filter(is_teacher=True)
    def get_queryset(self):
        queryset = User.objects.filter(is_teacher=True)
        queryset1 = queryset.filter(department=self.request.user.department, university=self.request.user.university)
        return queryset1
    serializer_class = TeacherRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(department=self.request.user.department, university=self.request.user.university)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsChairmanUser]
        return [permission() for permission in permission_classes]

# Student Account View Set


class StudentViewSet(viewsets.ModelViewSet):
    #queryset = User.objects.filter(is_student=True)
    def get_queryset(self):
        queryset = User.objects.filter(is_student=True)
        queryset1 = queryset.filter(department=self.request.user.department, university=self.request.user.university)
        return queryset1
    serializer_class = StudentRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(department=self.request.user.department, university=self.request.user.university)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [IsDepartmentHeadUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsDepartmentHeadUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsDepartmentHeadUser] 

        return [permission() for permission in permission_classes]




# Student view by Teacher

class StudentViewByTeacher(viewsets.ModelViewSet):
    #queryset = User.objects.filter(is_student=True)
    def get_queryset(self):
        queryset = User.objects.filter(is_student=True)
        queryset1 = queryset.filter(department=self.request.user.department, university=self.request.user.university, batch=self.request.user.batch , year=self.request.user.year, semester=self.request.user.semester)
        return queryset1
    serializer_class = StudentRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(department=self.request.user.department, university=self.request.user.university)

    def get_permissions(self):
        permission_classes = []
        if self.action == 'list':
            permission_classes = [IsTeacherUser]
       

        return [permission() for permission in permission_classes]