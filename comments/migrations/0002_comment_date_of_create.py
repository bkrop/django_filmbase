# Generated by Django 2.1.5 on 2020-06-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_of_create',
            field=models.DateField(auto_now=True),
        ),
    ]
