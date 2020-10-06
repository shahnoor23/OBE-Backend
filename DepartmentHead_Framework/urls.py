from rest_framework import routers
from .api import TeacherViewSet, StudentViewSet , StudentViewByTeacher , TeacherViewByChairman
from django.urls import path, include


router = routers.DefaultRouter()
# department head account router
router.register('api/teacher', TeacherViewSet, 'Teacher')
router.register('api/student', StudentViewSet, 'Student')
router.register('api/te-chairman', TeacherViewByChairman, 'te-chairman')
router.register('api/stu-teacher', StudentViewByTeacher, 'Stu-teacher')
urlpatterns = router.urls
