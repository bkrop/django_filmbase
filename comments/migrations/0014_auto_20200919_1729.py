# Generated by Django 2.1.5 on 2020-09-19 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0013_auto_20200919_1620'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='reply',
            new_name='comment',
        ),
    ]