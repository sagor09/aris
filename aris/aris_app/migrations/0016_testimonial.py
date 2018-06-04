# Generated by Django 2.0.5 on 2018-06-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aris_app', '0015_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('designation', models.CharField(max_length=40)),
                ('testimonial_user_pic', models.ImageField(upload_to='testimonial')),
                ('description', models.TextField()),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
