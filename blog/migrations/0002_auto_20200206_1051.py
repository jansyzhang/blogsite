# Generated by Django 2.2.5 on 2020-02-06 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_time']},
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='type_name',
            field=models.CharField(max_length=50),
        ),
    ]
