# Generated by Django 4.2.7 on 2024-02-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_tbl_subscribedplans'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_subscribedplans',
            name='payment_status',
            field=models.CharField(default=0, max_length=10, null=True),
        ),
    ]