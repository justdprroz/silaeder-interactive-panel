from lib2to3.pgen2.token import NAME
from django.conf import settings
from django.db import models
from django.utils import timezone
from . import views
import sqlite3
import json


class Achievements(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
