from django.db import models
from django.utils import timezone




class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} - {self.code}"


class Assignment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField(default=timezone.now,blank=True)
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="assignment"
    )

    def __str__(self):
        return f"{self.title}"


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="announcement"
    )

    def __str__(self):
        return f"{self.title}"


class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return f"{self.name} - {self.code} - {self.branch}"
