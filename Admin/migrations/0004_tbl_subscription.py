# Generated by Django 5.0.1 on 2024-02-04 18:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_admin'),
        ('Guest', '0004_alter_tbl_filmuploader_uploader_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_plan', models.CharField(max_length=50)),
                ('subscription_startdate', models.CharField(max_length=50)),
                ('subscription_status', models.CharField(default=0, max_length=2)),
                ('subscription_planamt', models.CharField(max_length=50)),
                ('subscription_details', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
