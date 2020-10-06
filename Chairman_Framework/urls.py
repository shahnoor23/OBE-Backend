from rest_framework import routers
from .api import PEOViewSet, DepartmentHeadViewSet, PEOViewSet, VisionViewSet, MissionViewSet, PLOViewSet, CoursesViewSet, CLOViewSet, CognitiveViewSet, PsychomotorViewSet, AffectiveViewSet, CoursesAssignViewSet, ViewAssignedCoursesToTeacher
from django.urls import path, include
from DepartmentHead_Framework.api import TeacherViewSet
from Accounts.api import InvertoryUpload , Profile

router = routers.DefaultRouter()

router.register('api/upload', InvertoryUpload, 'upload'),
router.register('api/profile', Profile, 'profile'),

# department head account router
router.register('api/department', DepartmentHeadViewSet, 'DepartmentHead')
# below router is for teachers which can be view by chairman
router.register('api/teachers', TeacherViewSet, 'teachers')
# router for peo view
router.register('api/peo', PEOViewSet, 'peo')
router.register('api/vision', VisionViewSet, 'vision')
router.register('api/mission', MissionViewSet, 'mission')
router.register('api/plo', PLOViewSet, 'plo')
router.register('api/clo', CLOViewSet, 'clo')
router.register('api/courses', CoursesViewSet, 'courses')
router.register('api/Cognitive', CognitiveViewSet, 'Cognitive')
router.register('api/Psychomotor', PsychomotorViewSet, 'Psychomotor')
router.register('api/Affective', AffectiveViewSet, 'Affective')
router.register('api/coursesassign', CoursesAssignViewSet, 'coursesassign')
router.register('api/assigned', ViewAssignedCoursesToTeacher, 'assigned')
urlpatterns = router.urls
