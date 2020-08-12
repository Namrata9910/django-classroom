from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from PIL import Image
from classroom.models import ClassRoom


class User(AbstractUser):
    is_student = models.BooleanField("student status", default=False)
    is_teacher = models.BooleanField("teacher status", default=False)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(default="", max_length=20, blank=True, null=True)
    branch = models.CharField(default="", max_length=500, blank=True, null=True)
    class_assigned = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(
        default="teacher_profile_pics/default.jpg", upload_to="teacher_profile_pics"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        width, height = img.size
        if height >= 300 or width >= 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.user.username} Profile"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(default="", max_length=20, blank=True, null=True)
    branch = models.CharField(default="", max_length=500, blank=True, null=True)
    year = models.CharField(default="", max_length=20, blank=True, null=True)
    roll_no = models.CharField(default="", max_length=20, blank=True, null=True)
    class_assigned = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(
        default="teacher_profile_pics/default.jpg", upload_to="student_profile_pics"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        width, height = img.size
        if height >= 300 or width >= 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def __str__(self):
        return f"{self.user.username} Profile"
