# Generated by Django 3.1.5 on 2021-05-03 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0003_auto_20191024_1242'),
        ('filetracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndentFile',
            fields=[
                ('file_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='filetracking.file')),
                ('item_name', models.CharField(max_length=250)),
                ('quantity', models.IntegerField()),
                ('present_stock', models.IntegerField()),
                ('estimated_cost', models.IntegerField(null=True)),
                ('purpose', models.CharField(max_length=250)),
                ('specification', models.CharField(max_length=250)),
                ('indent_type', models.CharField(max_length=250)),
                ('nature', models.BooleanField(default=False)),
                ('indigenous', models.BooleanField(default=False)),
                ('replaced', models.BooleanField(default=False)),
                ('budgetary_head', models.CharField(max_length=250)),
                ('expected_delivery', models.DateField()),
                ('sources_of_supply', models.CharField(max_length=250)),
                ('head_approval', models.BooleanField(default=False)),
                ('director_approval', models.BooleanField(default=False)),
                ('financial_approval', models.BooleanField(default=False)),
                ('purchased', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'IndentFile',
            },
        ),
        migrations.CreateModel(
            name='StockEntry',
            fields=[
                ('item_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='ps1.indentfile')),
                ('vendor', models.CharField(max_length=250)),
                ('item_name', models.CharField(max_length=250)),
                ('current_stock', models.IntegerField()),
                ('recieved_date', models.DateField()),
                ('bill', models.FileField(upload_to='')),
                ('dealing_assistant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'db_table': 'StockEntry',
            },
        ),
    ]
