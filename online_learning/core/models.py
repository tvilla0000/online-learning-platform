from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

# Here is our model for the Users
class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='custom_use_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get permissions granted to each of their groups.',
        related_query_name='user',
    )
    users_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user',
        related_query_name='user'
    )

    pass

# Here is our model for the Courses
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    difficulty_level = models.CharField(max_length=50)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')

    def __str__(self): 
        return self.title
    
# Here is our model for the Lessons
class Lesson(models.Model): 
    title = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.title

# Here is our model for the Quizzes
class Quiz(models.Model):
    question = models.CharField(max_length=255)
    options = models.JSONField()
    correct_answer = models.CharField(max_length=255)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.question
    
# Here is our Enrollment Model
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} enrolled in {self.course.title}'