from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CourseViewSet, LessonViewset, QuizViewSet, EnrollmentViewSet

router = DefaultRouter()


urlpatterns = [
    path('', include(router.urls))
]
