# Generated by Django 2.0.6 on 2018-06-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aris_app', '0004_auto_20180614_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.IntegerField(max_length=14),
        ),
    ]