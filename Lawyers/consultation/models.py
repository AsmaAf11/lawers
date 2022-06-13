from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Lawyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contract_speciality = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.user.username


class Users(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)



'''class Consultation(models.Model):
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return str(self.user.username)
 '''


class Consultation_request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lawyer = models.ForeignKey(Lawyer, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return str(self.user.username)


class Consultation_replay(models.Model):
    consultation_request = models.ForeignKey(Consultation_request, on_delete=models.CASCADE)
    replay = models.TextField()
