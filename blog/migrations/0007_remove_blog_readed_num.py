# Generated by Django 2.2.5 on 2020-02-18 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_readnum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='readed_num',
        ),
    ]