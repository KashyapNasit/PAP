from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from allotment.models import Group


class TeamFormation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slot_no = models.IntegerField(null=True)
    group = models.ForeignKey(Group, null=True, on_delete=models.CharField)
    requests = models.CharField(default=",", max_length=256)  # Coma separated list of GroupID


@receiver(post_save, sender=User)
def update_user_teamformation(sender, instance, created, **kwargs):
    if created and (instance.is_staff != True):
        TeamFormation.objects.create(user=instance)
        instance.teamformation.save()

