# Generated by Django 3.2 on 2022-12-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridge_app', '0011_auto_20221225_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companionrequest',
            name='finish_latitude',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='companionrequest',
            name='finish_longitude',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='companionrequest',
            name='start_latitude',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='companionrequest',
            name='start_longitude',
            field=models.CharField(max_length=20),
        ),
    ]
