# Generated by Django 4.1.3 on 2022-11-23 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_department_customuser_sales_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_category',
            field=models.CharField(default='patient', max_length=2),
        ),
    ]