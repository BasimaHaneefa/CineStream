from django.db import models
from Guest.models import *

# Create your models here.
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_cno=models.CharField(max_length=50)
    admin_pword=models.CharField(max_length=50)

class tbl_genre(models.Model):
    genre_name=models.CharField(max_length=50)

class tbl_lang(models.Model):
    lang_name=models.CharField(max_length=50)

class tbl_subscription(models.Model):
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    subscription_plan=models.CharField(max_length=50)
    subscription_startdate=models.CharField(max_length=50)
    subscription_status=models.CharField(max_length=2,default=0)
    subscription_planamt=models.CharField(max_length=50)
    subscription_details=models.CharField(max_length=200)

