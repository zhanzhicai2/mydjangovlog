from django.db import models

# Create your models here.


# class Student(models.Model):
#     name = models.CharField(max_length=255, blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'student'
#
#
# class Stu(models.Model):
#     id = models.IntegerField(primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'stu'


class City(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=35)  # Field name made lowercase.
    countrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryCode')  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=20)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'city'

