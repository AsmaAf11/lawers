from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class lawyer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contract_speciality = models.CharField(max_length=50)
    years_of_experience = models.IntegerField()
    consultation_price = models.IntegerField()


class consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()


class consultation_request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consultation = models.ForeignKey(consultation, on_delete=models.CASCADE)
    content = models.TextField()


class consultation_replay(models.Model):
    consultation_request = models.ForeignKey(consultation_request, on_delete=models.CASCADE)
    replay = models.TextField()
