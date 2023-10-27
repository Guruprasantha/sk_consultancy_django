


from django.db import models

class data(models.Model):
    work = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    d_no = models.CharField(max_length=20)
    s_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    mobile_no2 = models.CharField(max_length=100)
    mail_id = models.EmailField(max_length=100)
    issue=models.CharField(max_length=100)
