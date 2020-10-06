from Accounts.serializers import ChairmanRegisterSerializer
from rest_framework import viewsets, permissions, generics
from Accounts.permissions import AdminUser
from Accounts.models import User
# Teacher Account View Set


class ChairmanViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = User.objects.filter(is_chairman=True)
        queryset1 = queryset.filter(university=self.request.user.university)
        return queryset1
    serializer_class = ChairmanRegisterSerializer

    def perform_create(self, serializer):
        serializer.save(university=self.request.user.university)
    def get_permissions(self):
        
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AdminUser]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AdminUser]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AdminUser]
        return [permission() for permission in permission_classes]
