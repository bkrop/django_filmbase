# Generated by Django 2.1.5 on 2020-06-22 19:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_auto_20200622_1928'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='rate',
            unique_together={('sender', 'person')},
        ),
    ]
