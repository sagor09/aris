# Generated by Django 2.0.5 on 2018-06-03 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aris_app', '0012_auto_20180603_0555'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_title', models.CharField(max_length=20)),
                ('portfolio_class', models.CharField(max_length=10)),
                ('portfolio_data_filter', models.CharField(max_length=10)),
                ('portfolio_image', models.ImageField(upload_to='portfolio')),
                ('portfolio_image2', models.ImageField(upload_to='portfolio')),
            ],
        ),
    ]
