# Generated by Django 4.1.3 on 2022-11-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0006_remove_person_salutation_customer_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_myclinic',
            field=models.BooleanField(default=False),
        ),
    ]
