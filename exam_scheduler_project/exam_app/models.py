from django.db import models

# Create your models here.
class Dept(models.Model):
    did = models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=20)

    def __str__(self):
        return self.dname

class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    did = models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    fid = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=30)
    did = models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.fname


class Course(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=20)
    did = models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.cname


class Room(models.Model):
    rid = models.IntegerField(primary_key=True)
    capacity=models.IntegerField()




class Slot(models.Model):

    class Meta:
        unique_together =(('date','time'),)

    date = models.DateField()
    time = models.CharField(max_length=2)




class Exam_student(models.Model):
    cid = models.ForeignKey(Course,on_delete=models.CASCADE)
    sid = models.ForeignKey(Student,on_delete=models.CASCADE)

    class Meta:
        unique_together =(('cid','sid'),)




class Exam(models.Model):
    cid = models.ForeignKey(Course,on_delete=models.CASCADE,unique=True)
    date = models.ForeignKey(Slot,related_name='DateField',on_delete=models.CASCADE)
    time = models.ForeignKey(Slot,related_name='CharField',on_delete=models.CASCADE)
    rid = models.ForeignKey(Room,on_delete=models.CASCADE)




class Exam_faculty(models.Model):

    class Meta:
        unique_together =(('cid','fid'),)

    cid = models.ForeignKey(Course,on_delete=models.CASCADE)
    fid = models.ForeignKey(Faculty,on_delete=models.CASCADE)
