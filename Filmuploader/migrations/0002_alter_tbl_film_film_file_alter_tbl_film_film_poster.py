# Generated by Django 5.0.1 on 2024-02-07 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filmuploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_film',
            name='film_file',
            field=models.FileField(upload_to='Uploaderdocs/'),
        ),
        migrations.AlterField(
            model_name='tbl_film',
            name='film_poster',
            field=models.FileField(upload_to='Uploaderdocs/'),
        ),
    ]
