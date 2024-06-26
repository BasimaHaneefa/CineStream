# Generated by Django 5.0.1 on 2024-01-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0003_alter_tbl_filmuploader_uploader_vstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_filmuploader',
            name='uploader_photo',
            field=models.FileField(max_length=50, upload_to='Uploaderphoto/'),
        ),
        migrations.AlterField(
            model_name='tbl_filmuploader',
            name='uploader_proof',
            field=models.FileField(max_length=50, upload_to='Uploaderphoto/'),
        ),
        migrations.AlterField(
            model_name='tbl_user',
            name='user_photo',
            field=models.FileField(max_length=50, upload_to='Userphoto/'),
        ),
    ]
