from django.db import models
from Filmuploader.models import *
from Guest.models import *

# Create your models here.

class tbl_wishlist(models.Model):
    wishlist_status=models.CharField(max_length=50,default=0)
    film_id=models.ForeignKey(tbl_film,on_delete=models.CASCADE)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=100)
    complaint_date=models.DateField(auto_now_add=True,null=True)
    complaint_reply=models.CharField(max_length=50,default='Not Replied')
    complaint_status=models.CharField(max_length=50,default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=100)
    feedback_date=models.DateField(auto_now_add=True,null=True)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

class tbl_subscribedplans(models.Model):
    plan=models.ForeignKey(tbl_subscription,on_delete=models.CASCADE)
    subscription_startdate=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    subscription_status=models.CharField(max_length=10,default=0)
    payment_status=models.CharField(max_length=10,default=0,null=True)

class tbl_watchedfilm(models.Model):
    film=models.ForeignKey(tbl_film,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    watch_status=models.CharField(max_length=10,default=0)
    watch_datetime=models.DateTimeField(auto_now_add=True,null=True)

class tbl_review(models.Model):
    user_rating=models.IntegerField()
    user_review=models.CharField(max_length=20)
    user_name=models.CharField(max_length=20)
    review_datetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    film=models.ForeignKey(tbl_film,on_delete=models.CASCADE)
