from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from .models import User, Course, Lesson, Quiz, Enrollment
import datetime

# Create your tests here.

class UserModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testuser1',
            email = 'testuser1@example.com',
            password = 'testpassword1',
            role = 'student',
            bio = 'Test Bio',
            date_of_birth = datetime.date(2000, 1, 1),
            phone_number = '1234567890',
            address = '123 Test St',
            linkedin_profile = 'https://www.linkedin.com/in/testuser/',
            enrollent_date = datetime.date.today(),
            skills = 'Python, Django'
        )

        #Assign groups and permissions
        self.group = Group.objects.create(name='testgroup')
        self.user.groups.add(self.group)
        self.permission = Permission.objects.create(name='test_permission', codename='test_permission')
        self.user.user_permissions.add(self.permission)

    
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser1')
        self.assertEqual(self.user.email, 'testuser1@example.com')
        self.assertTrue(self.user.check_password, 'testpassword1')
        self.assertEqual(self.user.role, 'student')
        self.assertEqual(self.user.bio, 'Test Bio')
        self.assertEqual(self.user.date_of_birth, datetime.date(2000, 5, 1))
        self.assertEqual(self.user.phone_number, '1234567890')
        self.assertEqual(self.user.address, '123 Test St')
        self.assertEqual(self.user.linkedin_profile, 'https://www.linkedin.com/in/testuser/')
        self.assertEqual(self.user.skills, 'Python, Django')
        self.assertEqual(self.user.enrollment_date, datetime.date.today())

        #Check groups and permissions
        self.assertIn(self.group, self.user.groups.all())
        self.assertIn(self.permission, self.user.user_permissions.all())

    def test_user_profile_picture_blank(self):

        #Profile picture should already be blank by default
        self.assertFalse(self.user.profile_picture)

class CourseModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'testinstructor',
            email = 'testinstructor@example.com',
            password = 'testpassword',
            role = 'instructor'
        )
        self.course = Course.objects.create(
            title = 'Test Course',
            description = 'Test Description',
            category = 'Test Category',
            difficulty_level = 'Test Difficulty',
            instructor = self.user
        )

    def test_course_creation(self):
        self.assertEqual(self.course.title, 'Test Course')
        self.assertEqual(self.course.description, 'Test Description')
        self.assertEqual(self.course.category, 'Test Category')
        self.assertEqual(self.course.difficulty_level, 'Test Difficulty')
        self.assertEqual(self.course.instructor, self.user)