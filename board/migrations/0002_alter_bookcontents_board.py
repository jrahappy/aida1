# Generated by Django 4.1.3 on 2022-11-26 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookcontents',
            name='board',
            field=models.IntegerField(default=0),
        ),
    ]