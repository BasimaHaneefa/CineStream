# Generated by Django 5.0.1 on 2024-01-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_tbl_lang'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50)),
                ('admin_email', models.CharField(max_length=50)),
                ('admin_cno', models.CharField(max_length=50)),
                ('admin_pword', models.CharField(max_length=50)),
            ],
        ),
    ]
