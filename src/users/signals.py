from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Teacher, Student


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    print(instance)
    print(instance.is_teacher)
    if created:
        if instance.is_teacher:
            Teacher.objects.create(user=instance)
        else:
            Student.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
