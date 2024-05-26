from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CourseViewSet, LessonViewSet, QuizViewSet, EnrollmentViewSet, index

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'enrollments', EnrollmentViewSet)


urlpatterns = [
    path('', index),
    path('api/', include(router.urls))
]
