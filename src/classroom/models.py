from django.db import models


class Assigment(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    assigment = models.ForeignKey(Assigment, on_delete=models.CASCADE, default=" ")
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, default=" ")

    def __str__(self):
        return f"{self.name} - {self.code}"


class ClassRoom(models.Model):
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    subject = models.ForeignKey(Subject, on_delete=models.SET_DEFAULT, default=" ")

    def __str__(self):
        return f"{self.name} - {self.code} - {self.branch}"
