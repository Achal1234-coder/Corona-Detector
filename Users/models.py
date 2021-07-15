from django.db import models


class UserSymptomFormModel(models.Model):

    CHOICES = (
   (1, 'True'),
   (0, 'False')
)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone_no = models.IntegerField()
    address = models.TextField()
    cough = models.IntegerField(choices=CHOICES)
    cold = models.IntegerField(choices=CHOICES)
    fever = models.IntegerField(choices=CHOICES)
    breath_less_ness = models.IntegerField(choices=CHOICES)
    pain = models.IntegerField(choices=CHOICES)
    loss_of_test_or_smell = models.IntegerField(choices=CHOICES)
    sore_throat = models.IntegerField(choices=CHOICES)
