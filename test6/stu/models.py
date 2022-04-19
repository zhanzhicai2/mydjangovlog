from django.db import models

# Create your models here.


class Clazz(models.Model):
    cname = models.CharField(max_length=30)


class Student(models.Model):
    sname = models.CharField(max_length=30)
    score = models.PositiveIntegerField()
    cls = models.ForeignKey(Clazz, on_delete=models.CASCADE)

    def save(self, force_insert=False, force_update=False, using=None,update_fields=None):
        try:
            self.cls = Clazz.objects.get(cname=self.cls.cname)
        except Clazz.DoesNotExist:
            self.cls = Clazz.objects.create(cname=self.cls.cname)

#         学生表的插入
        models.Model.save(self, force_insert=False, force_update=False, using=None,update_fields=None)

# def showsql():
#     from django.db import connection
#     print(connection.queries[-1]['sql'])




# Student.save()

