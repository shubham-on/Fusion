# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-29 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feeds', '0009_auto_20200227_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tags',
            old_name='my_subtag',
            new_name='tag',
        ),
        migrations.RemoveField(
            model_name='tags',
            name='my_tag',
        ),
        migrations.AlterField(
            model_name='alltags',
            name='tag',
            field=models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('Mechanical', 'Mechanical'), ('Technical-Clubs', 'Technical Clubs'), ('Cultural-Clubs', 'Cultural Clubs'), ('Sports-Clubs', 'Sports Clubs'), ('Business-and-Career', 'Business and Career'), ('Entertainment', 'Entertainment'), ('IIITDMJ-Campus', 'IIITDMJ Campus'), ('Jabalpur-city', 'Jabalpur city'), ('IIITDMJ-Rules-and-Regulations', 'IIITDMJ rules and regulations'), ('Academics', 'Academics'), ('IIITDMJ', 'IIITDMJ'), ('Life-Relationship-and-Self', 'Life Relationship and Self'), ('Technology-and-Education', 'Technology and Education'), ('Programmes', 'Programmes'), ('Others', 'Others'), ('Design', 'Design')], default='CSE', max_length=100),
        ),
    ]
