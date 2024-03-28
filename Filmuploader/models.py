from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.
class tbl_film(models.Model):
    film_title=models.CharField(max_length=50)
    film_disc=models.CharField(max_length=50)
    film_genre=models.ForeignKey(tbl_genre,on_delete=models.CASCADE)
    film_lang=models.ForeignKey(tbl_lang,on_delete=models.CASCADE)
    film_duration=models.CharField(max_length=50)
    film_poster=models.FileField(max_length=50,upload_to='Uploaderdocs/')
    film_uploader=models.ForeignKey(tbl_filmuploader,on_delete=models.CASCADE)
    upload_date=models.DateField(auto_now_add=True)
    film_file=models.FileField(max_length=50,upload_to='Uploaderdocs/')
    film_status=models.CharField(max_length=2,default=0)
    
class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    uploader_from = models.ForeignKey(tbl_filmuploader,on_delete=models.CASCADE,related_name="uploader_from",null=True)
    uploader_to = models.ForeignKey(tbl_filmuploader,on_delete=models.CASCADE,related_name="uploader_to",null=True)
    admin_from=models.ForeignKey(tbl_admin,on_delete=models.CASCADE,related_name="admin_from",null=True)
    admin_to=models.ForeignKey(tbl_admin,on_delete=models.CASCADE,related_name="doctor_to",null=True)
  


