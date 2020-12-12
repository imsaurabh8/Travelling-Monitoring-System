from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Register(models.Model):
    adhaar_number=models.CharField(max_length=15,default="")
    name=models.CharField(max_length=70,default="")
    email=models.CharField(max_length=70,default="")
    gender=models.CharField(max_length=10,default="")
    phone_no=models.CharField(max_length=10,default="")
    age = models.CharField(max_length=3,default='')
    person=models.ForeignKey(User,default=None,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class History(models.Model):

    source=models.CharField(max_length=70)
    dest=models.CharField(max_length=70)
    tv_date=models.DateTimeField(blank=True,null=True)
    transportation=models.CharField(max_length=40)
    co_pass = models.IntegerField()
    person = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.source + "-" + self.dest


class Hospital(models.Model):

    name=models.CharField(max_length=70)
    room_no=models.IntegerField()
    room_type=models.CharField(max_length=10)
    bill = models.IntegerField()
    person = models.ForeignKey(User, default=None, on_delete=models.CASCADE)



    def __str__(self):
        return self.name

class Feedback(models.Model):

    covid_days=models.CharField(max_length=20)
    hosp_clean=models.CharField(max_length=10)
    food_quality=models.CharField(max_length=20)
    travel_exp = models.CharField(max_length=300)
    improvement = models.CharField(max_length=300)
    person = models.ForeignKey(User, default=None, on_delete=models.CASCADE)



    def __str__(self):
        return self.covid_days


class Test(models.Model):

    test_done=models.CharField(max_length=10)
    test_result=models.CharField(max_length=10)
    quarentined=models.CharField(max_length=10)

    person = models.ForeignKey(User, default=None, on_delete=models.CASCADE)



    def __str__(self):
        return self.quarentined





