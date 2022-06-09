from lib2to3.pgen2.token import NAME
from django.conf import settings
from django.db import models
from django.utils import timezone
from . import views



"""class clubs(models.Model):
    name = models.CharField(max_length=200)
                teacher = models.CharField(max_length=200)
                subject = models.CharField(max_length=200)
  
            
                def __str__(self):
                    return self.name, self.teacher, self.subject"""
class BlogClubs(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'blog_clubs'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Mytable(models.Model):
    index = models.IntegerField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    teacher = models.TextField(db_column='Teacher', blank=True, null=True)  # Field name made lowercase.
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'mytable'

class Olympiads(models.Model):
    index = models.IntegerField(blank=True, null=True)
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    event = models.TextField(db_column='Event', blank=True, null=True)
    clas = models.TextField(db_column='Class', blank=True, null=True)
    head_teacher = models.TextField(db_column='Head-teacher', blank=True, null=True)  # Field name made lowercase.
    level = models.TextField(db_column='Level', blank=True, null=True)
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.
    participants = models.TextField(db_column='Participants', blank=True, null=True)
    result = models.TextField(db_column='Result', blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'olympiads'
    
