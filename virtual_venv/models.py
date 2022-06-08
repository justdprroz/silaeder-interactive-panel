# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    name_field = models.TextField(db_column='Name ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    teacher = models.TextField(db_column='Teacher', blank=True, null=True)  # Field name made lowercase.
    subject = models.TextField(db_column='Subject', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mytable'
