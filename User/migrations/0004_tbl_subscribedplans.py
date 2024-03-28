# Generated by Django 4.2.7 on 2024-02-25 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_tbl_subscription'),
        ('Guest', '0004_alter_tbl_filmuploader_uploader_photo_and_more'),
        ('User', '0003_tbl_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_subscribedplans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_startdate', models.DateField(auto_now_add=True)),
                ('subscription_status', models.CharField(default=0, max_length=10)),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_subscription')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
