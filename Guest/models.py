from django.db import models

# Create your models here.
class tbl_filmuploader(models.Model):
    uploader_name=models.CharField(max_length=50)
    uploader_email=models.CharField(max_length=50)
    uploader_contact=models.CharField(max_length=50)
    uploader_address=models.CharField(max_length=100)
    uploader_photo=models.FileField(max_length=50,upload_to='Uploaderphoto/')
    uploader_proof=models.FileField(max_length=50,upload_to='Uploaderphoto/')
    uploader_password=models.CharField(max_length=50)
    uploader_vstatus=models.CharField(max_length=2,default=0)

class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_photo=models.FileField(max_length=50,upload_to='Userphoto/')
    user_password=models.CharField(max_length=50)
  