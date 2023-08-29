# Generated by Django 3.2.16 on 2023-08-27 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='city',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='conditions',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='temperature',
        ),
        migrations.AddField(
            model_name='weather',
            name='department',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='weather',
            name='employee',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='weather',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]