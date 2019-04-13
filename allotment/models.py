from django.db import models
from django.contrib.auth.models import User
from administrator.models import Batch
from professor.models import Professor


class Group(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    group_id = models.AutoField(primary_key=True)
    mentor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=models.SET_NULL)
    preference_of_professor = models.CharField(max_length=256, default=',')
