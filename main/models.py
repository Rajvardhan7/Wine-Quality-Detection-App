from django.db import models

# Create your models here.
class MLdata(models.Model):
    age = models.IntegerField(null = True)
    workclass = models.IntegerField(null = True)
    fnlwgt = models.IntegerField(null = True)
    education = models.IntegerField(null = True)
    education_num = models.IntegerField(null = True)
    martial_status = models.IntegerField(null = True)
    occupation = models.IntegerField(null = True)
    relationship = models.IntegerField(null = True)
    race = models.IntegerField(null = True)
    sex = models.IntegerField(null = True)
    capital_gain = models.IntegerField(null = True)
    capital_loss = models.IntegerField(null = True)
    hoursperweek = models.IntegerField(null = True)
    native_country = models.IntegerField(null = True)
    prediction = models.CharField(max_length = 20, null = True)



  #  {'age': 31.0,
 #'workclass': 3.0,
 #'fnlwgt': 121124.0,
 #'education': 11.0,
 #'education-num': 9.0,
 ##'marital-status': 2.0,
 #'occupation': 9.0,
 #'relationship': 0.0,
 ##'race': 4.0,
 #'sex': 1.0,
 #'capital-gain': 0.0,
 #'capital-loss': 0.0,
 #'hours-per-week': 40.0,
 #'native-country': 37.0}