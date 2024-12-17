from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ROLE_CHOICES = [

        ('admin','Admin'),
        ('office_staff','Office Staff'),
        ('librarian','Librarian'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


class Student(models.Model):

    name = models.CharField(max_length=200)
    class_name = models.CharField(max_length=200)
    age = models.IntegerField()
    Roll_no = models.IntegerField()
    fees_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    

class LibraryHistory(models.Model):

    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    book_title = models.CharField(max_length=200)
    borrowed_date = models.DateField()
    return_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=200,choices=[
        
        ('borrowed','Borrowed'),
        ('returned','Returned')

    ])


class FeesHistory(models.Model):

    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
    remarks = models.TextField()

    def __str__(self):
        return f"{self.student_id} - {self.fee_type}"




