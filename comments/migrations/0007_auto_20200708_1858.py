# Generated by Django 2.1.5 on 2020-07-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_topic_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Treść'),
        ),
    ]
