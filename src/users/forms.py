from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *


class StudentRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user


class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ["phone_no", "branch", "year", "roll_no", "class_assigned", "image"]


class TeacherRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user


class TeacherProfileForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ["phone_no", "branch", "image"]
