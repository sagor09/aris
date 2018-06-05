# Generated by Django 2.0.5 on 2018-06-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aris_app', '0014_auto_20180604_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=40)),
                ('profile_pic', models.ImageField(upload_to='team')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]