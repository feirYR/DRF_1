# Generated by Django 2.0.6 on 2020-06-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.SmallIntegerField(),
        ),
    ]