# Generated by Django 3.1.5 on 2021-05-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office_module', '0003_auto_20210504_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostel_allotment',
            name='year',
            field=models.IntegerField(default=2016),
        ),
    ]
