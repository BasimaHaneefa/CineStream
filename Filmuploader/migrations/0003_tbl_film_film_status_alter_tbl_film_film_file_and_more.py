# Generated by Django 5.0.1 on 2024-02-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Filmuploader', '0002_alter_tbl_film_film_file_alter_tbl_film_film_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_film',
            name='film_status',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='tbl_film',
            name='film_file',
            field=models.FileField(max_length=50, upload_to='Uploaderdocs/'),
        ),
        migrations.AlterField(
            model_name='tbl_film',
            name='film_poster',
            field=models.FileField(max_length=50, upload_to='Uploaderdocs/'),
        ),
    ]
