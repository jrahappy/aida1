# Generated by Django 4.1.3 on 2022-11-19 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_remove_customer_website_alter_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='country',
            field=models.CharField(blank=True, choices=[('USA', 'United State'), ('CANADA', 'Canada'), ('SKOREA', 'South Korea'), ('MEXICO', 'Mexico')], default='USA', max_length=30, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]