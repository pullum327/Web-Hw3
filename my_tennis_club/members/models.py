from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# class Reservation(models.Model):
#     court = models.ForeignKey(TennisCourt, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     reservation_date = models.DateField()
#     reservation_time = models.TimeField()
#     reservation_length = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.user.username} - {self.reservation_date} at {self.reservation_time}"
class Reservation(models.Model):
    court = models.ForeignKey('TennisCourt', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    reservation_length = models.PositiveIntegerField()
    
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  age = models.IntegerField(null=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  def __str__(self):
    return f"{self.firstname} {self.lastname}"  
class TennisCourt(models.Model):
    COURT_TYPES = [
        ('grass', 'Grass'),
        ('hard', 'Hard'),
        ('clay', 'Clay'),
        ('carpet', 'Carpet'),
    ]

    name = models.CharField(max_length=255)
    court_type = models.CharField(max_length=10, choices=COURT_TYPES)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.name
