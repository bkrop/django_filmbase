# Generated by Django 2.1.5 on 2020-08-30 09:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200830_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_of_create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
